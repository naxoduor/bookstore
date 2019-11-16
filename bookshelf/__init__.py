from flask import Flask
from bookshelf.main.controllers import main
from bookshelf.admin.controllers import admin
from bookshelf.config import configure_app
from bookshelf.data.models import db


app = Flask(__name__)

configure_app(app)
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')

