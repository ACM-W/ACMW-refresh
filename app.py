from flask import Flask, render_template

import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.cli.command('sass-compile')
def sass_compile():
    """you need to have sass installed to run this"""
    os.system('sass static/sass/gaia.scss static/css/gaia.css')
