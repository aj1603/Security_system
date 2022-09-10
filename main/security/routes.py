from flask import render_template, request, Blueprint
from main.models import Admins, Ps4_Ps5s
from main import db

security = Blueprint('security', __name__)

@security.route('/game_con/')
def game_con():
    game_cons = Ps4_Ps5s.query.all()
    return render_template("game.html", game_cons=game_cons)
