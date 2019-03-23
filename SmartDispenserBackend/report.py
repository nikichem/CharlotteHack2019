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

    # verify a machine exists
    db = get_db()
    machine_count = db.execute('SELECT COUNT(*) FROM machine WHERE id = ?', (id)).fetchall()

    if machine_count is None:
        error = 'machine with {0} number does not exist'.format(id)

    # display error if exists, else update
    if error is not None:
        flash(error)
    else:
        db.execute('UPDATE machine SET empty = ? WHERE id = ?', (status, id))
        count = db.execute('SELECT points FROM user WHERE userName = ?', ()).fetchone()
        db.execute('UPDATE user SET points = ? WHERE id = ?', (count+1,))
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

    # verify a machine exists
    db = get_db()
    machine_count = db.execute('SELECT COUNT(*) FROM machine WHERE id = ?', (id)).fetchall()

    if machine_count is None:
        error = 'machine with {0} number does not exist'.format(id)

    # display error if exists, else update
    if error is not None:
        flash(error)
    else:
        db.execute('UPDATE machine set missing = ? WHERE id = ?', (status, id))
        # TODO: update user's points
        db.commit()

    return 200

@bp.route('/getalldispenserlocations')
def get_all_dispenser_locations():

    db = get_db()
    db.execute('SELECT addresses FROM machine')
    addresses = db.fetchAll()

    return jsonify(addresses)
