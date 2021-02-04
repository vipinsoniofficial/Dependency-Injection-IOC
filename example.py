from flask import Flask
from flask_injector import FlaskInjector
from injector import singleton, inject


class Dependency:
    def __init__(self):
        self.attr = 'dependency'

    def prrint(self):
        print(self.attr)


class Client:
    @inject
    def __init__(self, obj: Dependency):
        self.A = obj

    def print(self):
        print(self.A.prrint())


def configure(binder):
    binder.bind(Dependency, to=Dependency, scope=singleton)
    binder.bind(Client, to=Client, scope=singleton)


app = Flask(__name__)


@app.route('/')
def test(client: Client):
    print(client.A.prrint())
    return client.A.attr


FlaskInjector(app=app, modules=[configure])

if __name__ == '__main__':
    app.run(debug=True)