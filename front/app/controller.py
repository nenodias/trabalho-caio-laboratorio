# -*- coding: utf-8 -*-
from app import app, request, render_template

@app.route('/')
def index():
    return render_template('index.html'), 200