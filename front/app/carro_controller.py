# -*- coding: utf-8 -*-
from pdb import set_trace
import json
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange, Length
from app import app, request, redirect, flash, url_for, render_template, Blueprint, Api, jsonify, auth_require

carro_blueprint = Blueprint('carro', __name__)

class CarroForm(FlaskForm):
    placa = StringField('Placa', validators=[DataRequired(), Length(min=8, max=10)])
    marca = StringField('Marca', validators=[DataRequired()])
    modelo = StringField('Modelo', validators=[DataRequired()])
    ano = IntegerField('Ano', validators=[DataRequired()])
    cor = StringField('Cor')
    
    def criar_carro(self):
        return {
            'placa': self.placa.data,
            'marca': self.marca.data,
            'modelo': self.modelo.data,
            'ano': self.ano.data,
            'cor': self.cor.data,
        }



@carro_blueprint.route('/form/', defaults={'pk':None}, methods = ['post', 'get'])
@carro_blueprint.route('/form/<pk>', methods = ['post', 'get'])
@auth_require()
def form(pk):
    #set_trace()
    form = CarroForm()
    contexto = {}
    try:
        endpoint = '/carro/'
        retorno = False
        if pk:
            endpoint += pk
        if form.validate_on_submit():
            dados = form.criar_carro()
            if pk and pk in endpoint:
                '''Atualizando'''
                retorno = Api.atualizar(endpoint, dados)
                flash(u'Carro com código %s foi salvo com sucesso'%(retorno.pk), 'success')
            else:
                '''Salvando'''
                retorno = Api.salvar(endpoint, dados)
                flash(u'Carro com código %s foi atualizado com sucesso'%(retorno.pk), 'success')
            if retorno:
                return redirect(url_for('carro/carro.form', pk=retorno.pk))
            else:
                '''Erro'''
                flash(retorno.text, 'danger')
        elif pk:
            '''Editar'''
            retorno = Api.buscar(endpoint)
            if retorno:
                conjunto_campos = set([u'placa', u'marca', u'modelo', u'ano',u'cor'])
                dados = {chave.encode('ascii','ignore'):valor for chave,valor in retorno.dados.iteritems() if chave in conjunto_campos }
                form = CarroForm(**dados)
    except Exception as ex:
        flash(str(ex), 'info')
    contexto['form'] = form
    return render_template('carro/form.html', **contexto), 200


@carro_blueprint.route('/', methods = ['post', 'get'])
@auth_require()
def index():
    contexto = {}
    endpoint = '/carro/'
    size = int(request.args.get('size','10'))
    page = int(request.args.get('page','0'))
    retorno = Api.listar(endpoint, page, size)
    contexto['size'] = size
    contexto['page'] = page
    contexto['endpoint'] = endpoint
    contexto['dados'] = retorno.dados
    contexto['pagination'] = retorno.pagination
    return render_template('carro/index.html', **contexto), 200

@carro_blueprint.route('/delete/<pk>', methods = ['post'])
@auth_require()
def delete(pk):
    contexto = {}
    endpoint = '/carro/'
    retorno = Api.deletar(endpoint, pk)
    if retorno.operacao:
        return '',200
    return '', 404

@carro_blueprint.route('/ajax', methods = ['get'])
@auth_require()
def ajax():
    search = request.args.get('search', '')
    limit = request.args.get('limit','10')
    offset = request.args.get('offset','0')
    param = '?modelo='+search+'&marca='+search+'&size='+limit+'&page='+offset
    url = '/carro/search/findByModeloContainsIgnoreCaseOrMarcaContainsIgnoreCase'
    retorno = Api.listar(url,param=param)
    return jsonify(retorno.dados )

@carro_blueprint.route('/ajax/<pk>', methods = ['get'])
@auth_require()
def ajax_by_id(pk):
    endpoint = '/carro/'+pk
    return jsonify(Api.buscar(endpoint).dados )