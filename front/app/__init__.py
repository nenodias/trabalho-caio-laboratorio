# -*- coding: utf-8 -*-
from flask import Flask, request, render_template

app = Flask(__name__)

from app import controller