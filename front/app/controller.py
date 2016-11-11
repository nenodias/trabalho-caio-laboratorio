# -*- coding: utf-8 -*-
from pdb import set_trace
from app import app, request, render_template, redirect, session, url_for, auth_require
from app.carro_controller import carro_blueprint
from app.cliente_controller import cliente_blueprint
from app.registro_controller import registro_blueprint

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        if email == 'admin@admin.com' and senha == '123':
            session['login'] = True
            return redirect(url_for('index'))
    return render_template('login.html'), 200


@app.route('/logout')
def logout():
    if 'login' in session:
        del session['login']
    return redirect(url_for('login'))

@app.route('/')
def index():
    return render_template('index.html'), 200

app.register_blueprint(carro_blueprint, url_prefix='/carro')
app.register_blueprint(cliente_blueprint, url_prefix='/cliente')
app.register_blueprint(registro_blueprint, url_prefix='/registro')