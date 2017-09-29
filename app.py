from flask import Flask, render_template, url_for

import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', bannerurl=url_for('static', filename='img/ACMWBackground.png'), title='About Us')

@app.route('/board')
def members():
    return render_template('members.html', bannerurl=url_for('static', filename='img/ACMWBackground.png'), title='Board Members')

@app.route('/events')
def events_home():
    return render_template('events/index.html', bannerurl=url_for('static', filename='img/TITANS-scenic.jpg'), title='Events')

@app.route('/events/code-camp')
def code_camp():
    return render_template('events/code-camp.html', bannerurl=url_for('static', filename='img/events/code-camp.jpg'), title='Code Camp')

@app.route('/contact')
def contact_us():
    return render_template('contact.html')


@app.cli.command('sass-compile')
def sass_compile():
    """you need to have sass installed to run this"""
    os.system('sass static/sass/gaia.scss static/css/gaia.css')
