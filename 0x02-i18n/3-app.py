#!/usr/bin/env python3
"""configure available languages
   and keep track of the list of
   supported languages
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config():
    """intialize configuration
    """
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
# load configuration from Config
app.config.from_object(Config)
babel = Babel(app)


# Set up the locale selector as a decorator
def get_locale():
    """Returns the locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Configure Babel to use the supported languages
babel.init_app(app, default_locale='en', default_timezone='UTC',
               locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index():
    """set / routes"""
    title = gettext('home_title')
    say_hello = gettext('home_header')
    return render_template('3-index.html', title=title, say_hello=say_hello)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
