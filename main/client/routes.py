from flask import Blueprint, session, redirect, render_template, request
from  .forms import ClientForm, ClientUpdateForm
from main.models import Clients
from main import db

clients = Blueprint('clients', __name__)


@clients.route('/all_clients/')
def all_clients():
    our_clients = Clients.query.all()
    return render_template("client.html", our_clients=our_clients)

@clients.route('/for_logo/')
def for_logo():
    return render_template("index.html")

@clients.route('/yuwunmak_ucin/')
def yuwunmak_ucin():
    clear_products = Clients.query.filter_by(product_type=2)
    return render_template("clear_pro.html", clear_products=clear_products)

@clients.route('/electronics_tel/')
def electronics_tel():
    tel_products = Clients.query.filter_by(product_type=3)
    return render_template("electronics.html", tel_products=tel_products)

@clients.route('/azyk_haryt/')
def azyk_haryt():
    azyk_products = Clients.query.filter_by(product_type=1)
    return render_template("azyk_haryt.html", azyk_products=azyk_products)

# @clients.route('/game/<int:id>/delete/', methods=['GET', 'POST'])
# def delete_game(id):
#     delete_game = Clients.query.get_or_404(id)
#     db.session.delete(delete_game)
#     db.session.commit()
#     our_games = Clients.query.all()
#     return render_template("products.html", our_games=our_games)


# @clients.route('/game/<int:id>/update/', methods=['GET', 'POST'])
# def update_game(id):
#     games = Clients.query.get_or_404(id)
#     form = ClientUpdateForm()
#     if form.validate_on_submit():
#         games.game_name = form.game_name.data
#         games.description = form.description.data
#         games.game_price = form.game_price.data
#         games.game_sale = form.game_sale.data
#         games.today_sale = form.today_sale.data
#         games.compitation = form.compitation.data
#         db.session.commit()
#         our_games = Clients.query.all()
#         return render_template("products.html", our_games=our_games)
#     elif request.method == 'GET':
#         form.game_name.data = games.game_name
#         form.description.data = games.description
#         form.game_price.data = games.game_price
#         form.game_sale.data = games.game_sale
#         form.today_sale.data = games.today_sale
#         form.compitation.data = games.compitation
#         return render_template("edit_game.html", form=form)

@clients.route('/add_clients/', methods=['GET', 'POST'])
def add_clients():
    form = ClientForm()
    if form.validate_on_submit():
        new_client = Clients.query.filter_by(secret_key=form.secret_key.data).first()
        if new_client is None:
            new_client = Clients(name=form.name.data, surname=form.surname.data, username=form.username.data, password=form.password.data, phone_number=form.phone_number.data, secret_key = form.secret_key.data, play_time = form.play_time.data, play_price = form.play_price.data, play_sale = form.play_sale.data, full_play_time = form.full_play_time.data)
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
        form.play_price.data = ''
        form.play_sale.data = ''
        form.full_play_time.data = ''
    title = "hi"
    return render_template('add_client.html', form=form)

# /change-language/tk
@clients.route('/change-language/<code>')
def change_language(code):
    session['language'] = code
    return redirect('/azyk_haryt/')
    #return {'language': session['language']}
