from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session
from buzzdata import buzzer, data_for

webapp = Flask('__name__')

@webapp.route('/')
@check_logged_in
def indexpage():
    """ The home page for this webapp. Displays what the site is about/for.
    """

    return render_template("index.html",
                           title = "Portfolio of James Cantwell")
                           

@webapp.route('/games')
@check_logged_in
def goToGames():
    """ Sends the user to the Games Programming page.
    """
    
    return render_template("gamesProgramming.html",
                           title="Games Programming")

                           
@webapp.route('/3dsculptures')
@check_logged_in
def goToSculpting():
    """ Sends the user to the Games Programming page.
    """
    
    return render_template("sculptures.html",
                           title="3D Sculptures")
                           
@webapp.route('/contact')
@check_logged_in
def goToContact():
    """ Sends the user to the Games Programming page.
    """
    
    return render_template("contact.html",
                           title="Contact James")

@webapp.route('/about')
@check_logged_in
def goToSculpting():
    """ Sends the user to the Games Programming page.
    """
    
    return render_template("about.html",
                           title="About James")

if __name__ == '__main__':
    webapp.secret_key = b'..-.keysecretaisthis0101..-'
    webapp.run(debug=True, host='0.0.0.0')