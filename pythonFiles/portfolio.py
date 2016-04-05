from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask('__name__')

@app.route('/')
def indexpage():
    """ The home page for this webapp. Displays what the site is about/for.
    """

    return render_template(".../html/index.html",
                           title = "Portfolio of James Cantwell")
                           

@app.route('/games')
def goToGames():
    """ Sends the user to the Games Programming page.
    """
    
    return render_template(".../html/gamesProgramming.html",
                           title="Games Programming")

                           
@app.route('/3dsculptures')
def goToSculpting():
    """ Sends the user to the Games Programming page.
    """
    
    return render_template(".../html/sculptures.html",
                           title="3D Sculptures")
                           
@app.route('/contact')
def goToContact():
    """ Sends the user to the Games Programming page.
    """
    
    return render_template(".../html/contact.html",
                           title="Contact James")

@app.route('/about')
def goToAbout():
    """ Sends the user to the Games Programming page.
    """
    
    return render_template(".../html/about.html",
                           title="About James")

if __name__ == '__main__':
    app.secret_key = b'..-.keysecretaisthis0101..-'
    app.run(debug=True, host='0.0.0.0')