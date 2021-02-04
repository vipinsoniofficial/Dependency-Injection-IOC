from injector import Module, Injector, inject, singleton
from flask_sqlalchemy import SQLAlchemy
from Keyvalue import Base, KeyValue
from method_call import X


class AppModule(Module):
    def __init__(self, app):
        self.app = app

    """Configure the application."""

    def configure(self, binder):
        # We configure the DB here, explicitly, as Flask-SQLAlchemy requires
        # the DB to be configured before request handlers are called.
        x = self.config()
        db = self.configure_db(self.app)
        binder.bind(SQLAlchemy, to=db, scope=singleton)
        binder.bind(X, to=x, scope=singleton)

    def configure_db(self, app):
        db = SQLAlchemy(app)
        Base.metadata.create_all(db.engine)
        db.session.add_all([KeyValue('hello', 'world'), KeyValue('goodbye', 'cruel world')])
        db.session.commit()
        return db

    def config(self):
        x = X()
        return x
