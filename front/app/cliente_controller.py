# -*- coding: utf-8 -*-
import json
from pdb import set_trace
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange, Length
from app import app, request, redirect, flash, url_for, render_template, Blueprint, Api, jsonify, auth_require

cliente_blueprint = Blueprint('cliente', __name__)

class ClienteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    rg = IntegerField('RG', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[Length(min=8, max=18)])
    rua = StringField('Rua', validators=[DataRequired()])
    numero = StringField(u'Número', validators=[DataRequired()])
    bairro = StringField('Bairro', validators=[DataRequired()])
    cidade = StringField('Cidade', validators=[DataRequired()])

    def criar_cliente(self):
        return {
            'nome': self.nome.data,
            'email': self.email.data,
            'rg': int(self.rg.data),
            'telefone': self.telefone.data,
            'endereco':{
                'rua': self.rua.data,
                'numero': self.numero.data,
                'bairro': self.bairro.data,
                'cidade': self.cidade.data
            }
        }

def retornar_cliente(dados):
    return {
        'nome':dados['nome'],
        'email':dados['email'],
        'rg':dados['rg'],
        'telefone':dados['telefone'],
        'rua':dados['endereco']['rua'],
        'numero':dados['endereco']['numero'],
        'bairro':dados['endereco']['bairro'],
        'cidade':dados['endereco']['cidade']
    }

@cliente_blueprint.route('/form/', defaults={'pk':None}, methods = ['post', 'get'])
@cliente_blueprint.route('/form/<pk>', methods = ['post', 'get'])
@auth_require()
def form(pk):
    #set_trace()
    form = ClienteForm()
    contexto = {}
    try:
        endpoint = '/cliente/'
        retorno = False
        if pk:
            endpoint += pk
        if form.validate_on_submit():
            dados = form.criar_cliente()
            if pk and pk in endpoint:
                '''Atualizando'''
                retorno = Api.atualizar(endpoint, dados)
                flash(u'Cliente com código %s foi salvo com sucesso'%(retorno.pk), 'success')
            else:
                '''Salvando'''
                retorno = Api.salvar(endpoint, dados)
                flash(u'Cliente com código %s foi atualizado com sucesso'%(retorno.pk), 'success')
            if retorno:
                return redirect(url_for('cliente.form', pk=retorno.pk))
            else:
                '''Erro'''
                flash(retorno.text, 'danger')
        elif pk:
            '''Editar'''
            retorno = Api.buscar(endpoint)
            if retorno:
                dados = retornar_cliente(retorno.dados)
                form = ClienteForm(**dados)
    except Exception as ex:
        flash(str(ex), 'info')
    contexto['form'] = form
    return render_template('cliente/form.html', **contexto), 200

@cliente_blueprint.route('/', methods = ['post', 'get'])
@auth_require()
def index():
    contexto = {}
    endpoint = '/cliente/'
    size = int(request.args.get('size','10'))
    page = int(request.args.get('page','0'))
    retorno = Api.listar(endpoint, page, size)
    contexto['size'] = size
    contexto['page'] = page
    contexto['endpoint'] = endpoint
    contexto['dados'] = retorno.dados
    contexto['pagination'] = retorno.pagination
    return render_template('cliente/index.html', **contexto), 200

@cliente_blueprint.route('/delete/<pk>', methods = ['post'])
@auth_require()
def delete(pk):
    contexto = {}
    endpoint = '/cliente/'
    retorno = Api.deletar(endpoint, pk)
    if retorno.operacao:
        return '',200
    return '', 404


@cliente_blueprint.route('/ajax', methods = ['get'])
@auth_require()
def ajax():
    search = request.args.get('search', '')
    limit = request.args.get('limit','10')
    offset = request.args.get('offset','0')
    param = '?nome='+search+'&size='+limit+'&page='+offset
    url = '/cliente/search/findByNomeContainsIgnoreCase'
    return jsonify(Api.listar(url,param=param).dados )

@cliente_blueprint.route('/ajax/<pk>', methods = ['get'])
@auth_require()
def ajax_by_id(pk):
    endpoint = '/cliente/'+pk
    return jsonify(Api.buscar(endpoint).dados )