# -*- coding: utf-8 -*-
import json
from pdb import set_trace
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, NumberRange, Length
from app import app, request, redirect, flash, url_for, render_template, Blueprint, Api

registro_blueprint = Blueprint('registro', __name__)

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
                form.cliente.data = dados['cliente']
                form.data.data = dados['data']
                form.tipo.data = dados['tipo']
    except Exception as ex:
        flash(str(ex), 'info')
    contexto['form'] = form
    return render_template('registro/form.html', **contexto), 200

def load_relacoes(dados, aux):
    req = aux['req']
    auth = aux['auth']
    headers = aux['headers']
    cliente_url = dados[u'_links'][u'cliente'][u'href']
    carro_url = dados[u'_links'][u'carro'][u'href']
    try:
        res = req.get( carro_url,auth=auth, headers=headers)
        dados['carro_instance'] = res.json()
    except:
        pass
    try:
        res = req.get( cliente_url,auth=auth, headers=headers)
        dados['cliente_instance'] = res.json()
    except:
        pass
    return dados

@registro_blueprint.route('/', methods = ['post', 'get'])
def index():
    contexto = {}
    endpoint = '/registro/'
    size = int(request.args.get('size','10'))
    page = int(request.args.get('page','0'))
    retorno = Api.listar(endpoint, page, size,callback=load_relacoes)
    contexto['size'] = size
    contexto['page'] = page
    contexto['endpoint'] = endpoint
    contexto['dados'] = retorno.dados
    contexto['pagination'] = retorno.pagination
    return render_template('registro/index.html', **contexto), 200

@registro_blueprint.route('/delete/<pk>', methods = ['post'])
def delete(pk):
    contexto = {}
    endpoint = '/registro/'
    retorno = Api.deletar(endpoint, pk)
    if retorno.operacao:
        return '',200
    return '', 404