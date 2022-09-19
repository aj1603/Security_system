from glob import glob
from flask import  Blueprint, make_response, request, jsonify, render_template
import requests
from main import db
from main.models import Node, Station, Day, Month, Admin
from .netScanner import map_network
from datetime import datetime
from sqlalchemy import func
from main.db_data_utils.get_devices_data import get_devices_data

nol = 0  # number of

devices = Blueprint('devices', __name__)

@devices.route("/nodemcu/checkData/")
def check_state():
	# print(request.headers)
	# if 'resident-key' not in request.headers:
	# 	print("notin")
	# 	abort(401)
	# print(request.headers['resident-key'])
	# secret_key = request.headers['resident-key']
	# resident = Resident.query.filter_by(secret_key = secret_key).first()
	# print(resident.name)
	data = get_devices_data()
	return make_response(jsonify(data),200)


@devices.route("/scanNetwork/")
def scanNetwork():
	try:
		print("requested scanning")
		ip_addresses = map_network()
		print("scanning network, found data: {}".format(ip_addresses))
		for ip in ip_addresses:
			try:
				r = requests.get("http://{}/ping/".format(ip))
				print(r.text)
				device_command = r.text
				device = Node.query.filter_by(deviceKey = device_command).first()
				if device:
					try:
						device.ip = ip
						db.session.commit()
					except Exception as ex:
						print(ex)
			except Exception as ex:
				print("couldn't get data from an Ip {}, {}".format(ip, ex))
	except Exception as ex:
		print(ex)
	return make_response("scanning done",200)

# esp_json_to_arg

@devices.route("/buy_something/", methods=["GET", "POST"])
def buy_something():
    if request.method == "POST":
        req = request.get_json()
        reqCommand = req.get("command")
        reqPrice = req.get("playPrice")
        print(reqPrice, reqCommand)

        buy = Station.query.filter_by(command=reqCommand).first()
        dayBuy = Day.query.filter_by(id=buy.id).first()
        monthBuy = Month.query.filter_by(id=buy.id).first()
        satynAl = int(reqPrice)
        print(satynAl)
        buy.playPrice += satynAl
        dayBuy.playedPrice += satynAl
        monthBuy.playedPrice += satynAl
        db.session.commit()
        return "Hasaplandy"


@devices.route("/nodemcuControl/", methods=['GET','POST'])
def nodemcuControl():
    if request.method == 'POST':
        req = request.get_json()
        command = req["command"]
        state = req["state"]

        device = Node.query.filter_by(command = command).first()
        global idForStation
        idForStation = (device.id)
        device.state=state
        db.session.commit()
        if device.state == 1:
            print("first_time")
            first_time()
            print("first")
        if device.state == 0:
            print("second_time")
            second_time()
            print("second")
        controlIp = device.ip
        deviceState = str(device.state)	
        print(controlIp, deviceState)
        try:
            print("ugratjak")
            requests.get("http://{}/control/?command={}".format(controlIp, deviceState))
            print("ugradyldy")
            return "OK"
        except Exception as ex:
            return 'Error'
    return make_response("error, couldn't make a request (no device found)",200)

#first_time_dontrol
def first_time():
    e = datetime.now()
    try:
        games = Station.query.filter_by(id = idForStation).first()
        if games.startTime is not None:
            return "Hasaplam"            
        games.startTime = e
        games.endTime = None
        games.playInterval = None
        games.playPrice = nol
        db.session.commit() 
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)

# second_time_control
def second_time():
    e = datetime.now()
    try:
        games = Station.query.filter_by(id = idForStation).first()
        day = Day.query.filter_by(id=games.id).first()
        month = Month.query.filter_by(id=games.id).first()
        if games.endTime is not None:
            return "Hasaplanmady"
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
        games.startTime = None
        db.session.commit()
        try:
            games = Station.query.filter_by(id = idForStation).first()
            day = Day.query.filter_by(stationId=games.id).first()
            month = Month.query.filter_by(stationId=games.id).first()
            d6 = games.discount
            if d6 == 0:
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
                return "Hasaplandy"
            if d6 > 0:
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
                return "Hasaplandy"
        except Exception as ex:
            print(f"error, couldn't make a request (connection issue) {ex}",200)
    except Exception as ex:
        print(f"error, couldn't make a request (connection issue) {ex}",200)