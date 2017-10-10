from flask import Flask, render_template, url_for

import os

app = Flask(__name__)


# Routes
# These match the URL to a function that tells Flask what HTML to send back in render_template
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

@app.route('/events/code-camp')
def code_camp():
    return render_template('events/code-camp.html', bannerurl=url_for('static', filename='img/events/code-camp.jpg'), title='Code Camp')

@app.route('/events/creative-coding')
def creative_coding():
    return render_template('events/creative-coding.html', bannerurl=url_for('static', filename='img/events/creative-coding.jpg'), title='Creative Coding')

@app.route('/events/leadership-summit')
def leadership_summit():
    return render_template('events/summit.html', bannerurl=url_for('static', filename='img/events/leadership-summit.jpg'), title='Computer Science Diversity and Leadership Summit')

@app.route('/events/stem-expo')
def stem_expo():
    return render_template('events/expo.html', bannerurl=url_for('static', filename='img/events/stem-expo.jpg'), title='STEM Expo')

@app.route('/contact')
def contact_us():
    return render_template('contact.html', bannerurl=url_for('static', filename='img/TITANS-scenic.jpg'), title='Contact Us')


# this is the code that runs when a request is sent with a URL that doesn't match any routes
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', bannerurl=url_for('static', filename='img/ACMWBackground.png', title='Page Not Found')), 404

# this is to define a custom command line command to compile the SASS files in static/sass into plain old css in static/css
@app.cli.command('sass-compile')
def sass_compile():
    """you need to have sass installed to run this"""
    os.system('sass static/sass/gaia.scss static/css/gaia.css')
