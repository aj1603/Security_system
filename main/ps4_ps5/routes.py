from flask import Blueprint, session, redirect, render_template
from main.models import Ps4_Ps5s
from main import db
from datetime import datetime
    
ps4_ps5s = Blueprint('ps4_ps5s', __name__)
nol = 0
e = datetime.now()

@ps4_ps5s.route('/first_time/<int:id>/')
def first_time(id):
    e = datetime.now()  
    try:
        games = Ps4_Ps5s.query.get_or_404(id)
        games.game_start_time = e
        games.game_stop_time = nol
        games.game_time = nol
        db.session.commit()
        return("Üstünlikli başlandy")
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
            print(d6, d7, d8)
            h_1 = int(d8[0])
            m_1 = int(d8[1])
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
                return("Üstünlikli tamamlandy")
            games.full_game_hours = hours
            games.full_game_minutes = minutes
            games.game_start_time = nol
            db.session.commit()
            return("Üstünlikli tamamlandy")
        except Exception as ex:
            print(f"error, couldn't make a request (connection issue) {ex}",200)
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)

  
