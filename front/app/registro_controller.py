# -*- coding: utf-8 -*-
import json
from pdb import set_trace
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, NumberRange, Length
from app import app, request, redirect, flash, url_for, render_template, Blueprint, Api

registro_blueprint = Blueprint('registro', __name__, template_folder='templates')

class RegistroForm(FlaskForm):
    carro = IntegerField('Carro', validators=[DataRequired()])
    cliente = IntegerField('Cliente', validators=[DataRequired()])
    data = DateField('Data', validators=[DataRequired()])
    tipo = SelectField('Tipo Registro', validators=[DataRequired()],choices=[('ENTRADA','Entrada'),('SAIDA',u'Saída')])
    

    def criar_registro(self):
        return {
            'idCarro': self.carro.data,
            'idCliente': self.cliente.data,
            'data': datetime.strftime(self.data.data, '%Y-%m-%d %H:%M:%S'),
            'tipo': self.tipo.data,
        }

def retornar_registro(dados):
    return {
        'carro':dados['idCarro'],
        'cliente':dados['idCliente'],
        'data':dados['data'],
        'tipo':dados['tipo'],
    }

@registro_blueprint.route('/form/', defaults={'pk':None}, methods = ['post', 'get'])
@registro_blueprint.route('/form/<pk>', methods = ['post', 'get'])
def form(pk):
    #set_trace()
    form = RegistroForm()
    contexto = {}
    try:
        endpoint = '/registro/'
        retorno = False
        if pk:
            endpoint += pk
        if form.validate_on_submit():
            dados = form.criar_registro()
            if pk and pk in endpoint:
                '''Atualizando'''
                retorno = Api.atualizar(endpoint, dados)
                flash(u'Registro com código %s foi salvo com sucesso'%(retorno.pk), 'success')
            else:
                '''Salvando'''
                retorno = Api.salvar(endpoint, dados)
                flash(u'Registro com código %s foi atualizado com sucesso'%(retorno.pk), 'success')
            if retorno:
                return redirect(url_for('registro.form', pk=retorno.pk))
            else:
                '''Erro'''
                flash(retorno.text, 'danger')
        elif pk:
            '''Editar'''
            retorno = Api.buscar(endpoint)
            if retorno:
                dados = retornar_registro(retorno.dados)
                form = RegistroForm(**dados)
    except Exception as ex:
        mensagem = str(ex)
    contexto['form'] = form
    return render_template('registro/form.html', **contexto), 200