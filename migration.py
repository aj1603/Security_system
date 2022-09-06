from main import db

from main.models import (
	Securitys,
    Ps4_Ps5s,
    Admins,
    Games,
)

from main.db_migration_data.admin_config import admins, securitys
from main.db_migration_data.ps4_ps5_config import ps4_ps5_config
from main.db_migration_data.plays_config import games


db.drop_all()
db.create_all()

for admin in admins:
    db_admin = Admins(**admin)
    db.session.add(db_admin)
    db.session.commit()

for ps4_ps5 in ps4_ps5_config:
    db_ps4_ps5 = Ps4_Ps5s(**ps4_ps5)
    db.session.add(db_ps4_ps5)
    db.session.commit()

for security in securitys:
    db_security = Securitys(**security)
    db.session.add(db_security)
    db.session.commit()

for game in games:
    db_game = Games(**game)
    db.session.add(db_game)
    db.session.commit()