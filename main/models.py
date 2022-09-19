from calendar import month
from datetime import datetime
from xmlrpc import client
from main import app, db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
	return Admin.query.get(int(id))

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    surname = db.Column(db.String(150))
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150))
    phoneNumber = db.Column(db.String(50), unique=True)
    isPatron = db.Column(db.Boolean, default=False)
    dateAdded = db.Column(db.DateTime,default=datetime.now())
    dateUpdated = db.Column(db.DateTime,default=datetime.now())

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
        return f"Admin('{self.name}', '{self.surname}', '{self.email}', '{self.password}', '{self.phoneNumber}', '{self.isPatron}')"


class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(150), nullable=False)
    isVip = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(200))
    command = db.Column(db.String(200))
    pricePerHour = db.Column(db.Float(150))
    startTime = db.Column(db.DateTime, nullable=True)
    endTime = db.Column(db.DateTime, nullable=True)
    playInterval = db.Column(db.Integer)
    playPrice = db.Column(db.Float(150), default=0.0)
    discount = db.Column(db.Float(150))
    day = db.relationship("Day", uselist=False, backref="station")
    month = db.relationship("Month", uselist=False, backref="station")
    node = db.relationship("Node", uselist=False, backref="station")
    dateAdded = db.Column(db.DateTime,default=datetime.now())
    dateUpdated = db.Column(db.DateTime,default=datetime.now())
    
    def json(self):
        playstation = {
            "id": self.id,
            "status": self.status,
            "isVip": self.isVip,
            "name": self.name,
            "command": self.command,
            "pricePerHour": self.pricePerHour,
            "startTime": self.startTime,
            "endTime": self.endTime,
            "playInterval": self.playInterval,
            "playPrice": self.playPrice,
            "discount": self.discount,
            "dateAdded": self.dateAdded,
            "dateUpdated": self.dateUpdated,
        }
        return playstation

    def __repr__(self):
        return f"Station('{self.status}', '{self.isVip}', '{self.name}', '{self.command}', '{self.pricePerHour,}', '{self.startTime,}', '{self.discount}', '{self.endTime,}', '{self.playPrice,}', '{self.node}', '{self.dateAdded}', '{self.dateUpdated})"

class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    playedTime = db.Column(db.Integer, default=0)
    playedPrice = db.Column(db.Float(150), default=0.0)    
    stationId = db.Column(db.Integer,db.ForeignKey("station.id"))
    dateAdded = db.Column(db.DateTime,default=datetime.now())
    dateUpdated = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())
    
    def json(self):
        day = {
            "id": self.id,
            "name": self.name,
            "playedTime": self.playedTime,
            "playedPrice": self.playedPrice,
            "stationId": self.stationId,
            "dateAdded": self.dateAdded,
            "dateUpdated": self.dateUpdated,
        }
        return day

    def __repr__(self):
        return f"Day('{self.name}', '{self.playedTime}', '{self.playedPrice}', '{self.stationId}', '{self.dateAdded}', '{self.dateUpdated}')"


class Month(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    playedTime = db.Column(db.Integer, default=0)
    playedPrice = db.Column(db.Float(150), default=0.0)
    stationId = db.Column(db.Integer,db.ForeignKey("station.id"))
    dateAdded = db.Column(db.DateTime,default=datetime.now())
    dateUpdated = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())
    
    def json(self):
        month = {
            "id": self.id,
            "name": self.name,
            "playedTime": self.playedTime,
            "playedPrice": self.playedPrice,
            "stationId": self.stationId,
            "dateAdded": self.dateAdded,
            "dateUpdated": self.dateUpdated,
        }
        return month

    def __repr__(self):
        return f"Month('{self.name}', '{self.playedTime}', '{self.playedPrice}', '{self.stationId}', '{self.dateAdded}', '{self.dateUpdated})"

class Node(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    ip = db.Column(db.String(100))
    deviceKey = db.Column(db.String(1000),nullable=False)
    secretKey = db.Column(db.String(1000),nullable=False)
    command = db.Column(db.String(100))
    state = db.Column(db.Integer,default=0)
    stationId = db.Column(db.Integer,db.ForeignKey("station.id"))
    dateAdded = db.Column(db.DateTime,default=datetime.now())
    dateUpdated = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())

    def json(self):
        node = {
            "id": self.id,
            "name": self.name,
            "ip": self.ip,
            "deviceKey": self.deviceKey,
            "secretKey": self.secretKey,
            "command": self.command,
            "state": self.state,
            "stationId": self.stationId,
            "dateAdded": self.dateAdded,
            "dateUpdated": self.dateUpdated,
        }
        return node

    def __repr__(self):
        return f"Node('{self.name}', '{self.ip}', '{self.deviceKey}', '{self.command}', '{self.secretKey}', '{self.state}', '{self.stationId}', '{self.dateAdded}', '{self.dateUpdated}')"

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), unique=True)
    phoneNumber = db.Column(db.String(50))
    discount = db.Column(db.Float(150))
    playedTime = db.Column(db.Float(150))
    dateAdded = db.Column(db.DateTime,default=datetime.utcnow)
    dateUpdated = db.Column(db.DateTime,default=datetime.now())

    def json(self):
        client = {
            "id": self.id,
            "name": self.name,
            "password": self.password,
            "phoneNumber": self.phoneNumber,
            "discount": self.discount,
            "playedTime": self.playedTime,
            "dateAdded": self.dateAdded,
            "dateUpdated": self.dateUpdated,
        }
        return client

    def __repr__(self):
        return f"Client('{self.name}', '{self.password}', '{self.phoneNumber}', '{self.discount}', '{self.playedTime}', '{self.dateAdded}', '{self.dateUpdated}')"