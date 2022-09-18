from distutils.sysconfig import get_makefile_filename
from flask import Blueprint, session, redirect, render_template, flash, make_response, request, url_for
import requests
from sqlalchemy import null
from main.models import Station, Client, Admin, Day, Month, Node
from main import db
from datetime import datetime, timedelta
from .forms import ClientForm, ClientUpdateForm, GameForm, GameUpdateForm, LoginForm, DisCountForm, BuyForm
from flask_login import (
	login_required,
	login_user,
	current_user,
	logout_user,
)
admins = Blueprint('admins', __name__)
e = datetime.now()
nol = 0


@admins.route('/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    # if request.method == 'GET':
    #     if current_user.is_authenticated:
    #         if current_user.isPatron == 1:
    #             return redirect("/admin")
    #     return render_template ("admin/login.html")

    if request.method == 'POST':
        phoneNumber = request.form.get("phone")
        password = request.form.get("password")
        print(phoneNumber, password)
        try:
            user = Admin.query.filter_by(phoneNumber = phoneNumber).first()
            if user:
                
                if(user and user.password==password):
                    login_user(user)
                    next_page = request.args.get('next')
                    if user.isPatron == 1:
                        
                        return redirect(next_page) if next_page else redirect("/all_ps4_ps5/")
                    else:
                        return redirect(next_page) if next_page else redirect("/game_con/")
                else:
                    raise Exception
            else:
                raise Exception				
        except Exception as ex:
            flash(f'Giriş amala aşyrylmady, telefon belgi ya-da açarsöz ýalnyş!','danger')
            print(ex)
    return render_template ("login.html", form = form)


@admins.route("/logout/")
def logout():
	logout_user()
	return redirect(url_for("login"))


@admins.route('/admin/for_logo/')
def for_logo():
    return render_template("index.html")

@admins.route('/all_ps4_ps5/')
@login_required
def all_ps4_ps5():
    if current_user.isPatron != 1:
        return redirect('/game_con/')
    game_cons = Station.query.all()
    return render_template("boss.html", game_cons=game_cons)


@admins.route('/game_con/')
def game_con():
    game_cons = Station.query.all()
    return render_template("game.html", game_cons=game_cons)

@admins.route('/game_con/first_time/<int:id>/')
def first_time(id):
    e = datetime.now()
    try:
        games = Station.query.get_or_404(id)
        nodes = Node.query.filter_by(id = games.id).first()
        if games.startTime is not None:
            game_cons = Station.query.all()
            return render_template("game.html", game_cons=game_cons)            
        games.startTime = e
        nodes.state = 1
        games.endTime = None
        games.playInterval = None
        games.playPrice = nol
        db.session.commit() 
        controlIp = nodes.ip
        deviceState = nodes.state
        try:
            requests.get("http://{}/control/?command={}".format(controlIp, deviceState))
            game_cons = Station.query.all()
            return render_template("game.html", game_cons=game_cons)
        except Exception as ex:
            return 'Error'

    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)

@admins.route('/second_time/<int:id>/')
def second_time(id):
    e = datetime.now()
    try:
        games = Station.query.get_or_404(id)
        nodes = Node.query.filter_by(id = games.id).first()
        day = Day.query.filter_by(stationId=games.id).first()
        month = Month.query.filter_by(stationId=games.id).first()
        if games.endTime is not None:
            game_cons = Station.query.all()
            return render_template("game.html", game_cons=game_cons)
        endTime = e
        d0 = str(games.startTime)
        d1 = str(endTime)
        d2 = datetime.strptime(d0, "%Y-%m-%d %H:%M:%S.%f") #yr, mo, day, hr, min, sec
        d3 = datetime.strptime(d1, "%Y-%m-%d %H:%M:%S.%f")
        d4 = str(d3 - d2)
        hours = int(d4.split(':')[0])
        minutes = int(d4.split(':')[1])
        interval = hours * 60 + minutes
        games.playInterval = interval
        day.playedTime += interval
        month.playedTime += interval
        games.endTime = d3
        nodes.state = 0
        games.startTime = None
        db.session.commit()
        print("alo")
        try:
            games = Station.query.get_or_404(id)
            day = Day.query.filter_by(stationId=games.id).first()
            month = Month.query.filter_by(stationId=games.id).first()
            d6 = games.discount
            if d6 == 0:
                print("alo")
                money = games.playInterval
                idStation = games.id
                if idStation == 1 or idStation == 2:
                    full_money = money * 0.583333333
                    print(full_money)
                    games.playPrice += full_money
                    day.playedPrice += full_money
                    month.playedPrice += full_money
                    db.session.commit()
                elif idStation == 3 or idStation == 4:
                    full_money = money * 0.416666667
                    games.playPrice += full_money
                    day.playedPrice += full_money
                    month.playedPrice += full_money
                    db.session.commit()
                elif idStation == 5 or idStation == 6 or idStation == 7 or idStation == 8 or idStation == 9 or idStation == 10:
                    full_money = money * 0.333333333                  
                    games.playPrice += full_money
                    day.playedPrice += full_money
                    month.playedPrice += full_money
                    db.session.commit()
                game_cons = Station.query.all()
                return render_template("game.html", game_cons=game_cons)
            if d6 > 0:
                print("alo")
                money = games.playInterval
                idStation = games.id
                if idStation == 1 or idStation == 2:
                    full_money = money * 0.583333333
                    fullMoney = full_money - ((full_money * d6)/100)
                    games.playPrice += fullMoney
                    day.playedPrice += fullMoney
                    month.playedPrice += full_money
                    db.session.commit()
                elif idStation == 3 or idStation == 4:
                    full_money = money * 0.416666667
                    fullMoney = full_money - ((full_money * d6)/100)
                    games.playPrice += fullMoney
                    day.playedPrice += fullMoney
                    month.playedPrice += full_money
                    db.session.commit()
                elif idStation == 5 or idStation == 6 or idStation == 7 or idStation == 8 or idStation == 9 or idStation == 10:
                    full_money = money * 0.333333333
                    fullMoney = full_money - ((full_money * d6)/100)                    
                    games.playPrice += fullMoney
                    day.playedPrice += fullMoney
                    month.playedPrice += full_money
                    db.session.commit()
                controlIp = nodes.ip
                deviceState = nodes.state
                try:
                    requests.get("http://{}/control/?command={}".format(controlIp, deviceState))
                    game_cons = Station.query.all()
                    return render_template("game.html", game_cons=game_cons)
                except Exception as ex:
                    return 'Error'
        except Exception as ex:
            print(f"error, couldn't make a request (connection issue) {ex}",200)
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)

# Buy
@admins.route("/buy_something/<int:id>/", methods=["GET", "POST"])
def buy_something(id):
    buy = Station.query.get_or_404(id)
    dayBuy = Day.query.get_or_404(id)
    monthBuy = Month.query.get_or_404(id)
    form = BuyForm()	
    if form.validate_on_submit():
        buy.playPrice += float(form.buy_something.data)
        dayBuy.playedPrice += float(form.buy_something.data)
        monthBuy.playedPrice += float(form.buy_something.data)
        db.session.commit()
        game_cons = Station.query.all()
        return render_template("game.html", game_cons=game_cons)
    elif request.method == 'GET':
        form.buy_something.data = buy.playPrice
        return render_template("buy_something.html", form=form)
# Buy

# Discount
@admins.route('/update_discount/<int:id>/', methods=['GET', 'POST'])
def update_discount(id):
    disCount = Station.query.get_or_404(id)
    form = DisCountForm()
    print("hello")
    if form.validate_on_submit():
        disCount.discount = form.today_sale.data
        db.session.commit()
        game_cons = Station.query.all()
        return render_template("game.html", game_cons=game_cons)
    elif request.method == 'GET':
        form.today_sale.data = disCount.discount
        return render_template("discount.html", form=form)

# Discount


# Day Report
@admins.route('/dayReport/')
@login_required
def dayReport():
    if current_user.isPatron != 1:
        return redirect('/game_con/')
    try:
        totalSum = 0
        days = Day.query.all()
        for day in days:
            totalSum += day.playedPrice
        return render_template("dayReport.html", days=days, totalSum = totalSum)
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)

@admins.route('/deleteDay/')
@login_required
def deleteDay():
    if current_user.isPatron != 1:
        return redirect('/game_con/')
    try:
        dayDelete = Day.query.all()
        for day in dayDelete:
            day.playedTime = 0.0
            day.playedPrice = 0
            db.session.commit()
        game_cons = Day.query.all()
        return render_template("dayReport.html", game_cons=game_cons)
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)

# ////Day Report

# Month Report
@admins.route('/monthReport/')
@login_required
def monthReport():
    if current_user.isPatron != 1:
        return redirect('/game_con/')
    try:
        totalMoon = 0
        months = Month.query.all()
        for month in months:
            totalMoon += month.playedPrice
        return render_template("monthReport.html", months=months, totalMoon = totalMoon)
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)


@admins.route('/deleteMonth/')
@login_required
def deleteMonth():
    if current_user.isPatron != 1:
        return redirect('/game_con/')
    try:
        monthDelete = Month.query.all()
        for month in monthDelete:
            month.playedTime = 0.0
            month.playedPrice = 0
            db.session.commit()
        game_cons = Month.query.all()
        return render_template("monthReport.html", game_cons=game_cons)
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)

@admins.route('/month_count_price/')
def month_count_price():
    try:
        boss_money = Admin.query.filter_by(id = 1).first()
        full_today_money = boss_money.today_income
        boss_money.last_month_income += full_today_money
        boss_money.today_income = nol
        db.session.commit()
        boss_report = Admin.query.all()
        return render_template("report_month.html", boss_report = boss_report)
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)
# ///Month Report

# Client
@admins.route('/client/<int:id>/delete/', methods=['GET', 'POST'])
def delete_client(id):
    delete_client = Station.query.get_or_404(id)
    db.session.delete(delete_client)
    db.session.commit()
    our_clients = Station.query.all()
    return render_template("client.html", our_clients=our_clients)


@admins.route('/client/<int:id>/update/', methods=['GET', 'POST'])
def update_client(id):
    clients = Station.query.get_or_404(id)
    form = ClientUpdateForm()
    if form.validate_on_submit():
        clients.name = form.name.data
        clients.surname = form.surname.data
        clients.username = form.username.data
        clients.password = form.password.data
        clients.phone_number = form.phone_number.data
        clients.secret_key = form.secret_key.data
        clients.play_time = form.play_time.data
        clients.playPrice = form.playPrice.data
        clients.play_sale = form.play_sale.data
        clients.full_play_time = form.full_play_time.data
        db.session.commit()
        our_clients = Station.query.all()
        return render_template("client.html", our_clients=our_clients)
    elif request.method == 'GET':
        form.name.data = clients.name
        form.surname.data = clients.surname
        form.username.data = clients.username
        form.password.data = clients.password
        form.phone_number.data = clients.phone_number
        form.secret_key.data = clients.secret_key
        form.play_time.data = clients.play_time
        form.playPrice.data = clients.playPrice
        form.play_sale.data = clients.play_sale
        form.full_play_time.data = clients.full_play_time

        return render_template("edit_client.html", form=form)

@admins.route('/add_clients/', methods=['GET', 'POST'])
def add_clients():
    form = ClientForm()
    if form.validate_on_submit():
        new_client = Station.query.filter_by(secret_key=form.secret_key.data).first()
        if new_client is None:
            new_client = Station(name=form.name.data, surname=form.surname.data, username=form.username.data, password=form.password.data, phone_number=form.phone_number.data, secret_key = form.secret_key.data, play_time = form.play_time.data, playPrice = form.playPrice.data, play_sale = form.play_sale.data, full_play_time = form.full_play_time.data)
            db.session.add(new_client)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.surname.data = ''
        form.username.data = ''
        form.password.data = ''
        form.phone_number.data = ''
        form.secret_key.data = ''
        form.play_time.data = ''
        form.playPrice.data = ''
        form.play_sale.data = ''
        form.full_play_time.data = ''
    title = "hi"
    return render_template('add_client.html', form=form)
#/// Client

# /change-language/tk
@admins.route('/change-language/<code>')
def change_language(code):
    session['language'] = code
    return redirect('/azyk_haryt/')
    #return {'language': session['language']}
