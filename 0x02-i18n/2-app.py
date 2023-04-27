#!/usr/bin/env python3
"""
Basic Babel Setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Flask Babel Configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get locale from user"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def render_index():
    """renders 2-index.html"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
