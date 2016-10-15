# -*- coding: utf-8 -*-
import json
from pdb import set_trace
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange, Length
from app import app, request, redirect, render_template, Blueprint, req, api

cliente_blueprint = Blueprint('cliente', __name__, template_folder='templates')

class ClienteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    rg = IntegerField('RG', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[Length(min=8, max=18)])
    rua = StringField('Rua', validators=[DataRequired()])
    numero = StringField(u'Número', validators=[DataRequired()])
    bairro = StringField('Bairro', validators=[DataRequired()])
    cidade = StringField('Cidade', validators=[DataRequired()])

def criar_cliente(form):
    return {
        'nome': form.nome.data,
        'email': form.email.data,
        'rg': int(form.rg.data),
        'telefone': form.telefone.data,
        'endereco':{
            'rua': form.rua.data,
            'numero': form.numero.data,
            'bairro': form.bairro.data,
            'cidade': form.cidade.data
        }
    }

@cliente_blueprint.route('/form', methods = ['post', 'get'])
def form():
    #set_trace()
    form = ClienteForm()
    contexto = {}
    contexto['form'] = form
    try:
        if form.validate_on_submit():
            dados = criar_cliente(form)
            res = req.post(
                api['host_api']+'/cliente',
                data=json.dumps(dados,encoding='utf-8'),
                auth=(api['auth_api']),
                headers=api['headers_api']
                )
            if res.status_code == 200 or res.status_code == 201:
                contexto['mensagem_tipo'] = 'success'
                contexto['mensagem'] = u'Cliente Cadastrado com sucesso'
            else:
                contexto['mensagem_tipo'] = 'danger'
                contexto['mensagem'] = res.text
    except Exception as ex:
        mensagem = str(ex)
    return render_template('cliente/form.html', **contexto), 200