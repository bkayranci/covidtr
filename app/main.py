"""
main.py
====================================
The core module of my example project
"""

from flask import Flask, make_response, jsonify
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

config = {
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=[
        '1 / 5 seconds',
        '40 / 5 minutes'
    ],
    default_limits_deduct_when=lambda response: response.status_code == 200 or response.status_code == 404
)

from app.controller import turkey_bp

app.register_blueprint(turkey_bp, url_prefix='/')


@app.errorhandler(429)
def ratelimit_handler(e):
    return make_response(
        jsonify(error="ratelimit exceeded %s" % e.description)
        , 429
    )
