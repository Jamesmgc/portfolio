from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session
webapp = Flask('__name__')

@webapp.route('/')
def indexpage():
    """ The home page for this webapp. Displays what the site is about/for.
    """

    return render_template("index.html",
                           title = "Portfolio of James Cantwell")
                           

@webapp.route('/games')
def goToGames():
    """ Sends the user to the Games Programming page.
    """
    
    return render_template("gamesProgramming.html",
                           title="Games Programming")

                           
@webapp.route('/3dsculptures')
def goToSculpting():
    """ Sends the user to the Games Programming page.
    """
    
    return render_template("sculptures.html",
                           title="3D Sculptures")
                           
@webapp.route('/contact')
def goToContact():
    """ Sends the user to the Games Programming page.
    """
    
    return render_template("contact.html",
                           title="Contact James")

@webapp.route('/about')
def goToAbout():
    """ Sends the user to the Games Programming page.
    """
    
    return render_template("about.html",
                           title="About James")

if __name__ == '__main__':
    webapp.secret_key = b'..-.keysecretaisthis0101..-'
    webapp.run(debug=True, host='0.0.0.0')