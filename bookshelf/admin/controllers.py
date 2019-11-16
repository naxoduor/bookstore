from sqlalchemy import exc
from flask import Blueprint, flash
from flask import current_app
from bookshelf.data.models import Author, db

admin = Blueprint('admin', __name__)


@admin.route('/')
def index():
    author1 = Author('Chris Ronny')
    try:
        db.session.add(author1)
        db.session.commit()
        flash("Author succesfully created")
        return "User created succesfully"
    except exc.SQLAlchemyError as e:
        flash("Author was not created")
        current_app.logger.error(e )
        return "User not created"
