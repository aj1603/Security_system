from turtle import pos
from flask import render_template, Blueprint, request, redirect, url_for
from .forms import GameForm, GameUpdateForm
from main.models import Games
from main import db

games = Blueprint('games', __name__)

@games.route('/all_games/')
def all_games():
    our_games = Games.query.all()
    return render_template("products.html", our_games=our_games)

@games.route('/for_logo/')
def for_logo():
    return render_template("index.html")

@games.route('/yuwunmak_ucin/')
def yuwunmak_ucin():
    clear_products = Games.query.filter_by(product_type=2)
    return render_template("clear_pro.html", clear_products=clear_products)

@games.route('/electronics_tel/')
def electronics_tel():
    tel_products = Games.query.filter_by(product_type=3)
    return render_template("electronics.html", tel_products=tel_products)

@games.route('/azyk_haryt/')
def azyk_haryt():
    azyk_products = Games.query.filter_by(product_type=1)
    return render_template("azyk_haryt.html", azyk_products=azyk_products)

@games.route('/game/<int:id>/delete/', methods=['GET', 'POST'])
def delete_game(id):
    delete_game = Games.query.get_or_404(id)
    db.session.delete(delete_game)
    db.session.commit()
    our_games = Games.query.all()
    return render_template("products.html", our_games=our_games)


@games.route('/game/<int:id>/update/', methods=['GET', 'POST'])
def update_game(id):
    games = Games.query.get_or_404(id)
    form = GameUpdateForm()
    if form.validate_on_submit():
        games.game_name = form.game_name.data
        games.description = form.description.data
        games.game_price = form.game_price.data
        games.game_sale = form.game_sale.data
        games.today_sale = form.today_sale.data
        games.compitation = form.compitation.data
        db.session.commit()
        our_games = Games.query.all()
        return render_template("products.html", our_games=our_games)
    elif request.method == 'GET':
        form.game_name.data = games.game_name
        form.description.data = games.description
        form.game_price.data = games.game_price
        form.game_sale.data = games.game_sale
        form.today_sale.data = games.today_sale
        form.compitation.data = games.compitation
        return render_template("edit_game.html", form=form)

@games.route('/add_games/', methods=['GET', 'POST'])
def add_games():
    form = GameForm()
    if form.validate_on_submit():
        new_game = Games.query.filter_by(game_name=form.game_name.data).first()
        if new_game is None:
            new_game = Games(game_name=form.game_name.data, game_price=form.game_price.data, game_sale=form.game_sale.data, description=form.description.data, today_sale=form.today_sale.data, compitation = form.compitation.data)
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
