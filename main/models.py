from datetime import datetime
from xmlrpc import client
from main import app, db


class Ps4_Ps5s(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ps4_ps5_key = db.Column(db.String(150), nullable=False, unique=True)
    ps4_ps5_name = db.Column(db.String(150), nullable=False)
    ps4_ps5_price = db.Column(db.String(255))
    description = db.Column(db.String(1000))
    play_time_today = db.Column(db.Float(200))
    play_time_month = db.Column(db.Float(500))
    play_price = db.Column(db.Float(150))
    play_sale = db.Column(db.Float(150))
    today_income = db.Column(db.Float(150))
    last_day_income = db.Column(db.Float(200))
    last_month_income = db.Column(db.Float(300))
    dateAdded = db.Column(db.DateTime,default=datetime.now())
    dateUpdated = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())
    
    def json(self):
        ps4_ps5 = {
            "id": self.id,
            "ps4_ps5_name": self.ps4_ps5_name,
            "ps4_ps5_price": self.ps4_ps5_price,
            "description": self.description,
            "play_time_today": self.play_time_today,
            "play_time_month": self.play_time_month,
            "ps4_ps5_key": self.ps4_ps5_key,
            "play_price": self.play_price,
            "today_income": self.today_income,
            "last_day_income": self.last_day_income,
            "last_month_income": self.last_month_income,
            "play_sale": self.play_sale,
            "dateAdded": self.dateAdded,
            "dateUpdated": self.dateUpdated
        }
        return ps4_ps5

    def __repr__(self):
        return f"User('{self.ps4_ps5_name}', '{self.ps4_ps5_price}', '{self.description}', '{self.play_time_today}', '{self.play_time_month}', '{self.today_income}', '{self.last_day_income}'{self.ps4_ps5_key}', '{self.play_price}', '{self.today_income}', '{self.last_day_income}', '{self.last_month_income}', '{self.play_sale}', '{self.dateAdded}', '{self.dateUpdated})"

class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    surname = db.Column(db.String(150))
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(150))
    phone_number = db.Column(db.String(50))
    secret_key = db.Column(db.String(150), nullable=False)
    play_time = db.Column(db.Float(150), nullable=False)
    play_price = db.Column(db.Float(150), nullable=False)
    play_sale = db.Column(db.Float(150), nullable=False)
    full_play_time = db.Column(db.Float(200), nullable=False)
    dateAdded = db.Column(db.DateTime,default=datetime.utcnow)
    dateUpdated = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())

    def json(self):
        client = {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "username": self.username,
            "password": self.password,
            "phone_number": self.phone_number,
            "secret_key": self.secret_key,
            "play_time": self.play_time,
            "play_price": self.play_price,
            "play_sale": self.play_sale,
            "full_play_time": self.full_play_time,
            "dateAdded": self.dateAdded,
            "dateUpdated": self.dateUpdated
        }
        return client

    def __repr__(self):
        return f"User('{self.name}', '{self.surname}', '{self.username}', '{self.password}', '{self.phone_number}', '{self.secret_key}', '{self.play_time}', '{self.play_price}',, '{self.play_sale}', '{self.full_play_time}', '{self.dateAdded}', '{self.dateUpdated}')"

class Admins(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    surname = db.Column(db.String(150))
    email = db.Column(db.String(150), nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(150))
    phone_number = db.Column(db.String(50))
    passport_number = db.Column(db.String(50))
    secret_key = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(1000))
    ps4_ps5_key = db.Column(db.String(150), nullable=False, unique=True)
    play_price = db.Column(db.Float(150), nullable=False)
    play_sale = db.Column(db.Float(50))
    today_income = db.Column(db.Float(150), nullable=False)
    last_day_income = db.Column(db.Float(200), nullable=False)
    last_month_income = db.Column(db.Float(300), nullable=False)
    dateAdded = db.Column(db.DateTime,default=datetime.now())
    dateUpdated = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())

    def json(self):
        admin = {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "phone_number": self.phone_number,
            "passport_number": self.passport_number,
            "secret_key": self.secret_key,
            "description": self.description,
            "ps4_ps5_key": self.ps4_ps5_key,
            "play_price": self.play_price,
            "today_income": self.today_income,
            "last_day_income": self.last_day_income,
            "last_month_income": self.last_month_income,
            "play_sale": self.play_sale,
            "dateAdded": self.dateAdded,
            "dateUpdated": self.dateUpdated
        }
        return admin
        
    def __repr__(self):
        return f"User('{self.name}', '{self.surname}', '{self.email}', '{self.username}', '{self.password}', '{self.passport_number}', '{self.phone_number}', '{self.secret_key}', '{self.description}', '{self.ps4_ps5_key}', '{self.play_price}', '{self.today_income}', '{self.last_day_income}', '{self.last_month_income}', '{self.play_sale}', '{self.dateAdded}', '{self.dateUpdated}')"

class Securitys(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    surname = db.Column(db.String(150))
    email = db.Column(db.String(150), nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(150))
    phone_number = db.Column(db.String(50))
    passport_number = db.Column(db.String(50))
    secret_key = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(1000))
    play_time = db.Column(db.Float(150), nullable=False)
    play_price = db.Column(db.Float(150), nullable=False)
    play_sale = db.Column(db.Float(150), nullable=False)
    full_play_time = db.Column(db.Float(200), nullable=False)
    dateAdded = db.Column(db.DateTime,default=datetime.now())
    dateUpdated = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())

    def json(self):
        security = {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "phone_number": self.phone_number,
            "passport_number": self.passport_number,
            "secret_key": self.secret_key,
            "description": self.description,
            "play_time": self.play_time,
            "play_price": self.play_price,
            "play_sale": self.play_sale,
            "full_play_time": self.full_play_time,
            "dateAdded": self.dateAdded,
            "dateUpdated": self.dateUpdated,
        }
        return security
        
    def __repr__(self):
        return f"User('{self.name}', '{self.surname}', '{self.email}', '{self.password}', '{self.phone_number}', '{self.secret_key}', '{self.description}', '{self.username}', '{self.play_time}', '{self.play_price}',, '{self.play_sale}', '{self.full_play_time}', '{self.dateUpdated}')"

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(1000))
    game_price = db.Column(db.Float(150))
    game_sale = db.Column(db.Float(150))
    today_sale = db.Column(db.Float(200))
    compitation = db.Column(db.String(100))
    game_pictures = db.Column(db.String(1000))
    dateAdded = db.Column(db.DateTime,default=datetime.now())
    dateUpdated = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())
    
    def json(self):
        play = {
            "id": self.id,
            "ps4_ps5_name": self.game_name,
            "description": self.description,
            "play_price": self.game_price,
            "play_sale": self.game_sale,
            "today_sale": self.today_sale,
            "compitation": self.compitation,
            "dateAdded": self.dateAdded,
            "dateUpdated": self.dateUpdated,
        }
        return play

    def __repr__(self):
        return f"User('{self.game_name}', '{self.description}', '{self.game_price}', '{self.today_sale}', '{self.compitation}', '{self.game_sale}', '{self.dateAdded}', '{self.dateUpdated})"
