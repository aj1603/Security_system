from main import db

from main.models import (
    Station,
    Admin,
    Day,
    Month,
    Node,
    Client,
)

from main.db_migration_data.admin_config import admins, securities
from main.db_migration_data.station_config import stations
from main.db_migration_data.device_config import devices
from main.db_migration_data.day_month_config import day_config, month_config

db.drop_all()
db.create_all()

for admin in admins:
    db_admin = Admin(**admin)
    db.session.add(db_admin)
    db.session.commit()

for station in stations:
    db_station = Station(**station)
    db.session.add(db_station)
    db.session.commit()

for security in securities:
    db_security = Admin(**security)
    db.session.add(db_security)
    db.session.commit()

for dev_config in devices:
    db_dev_config = Node(**dev_config)
    db.session.add(db_dev_config)
    db.session.commit()

for day_conf in day_config:
    db_day_conf = Day(**day_conf)
    db.session.add(db_day_conf)
    db.session.commit()

for month_conf in month_config:
    db_month_conf = Month(**month_conf)
    db.session.add(db_month_conf)
    db.session.commit()

