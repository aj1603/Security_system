from flask import Blueprint, session, redirect, render_template
from main.models import Ps4_Ps5s, Admins
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

@ps4_ps5s.route('/month_count_price/')
def month_count_price():
    try:
        boss_money = Admins.query.filter_by(id = 1).first()
        full_today_money = boss_money.today_income
        boss_money.last_month_income += full_today_money
        boss_money.today_income = nol
        db.session.commit()
        boss_report = Admins.query.all()
        return render_template("report_month.html", boss_report = boss_report)
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)


@ps4_ps5s.route('/full_count_price/')
def full_count_price():
    try:
        games_0 = Ps4_Ps5s.query.filter_by(id = 1).first()
        games_1 = Ps4_Ps5s.query.filter_by(id = 2).first()
        games_2 = Ps4_Ps5s.query.filter_by(id = 3).first()
        games_3 = Ps4_Ps5s.query.filter_by(id = 4).first()
        games_4 = Ps4_Ps5s.query.filter_by(id = 5).first()
        games_5 = Ps4_Ps5s.query.filter_by(id = 6).first()
        games_6 = Ps4_Ps5s.query.filter_by(id = 7).first()
        games_7 = Ps4_Ps5s.query.filter_by(id = 8).first()
        games_8 = Ps4_Ps5s.query.filter_by(id = 9).first()
        games_9 = Ps4_Ps5s.query.filter_by(id = 10).first()
        ps_1 = games_0.today_income
        ps_2 = games_1.today_income 
        ps_3 = games_2.today_income 
        ps_4 = games_3.today_income 
        ps_5 = games_4.today_income 
        ps_6 = games_5.today_income 
        ps_7 = games_6.today_income 
        ps_8 = games_7.today_income 
        ps_9 = games_8.today_income 
        ps_10 = games_9.today_income 
        full_today_money = (ps_1 + ps_2 + ps_3 + ps_4 + ps_5 + ps_6 + ps_7 + ps_8 + ps_9 + ps_10)
        boss_money = Admins.query.filter_by(id = 1).first()
        boss_money.today_income = full_today_money
        db.session.commit()
        boss_report = Admins.query.all()
        return render_template("report_today.html", boss_report = boss_report)
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)

