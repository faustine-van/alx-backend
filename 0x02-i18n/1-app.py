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
    """set / routes"""
    title = 'Welcome to Holberton'
    say_hello = 'Hello world'
    return render_template('1-index.html', title=title, say_hello=say_hello)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
