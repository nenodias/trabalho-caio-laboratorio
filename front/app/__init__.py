# -*- coding: utf-8 -*-
import requests as req
from functools import wraps
from flask import (Flask, request, render_template, Blueprint, redirect,
 flash, url_for, jsonify, session)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'segredo'

api = {
    'host_api':'http://localhost:8000',
    'headers_api' : { 'Accept': 'application/json', 'Content-Type':'application/json'},
    'auth_api': ('admin', 'admin123')
}

def auth_require():
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not 'login' in session.keys():
                return redirect(url_for('login'))
            return f(*args, **kwargs)
        return wrapped
    return wrapper

from rest import Api
from app import controller