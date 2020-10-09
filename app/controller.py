from flask import jsonify, Blueprint
from app.service import ResultService

turkey_bp = Blueprint('turkey_bp', __name__,
                      template_folder='templates',
                      static_folder='static', static_url_path='assets')


@turkey_bp.route("/results")
def status():
    results = ResultService.results()
    if results:
        return jsonify(results)
    return jsonify(status=404)


@turkey_bp.route("/today")
def today():
    today = ResultService.today()
    if today:
        return jsonify(today)
    return jsonify(status=404)


@turkey_bp.route("/")
def last():
    last = ResultService.last()
    if last:
        return jsonify(last)
    return jsonify(status=404)

