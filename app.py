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
    return render_template('members.html', bannerurl=url_for('static', filename='img/staff/ACMW-group.jpg'), title='Board Members')

@app.route('/events')
def events_home():
    return render_template('events/index.html', bannerurl=url_for('static', filename='img/TITANS-scenic.jpg'), title='Events')

@app.route('/events/<event>')
def event_page(event):
    if event is 'code-camp':
        return render_template('events/code-camp.html', bannerurl=url_for('static', filename='img/events/code-camp.jpg'), title='Code Camp')
    elif event is 'creative-coding':
        return render_template('events/creative-coding.html', bannerurl=url_for('static', filename='img/events/creative-coding.jpg'), title='Creative Coding')
    elif event is 'leadership-summit':
        return render_template('events/leadership-summit.html', bannerurl=url_for('static', filename='img/events/leadership-summit.jpg'), title='Computer Science Diversity and Leadership Summit')
    elif event is 'stem-expo':
        return render_template('events/stem-expo.html', bannerurl=url_for('static', filename='img/events/stem-expo.jpg'), title='STEM Expo')
    else:
        return not_found('Page not found')


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', bannerurl=url_for('static', filename='img/ACMWBackground.png', title='Page Not Found')), 404

@app.route('/contact')
def contact_us():
    return render_template('contact.html')


@app.cli.command('sass-compile')
def sass_compile():
    """you need to have sass installed to run this"""
    os.system('sass static/sass/gaia.scss static/css/gaia.css')
