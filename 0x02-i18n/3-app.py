#!/usr/bin/env python3
"""Babel
"""
from flask import Flask
from flask import render_template, request
from flask_babel import Babel


class Config:
    """
    create a Config class that has a LANGUAGES
    class attribute equal to ["en", "fr"].
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    determine the best match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home() -> str:
    """
    a single / route and an index.html template that
    simply outputs “Welcome to Holberton” as page
    title (<title>) and “Hello world” as header (<h1>).
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
