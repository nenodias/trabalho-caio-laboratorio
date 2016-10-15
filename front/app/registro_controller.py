# -*- coding: utf-8 -*-
import json
from pdb import set_trace
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, NumberRange, Length
from app import app, request, redirect, render_template, Blueprint, req, api

registro_blueprint = Blueprint('registro', __name__, template_folder='templates')

class RegistroForm(FlaskForm):
    carro = IntegerField('Carro', validators=[DataRequired()])
    cliente = IntegerField('Cliente', validators=[DataRequired()])
    data = DateField('Data', validators=[DataRequired()])
    tipo = SelectField('Tipo Registro', validators=[DataRequired()],choices=[('ENTRADA','Entrada'),('SAIDA',u'Saída')])
    

def criar_registro(form):
    return {
        'carro': {
            'id':form.carro.data
        },
        'cliente': {
            'id':form.cliente.data
        },
        'data': datetime.strftime(form.data.data, '%Y-%m-%d %H:%M:%S'),
        'tipo': form.tipo.data,
    }

@registro_blueprint.route('/form', methods = ['post', 'get'])
def form():
    #set_trace()
    form = RegistroForm()
    contexto = {}
    contexto['form'] = form
    try:
        set_trace()
        if form.validate_on_submit():
            dados = criar_registro(form)
            res = req.post(
                api['host_api']+'/registro',
                data=json.dumps(dados,encoding='utf-8'),
                auth=(api['auth_api']),
                headers=api['headers_api']
                )
            if res.status_code == 200 or res.status_code == 201:
                contexto['mensagem_tipo'] = 'success'
                contexto['mensagem'] = u'Registro Cadastrado com sucesso'
            else:
                contexto['mensagem_tipo'] = 'danger'
                contexto['mensagem'] = res.text
    except Exception as ex:
        mensagem = str(ex)
    return render_template('registro/form.html', **contexto), 200