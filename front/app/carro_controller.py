# -*- coding: utf-8 -*-

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

@carro_blueprint.route('/form', methods = ['post', 'get'])
def form():
    #set_trace()
    form = CarroForm()
    contexto = {}
    contexto['form'] = form
    try:
        if form.validate_on_submit():
            dados = criar_carro(form)
            res = req.post(
                api['host_api']+'/carro',
                data=json.dumps(dados,encoding='utf-8'),
                auth=(api['auth_api']),
                headers=api['headers_api']
                )
            if res.status_code == 200 or res.status_code == 201:
                contexto['mensagem_tipo'] = 'success'
                contexto['mensagem'] = u'Carro Cadastrado com sucesso'
            else:
                contexto['mensagem_tipo'] = 'danger'
                contexto['mensagem'] = res.text
    except Exception as ex:
        mensagem = str(ex)
    return render_template('carro/form.html', **contexto), 200