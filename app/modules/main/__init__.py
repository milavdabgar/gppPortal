from flask import Blueprint
main = Blueprint('main', __name__, template_folder='templates')
from . import routes  # Import routes at the end to avoid circular dependencies