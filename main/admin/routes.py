from distutils.sysconfig import get_makefile_filename
from flask import Blueprint, session, redirect, render_template, flash, request
from sqlalchemy import null
from main.models import Station, Client, Admin, Day, Month
from main import db
from datetime import datetime, timedelta
from .forms import ClientForm, ClientUpdateForm, GameForm, GameUpdateForm, LoginForm, DisCountForm
from flask_login import (
	login_user,
	current_user,
	logout_user,
)
admins = Blueprint('admins', __name__)
e = datetime.now()

nol = 0

@admins.route('/', methods=["GET", "POST"])
def login():
	if request.method == 'GET':
		if current_user.is_authenticated:
			if current_user.isPatron == 1:
				return redirect("/admin")
		return render_template ("admin/login.html")

	if request.method == 'POST':
		username = request.form.get("username")
		password = request.form.get("password")
		try:
			user = Resident.query.filter_by(username = username).first()
			if user:
				if(user and user.password==password):
					login_user(user)
					next_page = request.args.get('next')
					if user.typeId == 1:
						return redirect(next_page) if next_page else redirect("/admin")
					else:
						return redirect(next_page) if next_page else redirect("/resident")
				else:
					raise Exception
			else:
				raise Exception				
		except Exception as ex:
			flash(f'Login ýalňyşlygy, ulanyjy ady ya-da açarsöz ýalnyş!','danger')
			print(ex)
	return render_template ("admin/login.html")


@admins.route("/logout/")
def logout():
	logout_user()
	return redirect(url_for("login"))


@admins.route('/admin/for_logo/')
def for_logo():
    return render_template("index.html")

@admins.route('/all_ps4_ps5/')
def all_ps4_ps5():
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
        if games.startTime is not None:
            game_cons = Station.query.all()
            return render_template("game.html", game_cons=game_cons)            
        games.startTime = e
        games.endTime = None
        games.playInterval = None
        games.playPrice = nol
        db.session.commit() 
        game_cons = Station.query.all()
        return render_template("game.html", game_cons=game_cons)
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)

@admins.route('/second_time/<int:id>/')
def second_time(id):
    e = datetime.now()
    try:
        games = Station.query.get_or_404(id)
        if games.endTime is not None:
            game_cons = Station.query.all()
            return render_template("game.html", game_cons=game_cons)
        endTime = e
        d0 = str(games.startTime)
        d1 = str(endTime)
        d2 = datetime.strptime(d0, "%Y-%m-%d %H:%M:%S.%f") #yr, mo, day, hr, min, sec
        d3 = datetime.strptime(d1, "%Y-%m-%d %H:%M:%S.%f")
        d4 = str(d3 - d2)
        games.playInterval = d4
        games.endTime = d3
        games.startTime = None
        db.session.commit()
        try:
            games = Station.query.get_or_404(id)
            d6 = games.discount
            if d6 > 0:
                d5 = games.playInterval
                d8 = d5.split(':')
                h_1 = int(d8[0])
                m_1 = int(d8[1])
                money = ((h_1 * 60) + m_1)
                sony = games.id
                if sony == 1 or sony == 2:
                    full_money = money * 0.583333333
                    fullMoney = full_money - ((full_money * d6)/100)
                    games.playPrice = fullMoney
                    db.session.commit()
                elif sony == 3 or sony == 4 or sony == 5 or sony == 6:
                    full_money = money * 0.416666667
                    fullMoney = full_money - ((full_money * d6)/100)
                    games.playPrice = fullMoney
                    db.session.commit()
                elif sony == 7 or sony == 8 or sony == 9 or sony == 10:
                    full_money = money * 0.333333333
                    fullMoney = full_money - ((full_money * d6)/100)                    
                    games.playPrice = fullMoney
                    db.session.commit()
                game_cons = Station.query.all()
                return render_template("game.html", game_cons=game_cons)
        except Exception as ex:
            print(f"error, couldn't make a request (connection issue) {ex}",200)
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)

  
@admins.route('/count_price/<int:id>/')
def count_price(id):
    try:
        games = Station.query.get_or_404(id)
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


@admins.route('/full_count_price/')
def full_count_price():
    try:
        games_0 = Station.query.filter_by(id = 1).first()
        games_1 = Station.query.filter_by(id = 2).first()
        games_2 = Station.query.filter_by(id = 3).first()
        games_3 = Station.query.filter_by(id = 4).first()
        games_4 = Station.query.filter_by(id = 5).first()
        games_5 = Station.query.filter_by(id = 6).first()
        games_6 = Station.query.filter_by(id = 7).first()
        games_7 = Station.query.filter_by(id = 8).first()
        games_8 = Station.query.filter_by(id = 9).first()
        games_9 = Station.query.filter_by(id = 10).first()
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
        boss_money = Admin.query.filter_by(id = 1).first()
        boss_money.today_income = full_today_money
        db.session.commit()
        boss_report = Admin.query.all()
        return render_template("report_today.html", boss_report = boss_report)
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)

@admins.route('/update_discount/<int:id>/', methods=['GET', 'POST'])
def update_discount(id):
    disCount = Station.query.get_or_404(id)
    form = DisCountForm()
    if form.validate_on_submit():
        print("alo")
        disCount.discount = form.today_sale.data
        db.session.commit()
        game_cons = Station.query.all()
        return render_template("game.html", game_cons=game_cons)
    elif request.method == 'GET':
        form.today_sale.data = disCount.discount
        return render_template("discount.html", form=form)

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

@admins.route('/game/<int:id>/delete/', methods=['GET', 'POST'])
def delete_game(id):
    delete_game = Station.query.get_or_404(id)
    db.session.delete(delete_game)
    db.session.commit()
    our_games = Station.query.all()
    return render_template("products.html", our_games=our_games)


@admins.route('/game/<int:id>/update/', methods=['GET', 'POST'])
def update_game(id):
    games = Station.query.get_or_404(id)
    form = GameUpdateForm()
    if form.validate_on_submit():
        games.game_name = form.game_name.data
        games.description = form.description.data
        games.game_price = form.game_price.data
        games.game_sale = form.game_sale.data
        games.today_sale = form.today_sale.data
        games.compitation = form.compitation.data
        db.session.commit()
        our_games = Station.query.all()
        return render_template("products.html", our_games=our_games)
    elif request.method == 'GET':
        form.game_name.data = games.game_name
        form.description.data = games.description
        form.game_price.data = games.game_price
        form.game_sale.data = games.game_sale
        form.today_sale.data = games.today_sale
        form.compitation.data = games.compitation
        return render_template("edit_game.html", form=form)

@admins.route('/add_games/', methods=['GET', 'POST'])
def add_games():
    form = GameForm()
    if form.validate_on_submit():
        new_game = Station.query.filter_by(game_name=form.game_name.data).first()
        if new_game is None:
            new_game = Station(game_name=form.game_name.data, game_price=form.game_price.data, game_sale=form.game_sale.data, description=form.description.data, today_sale=form.today_sale.data, compitation = form.compitation.data)
            db.session.add(new_game)
            db.session.commit()
        name = form.game_name.data
        form.game_name.data = ''
        form.description.data = ''
        form.game_price.data = ''
        form.game_sale.data = ''
        form.today_sale.data = ''
        form.compitation.data = ''
    title = "hi"
    return render_template('add_game.html', form=form)



# /change-language/tk
@admins.route('/change-language/<code>')
def change_language(code):
    session['language'] = code
    return redirect('/azyk_haryt/')
    #return {'language': session['language']}
