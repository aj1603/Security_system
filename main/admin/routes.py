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


@admins.route('/first_time/<int:id>/')
def first_time(id):
    e = datetime.now()  
    try:
        games = Ps4_Ps5s.query.get_or_404(id)
        games.ps4_ps5_price = e
        db.session.commit()
        # ps4_ps5s = Ps4_Ps5s.query.all()
        # return render_template('boss.html', ps4_ps5s=ps4_ps5s)
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)

@admins.route('/second_time/<int:id>/')
def second_time(id):
    games = Ps4_Ps5s.query.get_or_404(id)
    print(games.ps4_ps5_price)
    second_time = e
    d0 = games.ps4_ps5_price
    d1 = str(second_time)
    d2 = datetime.strptime(d0, "%Y-%m-%d %H:%M:%S.%f") #yr, mo, day, hr, min, sec
    d3 = datetime.strptime(d1, "%Y-%m-%d %H:%M:%S.%f")
    print(d2)
    print(d3)
    print (d3 - d2)
    return render_template("boss.html")

# /change-language/tk
@admins.route('/change-language/<code>')
def change_language(code):
    session['language'] = code
    return redirect('/azyk_haryt/')
    #return {'language': session['language']}
