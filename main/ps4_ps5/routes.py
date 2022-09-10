from flask import Blueprint, session, redirect, render_template
from main.models import Ps4_Ps5s
from main import db
from datetime import datetime
    
ps4_ps5s = Blueprint('ps4_ps5s', __name__)
nol = 0
e = datetime.now()

@ps4_ps5s.route('/game_con/')
def game_con():
    game_cons = Ps4_Ps5s.query.all()
    return render_template("game.html", game_cons=game_cons)

@ps4_ps5s.route('/first_time/<int:id>/')
def first_time(id):
    e = datetime.now()  
    try:
        games = Ps4_Ps5s.query.get_or_404(id)
        games.game_start_time = e
        games.game_stop_time = nol
        games.game_time = nol
        games.play_price = nol
        db.session.commit()
        game_cons = Ps4_Ps5s.query.all()
        return render_template("game.html", game_cons=game_cons)
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)

@ps4_ps5s.route('/second_time/<int:id>/')
def second_time(id):
    e = datetime.now()
    try:
        games = Ps4_Ps5s.query.get_or_404(id)
        second_time = e
        d0 = games.game_start_time
        d1 = str(second_time)
        d2 = datetime.strptime(d0, "%Y-%m-%d %H:%M:%S.%f") #yr, mo, day, hr, min, sec
        d3 = datetime.strptime(d1, "%Y-%m-%d %H:%M:%S.%f")
        d4 = str(d3 - d2)
        games.game_time = d4
        games.game_stop_time = d3
        db.session.commit()
        try:
            games = Ps4_Ps5s.query.get_or_404(id)
            d5 = games.game_time
            d6 = games.full_game_hours
            d7 = games.full_game_minutes
            d8 = d5.split(':')
            h_1 = int(d8[0])
            m_1 = int(d8[1])
            money = ((h_1 * 60) + m_1)
            sony = games.id
            if sony == 1 or sony == 2:
                full_money = money * 0.583333333
                games.play_price = full_money
                db.session.commit()
            elif sony == 3 or sony == 4 or sony == 5 or sony == 6:
                full_money = money * 0.416666667
                games.play_price = full_money
                db.session.commit()
            elif sony == 7 or sony == 8 or sony == 9 or sony == 10:
                full_money = money * 0.333333333
                games.play_price = full_money
                db.session.commit()
            d4 = int(d6)
            d5 = int(d7)
            hours = (h_1 + d4)
            minutes = (m_1 + d5)
            if minutes >= 60:
                hours_full = hours + 1
                minutes_full = minutes - 60
                print(hours_full, minutes_full)
                games.full_game_hours = hours_full
                games.full_game_minutes = minutes_full
                db.session.commit()
                game_cons = Ps4_Ps5s.query.all()
                return render_template("game.html", game_cons=game_cons)
            games.full_game_hours = hours
            games.full_game_minutes = minutes
            games.game_start_time = nol
            db.session.commit()
            game_cons = Ps4_Ps5s.query.all()
            return render_template("game.html", game_cons=game_cons)
        except Exception as ex:
            print(f"error, couldn't make a request (connection issue) {ex}",200)
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)

  
@ps4_ps5s.route('/count_price/<int:id>/')
def count_price(id):
    try:
        games = Ps4_Ps5s.query.get_or_404(id)
        h_1 = int(games.full_game_hours)
        m_1 = int(games.full_game_minutes)
        sony_1 = games.id
        to_price = ((h_1*60) + m_1)
        if sony_1 == 1 or sony_1 == 2:
            today_money = to_price * 0.583333333
            games.today_income = today_money
            print ("VIP")
            db.session.commit()
        elif sony_1 == 3 or sony_1 == 4 or sony_1 == 5 or sony_1 == 6:
            today_money = to_price * 0.416666667
            games.today_income = today_money
            db.session.commit()
            print ("PS5")
        elif sony_1 == 7 or sony_1 == 8 or sony_1 == 9 or sony_1 == 10:
            today_money = to_price * 0.333333333
            games.today_income = today_money
            db.session.commit()
            print ("PS4")
        return "Hasaplandy"
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)