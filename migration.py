from main import db

from main.models import (
    Ps4_Ps5,
    Admin,
    DayInfo,
    MonthInfo,
    Device,
    Client,
)

from main.db_migration_data.admin_config import admins
from main.db_migration_data.ps4_ps5_config import ps4_ps5_config

db.drop_all()
db.create_all()

for admin in admins:
    db_admin = Admin(**admin)
    db.session.add(db_admin)
    db.session.commit()

for ps4_ps5 in ps4_ps5_config:
    db_ps4_ps5 = Ps4_Ps5(**ps4_ps5)
    db.session.add(db_ps4_ps5)
    db.session.commit()