from flask import render_template, request, Blueprint
from main.models import Admins

security = Blueprint('security', __name__)

@security.route('/jora/')
def jora():
    return 'Jora'
