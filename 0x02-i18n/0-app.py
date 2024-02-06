#!/usr/bin/env python3
"""setup a basic Flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """set / route"""
    title = 'Welcome to Holberton'
    say_hello = 'Hello world'
    return render_template('0-index.html', title=title, say_hello=say_hello)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
