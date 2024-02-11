from flask import Blueprint, render_template
from MCManager.backend.Manager import manager

bp = Blueprint('overview', __name__)


@bp.route("/overview")
def landing_page():
    return render_template("overview.html.jinja", servers=manager.server_collection.servers)