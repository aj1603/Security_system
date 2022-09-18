from sqlalchemy.orm import joinedload
from main.models import Node, Station, Day, Month


def get_devices_data(id = None, db_models = None):
	if id:
		node = Node.query.filter_by(id = id).all()

	elif db_models:
		node = db_models

	else:
		nodes = Node.query.all()
		days = Day.query.all()
		months = Month.query.all()
		stations = Station.query.all()


	data = []
	for node in nodes:
		info = node.json()
		data.append(info)

	for station in stations:
		info = station.json()
		data.append(info)

	for day in days:
		info = day.json()
		data.append(info)

	for month in months:
		info = month.json()
		data.append(info)


	res = {
		"data": data,
		"message": "All sensor datas",
		"type": "sensors"
	}
	return res