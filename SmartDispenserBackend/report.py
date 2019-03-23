from flask import Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
from werkzeug.exceptions import abort
from SmartDispenserBackend.auth import login_required
from SmartDispenserBackend.db import get_db

bp = Blueprint('report', __name__)


@bp.route('/empty/<int:id>/<int:status>/', methods='POST')
@login_required
def empty(id, status):
    error = None

    # initial parameter checking
    if id is None or id < 0:
        error = 'id must be greater or equal to zero'
    elif status is None or status is not 0 or status is not 1:
        error = 'status must be either 0 or 1'

    # TODO: add authentication validation and check for machine existence

    if error is not None:
        flash(error)

    db = get_db()
    db.execute('UPDATE machine SET empty = ? WHERE id = ?', (status, id))
    # TODO: update user's points
    db.commit()

    return 200


@bp.route('/missing/<int:id>/<int:status>/', methods='POST')
@login_required
def missing(id, status):
    error = None

    # initial parameter checking
    if id is None or id < 0:
        error = 'id must be greater or equal to zero'
    elif status is None or status is not 0 or status is not 1:
        error = 'status must be either 0 or 1'

    # TODO: add authentication validation and check for machine existence

    if error is not None:
        flash(error)

    db = get_db()
    db.execute('UPDATE machine set missing = ? WHERE id = ?', (status, id))
    db.commit()

    return 200

@bp.route('/getalldispenserlocations')
def get_all_dispenser_locations():

    db = get_db()
    db.execute('SELECT addresses FROM machine')
    addresses = db.fetchAll()

    return jsonify(addresses)
