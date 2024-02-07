#!/usr/bin/env python3
"""configure available languages
   and keep track of the list of
   supported languages
"""
from typing import Dict
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config:
    """intialize configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Returns the locale
    """
    args = request.args
    if 'locale' in args and args.get('locale') in app.config['LANGUAGES']:
        return args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Dict:
    """returns a user dictionary
       or None if the ID cannot be found
    """
    login_as = request.args.get('login_as')
    if login_as is None:
        return None
    user_id = int(login_as)
    return users.get(user_id)


@app.before_request
def before_request():
    """used as decorator to make it be executed
        before all other functions
    """
    g.user = get_user()


@app.route('/', strict_slashes=False)
def index():
    """set / routes"""

    current_user = g.user
    if current_user is not None:
        user_name = current_user.get('name')
        logged_in_message = gettext('logged_in_as', username=user_name)
    else:
        user_name = None
        logged_in_message = None

    return render_template('5-index.html',
                           user_name=user_name,
                           logged_in_message=logged_in_message)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
