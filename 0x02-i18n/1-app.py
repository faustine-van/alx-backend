#!/usr/bin/env python3
"""configure available languages
   and keep track of the list of
   supported languages
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """intialize configuration
    """
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
babel.init_app(app, default_locale='en', default_timezone='UTC')


@app.route('/', strict_slashes=False)
def index():
    """set / route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
