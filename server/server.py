#!/usr/bin/env python
import os
import sqlite3
from flask import Flask
from flask import g
from core import NKF
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, "server.db"),
    DEBUG=True,
))

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('initial.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def init_core():
    app.nkf = NKF(g.get_db())

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def hello_world():
    return "Hello"

@app.route('/vat', methods=["GET"])
def list_vats():
    return "Lista"

if __name__ == "__main__":
    app.init_core()
    app.run()
