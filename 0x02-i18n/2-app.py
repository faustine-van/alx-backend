#!/usr/bin/env python3
"""configure available languages
   and keep track of the list of
   supported languages
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """intialize configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


# Set up the locale selector as a decorator
@babel.localeselector
def get_locale():
    """Returns the locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """set / route"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
