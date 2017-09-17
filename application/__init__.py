# DB username: tylerjamesmalloy
# DB password: PTgRa%_'^;xpn&.,4r&ytcrqd.cCMY#\
# DB instance: lumohackscsss
# aws-eb passphrase: Y_8(ds9/e^bTQzpX

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

application = Flask(__name__, instance_relative_config=True)

lm = LoginManager()
lm.login_view = 'login'
lm.init_app(application)

db = SQLAlchemy(application)
db.create_all()

migrate = Migrate(application, db)
manager = Manager(application)
manager.add_command('db', MigrateCommand)

from application import views, models