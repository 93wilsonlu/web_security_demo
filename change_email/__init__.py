from flask import Blueprint

change_email = Blueprint('change_email', __name__)

from . import view