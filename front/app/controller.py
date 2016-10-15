# -*- coding: utf-8 -*-
from app import app, request, render_template
from app.carro_controller import carro_blueprint
from app.cliente_controller import cliente_blueprint
from app.registro_controller import registro_blueprint


@app.route('/')
def index():
    return render_template('index.html'), 200

app.register_blueprint(carro_blueprint, url_prefix='/carro')
app.register_blueprint(cliente_blueprint, url_prefix='/cliente')
app.register_blueprint(registro_blueprint, url_prefix='/registro')