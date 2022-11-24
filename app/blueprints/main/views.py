from app.blueprints.main import main_bp

from flask import (
    render_template,
    abort
)

# from flask import current_app as app
# from flask_login import login_required, current_user

@main_bp.route("/", methods = ['GET'])
def landing_page():
    return "Hello world!"
