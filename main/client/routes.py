from flask import Blueprint, session, redirect, render_template, request
from  .forms import ClientForm, ClientUpdateForm
from main.models import Client
from main import db
import datetime
cur_time = datetime.datetime.now()

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

@clients.route('/client/<int:id>/delete/', methods=['GET', 'POST'])
def delete_client(id):
    delete_client = Clients.query.get_or_404(id)
    db.session.delete(delete_client)
    db.session.commit()
    our_clients = Clients.query.all()
    return render_template("client.html", our_clients=our_clients)


@clients.route('/client/<int:id>/update/', methods=['GET', 'POST'])
def update_client(id):
    clients = Clients.query.get_or_404(id)
    form = ClientUpdateForm()
    if form.validate_on_submit():
        clients.name = form.name.data
        clients.surname = form.surname.data
        clients.username = form.username.data
        clients.password = form.password.data
        clients.phone_number = form.phone_number.data
        clients.secret_key = form.secret_key.data
        clients.play_time = form.play_time.data
        clients.play_price = form.play_price.data
        clients.play_sale = form.play_sale.data
        clients.full_play_time = form.full_play_time.data
        db.session.commit()
        our_clients = Clients.query.all()
        return render_template("client.html", our_clients=our_clients)
    elif request.method == 'GET':
        form.name.data = clients.name
        form.surname.data = clients.surname
        form.username.data = clients.username
        form.password.data = clients.password
        form.phone_number.data = clients.phone_number
        form.secret_key.data = clients.secret_key
        form.play_time.data = clients.play_time
        form.play_price.data = clients.play_price
        form.play_sale.data = clients.play_sale
        form.full_play_time.data = clients.full_play_time

        return render_template("edit_client.html", form=form)

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
