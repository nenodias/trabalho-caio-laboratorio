# -*- coding: utf-8 -*-
import json
from pdb import set_trace
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, NumberRange, Length
from app import app, request, redirect, flash, url_for, render_template, Blueprint, Api

registro_blueprint = Blueprint('registro', __name__, template_folder='templates/registro')

TIPO_ENTRADA = (u'ENTRADA',u'Entrada')
TIPO_SAIDA = (u'SAIDA',u'Saída')

class RegistroForm(FlaskForm):
    carro = IntegerField('Carro', validators=[DataRequired()])
    cliente = IntegerField('Cliente', validators=[DataRequired()])
    data = DateField('Data', validators=[DataRequired()])
    tipo = SelectField('Tipo Registro',coerce=str, validators=[DataRequired()],choices=[TIPO_ENTRADA,TIPO_SAIDA])
    

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
        'data':datetime.strptime(dados['data'], '%Y-%m-%d %H:%M:%S'),
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
                set_trace()
                dados = retornar_registro(retorno.dados)
                form = RegistroForm()
                form.carro.data = dados['carro']
                form.cliente.data = dados['carro']
                form.data.data = dados['data']
                form.tipo.data = dados['tipo']
    except Exception as ex:
        flash(str(ex), 'info')
    contexto['form'] = form
    return render_template('form.html', **contexto), 200