import logging

from injector import Module, Injector, inject, singleton
from flask import Flask, Request, jsonify
from flask_injector import FlaskInjector
from flask_sqlalchemy import SQLAlchemy
from Keyvalue import KeyValue
from sqlalchemy.orm.exc import NoResultFound

from method_call import X
from config import AppModule


def configure_views(app):
    @inject
    @app.route('/<key>')
    def get(key, db: SQLAlchemy, x: X):
        try:
            print(x.print(23))
            print(x.print(23))
            print(x.print(23))
            print(x.print(23))
            print(x.print(23))
            print(x.print(23))
            print(x.print(23))

            kv = db.session.query(KeyValue).filter(KeyValue.key == key).one()
        except NoResultFound:
            response = jsonify(status='No such key', context=key)
            response.status = '404 Not Found'
            return response
        return jsonify(key=kv.key, value=kv.value)

    @app.route('/')
    def list(db: SQLAlchemy):
        data = [i.key for i in db.session.query(KeyValue).order_by(KeyValue.key)]
        return jsonify(keys=data)

    @app.route('/', methods=['POST'])
    def create(request: Request, db: SQLAlchemy):
        kv = KeyValue(request.form['key'], request.form['value'])
        db.session.add(kv)
        db.session.commit()
        response = jsonify(status='OK')
        response.status = '201 CREATED'
        return response

    @app.route('/<key>', methods=['DELETE'])
    def delete(db: SQLAlchemy, key):
        db.session.query(KeyValue).filter(KeyValue.key == key).delete()
        db.session.commit()
        response = jsonify(status='OK')
        response.status = '200 OK'
        return response


def main():
    app = Flask(__name__)
    app.config.update(
        DB_CONNECTION_STRING=':memory:',
        SQLALCHEMY_DATABASE_URI='sqlite://',
        SQLALCHEMY_TRACK_MODIFICATIONS=True
    )
    app.debug = True

    injector = Injector([AppModule(app)])
    configure_views(app=app)

    FlaskInjector(app=app, injector=injector)

    client = app.test_client()

    response = client.get('/')
    print('%s\n%s%s' % (response.status, response.headers, response.data))
    response = client.post('/', data={'key': 'foo', 'value': 'bar'})
    print('%s\n%s%s' % (response.status, response.headers, response.data))
    response = client.get('/')
    print('%s\n%s%s' % (response.status, response.headers, response.data))
    response = client.get('/hello')
    print('%s\n%s%s' % (response.status, response.headers, response.data))
    response = client.delete('/hello')
    print('%s\n%s%s' % (response.status, response.headers, response.data))
    response = client.get('/')
    print('%s\n%s%s' % (response.status, response.headers, response.data))
    response = client.get('/hello')
    print('%s\n%s%s' % (response.status, response.headers, response.data))
    response = client.delete('/hello')
    print('%s\n%s%s' % (response.status, response.headers, response.data))


if __name__ == '__main__':
    main()
