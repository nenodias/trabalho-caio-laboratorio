# -*- coding: utf-8 -*-
import requests as req
from flask import Flask, request, render_template, Blueprint, redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = 'segredo'

api = {
    'host_api':'http://localhost:8000',
    'headers_api' : { 'Accept': 'application/json', 'Content-Type':'application/json'},
    'auth_api': ('admin', 'admin123')
}

from app import controller