# -*- coding: utf-8 -*-
# quiz-orm/views.py

from flask import Flask
from flask import render_template, request, redirect, url_for, abort, flash
from modele import *
from forms import *

app = Flask(__name__)

@app.route('/')
def index():
    """Strona główna"""
    return render_template('index.html')
    
@app.route('/lista')
def lista():
    return render_template('lista.html', query=pytania)
    
@app.route('/uczniowie')
def uczniowie():
    return render_template('uczniowie.html', query=pytania)


@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj():
    form = DodajForm()
    
    return render_template('dodaj.html', form=form)


