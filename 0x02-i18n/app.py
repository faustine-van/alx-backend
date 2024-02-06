#!/usr/bin/env python3
"""configure available languages
   and keep track of the list of
   supported languages
"""
from typing import Dict
from datetime import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext, format_datetime
from pytz import timezone, UnknownTimeZoneError


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
    """Returns the locale from:
        - URL parameters
        - user settings
        - request header
        - Default locale
    """
    args = request.args
    user = getattr(g, 'user', None)
    if user is not None:
        # user's locale is not in the supported languages
        if user.get('locale') not in app.config['LANGUAGES']:
            return babel.default_locale  # set locale default
        return user.get('locale')
    elif 'locale' in args and args.get('locale') in app.config['LANGUAGES']:
        # checks if the locale is specified in the URL parameters (args)
        return args.get('locale')
    else:
        # try to guess the language based on the Accept-Language header
        # sent by the user's browser
        return request.accept_languages.best_match(app.config['LANGUAGES'])


# @babel.timezoneselector
def get_timezone():
    """get timezone from
        - Find timezone parameter in URL parameters
        - Find time zone from user settings
        - Default to UTC
    """
    try:
        args = request.args
        user = getattr(g, 'user', None)
        if user is not None:
            return timezone(user.get('timezone'))
        elif 'timezone' in args:
            return timezone(args.get('timezone'))
    except UnknownTimeZoneError:
        pass
    return babel.default_timezone


# Configure Babel to use the supported languages
babel.init_app(app, default_locale='en', default_timezone='UTC',
               locale_selector=get_locale, timezone_selector=get_timezone)

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


def to_user_timezone(datetime):
    tzinfo = get_timezone()
    return tzinfo.normalize(datetime.astimezone(tzinfo))


@app.route('/', strict_slashes=False)
def index():
    """set / routes"""
    title = gettext('home_title')
    say_hello = gettext('home_header')
    # get user name
    current_user = g.user
    if current_user is not None:
        user_name = current_user.get('name')
        logged_in_message = gettext('logged_in_as', username=user_name)
    else:
        user_name = None
        logged_in_message = None

    # get current time
    current_time_utc = datetime.utcnow()
    # Convert to user's timezone
    current_time_user_tz = to_user_timezone(current_time_utc)

    # Format the time
    formatted_time = current_time_user_tz.strftime("%d %b %Y à %H:%M:%S")
    current_time = gettext('current_time_is', current_time=formatted_time)
    return render_template('index.html',
                           title=title, say_hello=say_hello,
                           user_name=user_name,
                           logged_in_message=logged_in_message,
                           current_time=current_time)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
