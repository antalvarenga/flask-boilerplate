from flask import Flask

from app.stores.database import db, migrate


def init_app(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)

    return db
