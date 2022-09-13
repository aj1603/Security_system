from main import db

from main.models import (
    Station,
    Admin,
    Day,
    Month,
    Node,
    Client,
)

from main.db_migration_data.admin_config import admins, securitys
from main.db_migration_data.ps4_ps5_config import ps4_ps5_config
from main.db_migration_data.device_config import device

db.drop_all()
db.create_all()

for admin in admins:
    db_admin = Admin(**admin)
    db.session.add(db_admin)
    db.session.commit()

for ps4_ps5 in ps4_ps5_config:
    db_ps4_ps5 = Station(**ps4_ps5)
    db.session.add(db_ps4_ps5)
    db.session.commit()

for security in securitys:
    db_security = Admin(**security)
    db.session.add(db_security)
    db.session.commit()

for dev_config in device:
    db_dev_config = Node(**dev_config)
    db.session.add(db_dev_config)
    db.session.commit()

