from datetime import datetime
from xmlrpc import client
from main import app, db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    surname = db.Column(db.String(150))
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150))
    phoneNumber = db.Column(db.String(50), unique=True)
    isPatron = db.Column(db.Boolean, default=False)
    dateAdded = db.Column(db.DateTime,default=datetime.now())
    dateUpdated = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())

    def json(self):
        admin = {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "password": self.password,
            "phoneNumber": self.phoneNumber,
            "isPatron": self.isPatron,
            "dateAdded": self.dateAdded,
            "dateUpdated": self.dateUpdated,
        }
        return admin
        
    def __repr__(self):
        return f"User('{self.name}', '{self.surname}', '{self.email}', '{self.password}', '{self.phoneNumber}', '{self.isPatron}')"


class Ps4_Ps5(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(150), nullable=False)
    isVip = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(200))
    pricePerHour = db.Column(db.Float)
    startTime = db.Column(db.DateTime)
    endTime = db.Column(db.DateTime)
    playInterval = db.Column(db.Integer)
    playPrice = db.Column(db.Float)
    discount = db.Column(db.Float)
    dayInfo = db.relationship('DayInfo',backref='ps',lazy=True)
    monthInfo = db.relationship('MonthInfo',backref='ps',lazy=True)
    device = db.relationship('Device',backref='ps',lazy=True)
    dateAdded = db.Column(db.DateTime,default=datetime.now())
    dateUpdated = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())
    
    def json(self):
        ps4_ps5 = {
            "id": self.id,
            "status": self.status,
            "isVip": self.isVip,
            "name": self.name,
            "pricePerHour": self.pricePerHour,
            "startTime": self.startTime,
            "endTime": self.endTime,
            "playInterval": self.playInterval,
            "playPrice": self.playPrice,
            "discount": self.discount,
            "dayInfo": self.dayInfo,
            "monthInfo": self.monthInfo,
            "device": self.device,
            "dateAdded": self.dateAdded,
            "dateUpdated": self.dateUpdated
        }
        return ps4_ps5

    def __repr__(self):
        return f"User('{self.status}', '{self.isVip}', '{self.name}', '{self.pricePerHour,}', '{self.startTime,}', '{self.discount}', '{self.endTime,}', '{self.dayInfo}', '{self.monthInfo}', '{self.playInterval,}', '{self.playPrice,}', '{self.device}', '{self.dateAdded}', '{self.dateUpdated})"

class DayInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playedTime = db.Column(db.Integer)
    playedPrice = db.Column(db.Float)
    psId = db.Column(db.Integer,db.ForeignKey("ps.id"))
    dateAdded = db.Column(db.DateTime,default=datetime.now())
    dateUpdated = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())
    
    def json(self):
        ps4_ps5 = {
            "id": self.id,
            "playedTime": self.playedTime,
            "playedPrice": self.playedPrice,
            "psId": self.psId,
            "dateAdded": self.dateAdded,
            "dateUpdated": self.dateUpdated
        }
        return ps4_ps5

    def __repr__(self):
        return f"User('{self.playedTime}', '{self.playedPrice}', '{self.psId}', '{self.dateAdded}', '{self.dateUpdated})"


class MonthInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playedTime = db.Column(db.Integer)
    playedPrice = db.Column(db.Float)
    psId = db.Column(db.Integer,db.ForeignKey("ps.id"))
    dateAdded = db.Column(db.DateTime,default=datetime.now())
    dateUpdated = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())
    
    def json(self):
        ps4_ps5 = {
            "id": self.id,
            "playedTime": self.playedTime,
            "playedPrice": self.playedPrice,
            "psId": self.psId,
            "dateAdded": self.dateAdded,
            "dateUpdated": self.dateUpdated
        }
        return ps4_ps5

    def __repr__(self):
        return f"User('{self.playedTime}', '{self.playedPrice}', '{self.psId}', '{self.dateAdded}', '{self.dateUpdated})"

class Device(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    ip = db.Column(db.String(100))
    deviceKey = db.Column(db.String(1000),nullable=False)
    secretKey = db.Column(db.String(1000),nullable=False)
    command = db.Column(db.String(100))
    state = db.Column(db.Integer,default=0)
    psId = db.Column(db.Integer,db.ForeignKey("ps.id"))
    dateAdded = db.Column(db.DateTime,default=datetime.now())
    dateUpdated = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())

    def json(self):
        device = {
            "id": self.id,
            "name": self.name,
            "ip": self.ip,
            "deviceKey": self.deviceKey,
            "secretKey": self.secretKey,
            "command": self.command,
            "state": self.state,
            "psId": self.psId,
            "dateAdded": self.dateAdded,
            "dateUpdated": self.dateUpdated
        }
        return device

    def __repr__(self):
        return f"User('{self.name}', '{self.ip}', '{self.deviceKey}', '{self.command}', '{self.secretKey}', '{self.state}', '{self.psId}' '{self.dateAdded}', '{self.dateUpdated}')"

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), unique=True)
    phoneNumber = db.Column(db.String(50))
    discount = db.Column(db.Float)
    playedTime = db.Column(db.Float)
    dateAdded = db.Column(db.DateTime,default=datetime.utcnow)
    dateUpdated = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())

    def json(self):
        client = {
            "id": self.id,
            "name": self.name,
            "password": self.password,
            "phoneNumber": self.phoneNumber,
            "discount": self.discount,
            "playedTime": self.playedTime,
            "dateAdded": self.dateAdded,
            "dateUpdated": self.dateUpdated
        }
        return client

    def __repr__(self):
        return f"User('{self.name}', '{self.password}', '{self.phoneNumber}', '{self.discount}', '{self.playedTime}', '{self.dateAdded}', '{self.dateUpdated}')"