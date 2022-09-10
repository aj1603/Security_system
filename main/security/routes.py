from flask import render_template, request, Blueprint
from main.models import Admins, Ps4_Ps5s
from main import db

security = Blueprint('security', __name__)

@security.route('/game_con/')
def alo():
    
    return "sogran"
