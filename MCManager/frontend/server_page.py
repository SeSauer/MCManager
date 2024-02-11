from flask import Blueprint, render_template
from MCManager.backend.Manager import manager
from MCManager.backend.ServerModel.ServerManager import ServerManager

bp = Blueprint('server_page', __name__)


@bp.route("/server/<server_name>")
def server_page(server_name):
    server: ServerManager = manager.get_server(server_name)
    return render_template("server_page.html.jinja", server=server)