# -*- coding: utf-8 -*-
from pdb import set_trace
import json
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange, Length
from app import app, request, redirect, render_template, Blueprint, req, api

carro_blueprint = Blueprint('carro', __name__, template_folder='templates/carro')

class CarroForm(FlaskForm):
    placa = StringField('Placa', validators=[DataRequired(), Length(min=8, max=10)])
    marca = StringField('Marca', validators=[DataRequired()])
    modelo = StringField('Modelo', validators=[DataRequired()])
    ano = IntegerField('Ano', validators=[DataRequired()])
    cor = StringField('Cor')
    
def criar_carro(form):
    return {
        'placa': form.placa.data,
        'marca': form.marca.data,
        'modelo': form.modelo.data,
        'ano': form.ano.data,
        'cor': form.cor.data,
    }


def salvar(endpoint, dados):
    res = req.post(
        api['host_api']+endpoint,
        data=json.dumps(dados,encoding='utf-8'),
        auth=(api['auth_api']),
        headers=api['headers_api']
        )
    return res.status_code == 200 or res.status_code == 201

def atualizar(endpoint, dados):
    res = req.put(
        api['host_api']+endpoint,
        data=json.dumps(dados,encoding='utf-8'),
        auth=(api['auth_api']),
        headers=api['headers_api']
        )
    return res.status_code == 200 or res.status_code == 201

def buscar(endpoint):
    res = req.get(
                api['host_api']+endpoint,
                auth=(api['auth_api']),
                headers=api['headers_api']
                )
    dados = None
    if res.status_code != 404:
        retorno = res.json()
        conjunto_campos = set([u'placa', u'marca', u'modelo', u'ano',u'cor'])
        dados = {chave.encode('ascii','ignore'):valor for chave,valor in retorno.iteritems() if chave in conjunto_campos }
    return dados



@carro_blueprint.route('/form/', defaults={'pk':None}, methods = ['post', 'get'])
@carro_blueprint.route('/form/<pk>', methods = ['post', 'get'])
def form(pk):
    #set_trace()
    form = CarroForm()
    contexto = {}
    try:
        endpoint = '/carro/'
        if pk:
            endpoint += pk
        if form.validate_on_submit():
            dados = criar_carro(form)
            operacao = False
            if pk and pk in endpoint:
                operacao = atualizar(endpoint, dados)
            else:
                operacao = salvar(endpoint, dados)
            if operacao:
                contexto['mensagem_tipo'] = 'success'
                contexto['mensagem'] = u'Carro Cadastrado com sucesso'
            else:
                contexto['mensagem_tipo'] = 'danger'
                contexto['mensagem'] = res.text
        elif pk:
            dados = buscar(endpoint)
            if dados:
                form = CarroForm(**dados)
    except Exception as ex:
        mensagem = str(ex)
    contexto['form'] = form
    return render_template('carro/form.html', **contexto), 200