from flask import Blueprint, session, redirect, render_template
from main.models import Ps4_Ps5s
from main import db
from datetime import datetime,timedelta
    
admins = Blueprint('admins', __name__)

e = datetime.now()


@admins.route('/home/')
def home():
    return '///////////////////////////////'

@admins.route('/all_ps4_ps5/')
def all_ps4_ps5():
    ps4_ps5s = Ps4_Ps5s.query.all()
    return render_template("boss.html", ps4_ps5s=ps4_ps5s)

# /change-language/tk
@admins.route('/change-language/<code>')
def change_language(code):
    session['language'] = code
    return redirect('/azyk_haryt/')
    #return {'language': session['language']}
