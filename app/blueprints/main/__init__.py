from flask import Blueprint

from flask import Blueprint

# Blueprint configuration
main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

from app.blueprints.main import views
