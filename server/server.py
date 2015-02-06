#!/usr/bin/env python
import os
import json
import sqlite3
from flask import Flask
from flask import g
from flask import request
from flask import jsonify
from nkf import NKF
from flask.ext.restful import reqparse, abort, Api, Resource
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, "server.db"),
    DEBUG=True,
))
api = Api(app)

class Vats(Resource):
    def get(self):
        lista = app.core.vat_list()
        return lista

class Vat(Resource):
    def get(self, vat_id):
        return "a to vat {}".format(vat_id)

api.add_resource(Vats, '/vat')
api.add_resource(Vat, '/vat/<vat_id>')

app.core = NKF()
app.core.init()
if __name__ == "__main__":
    app.debug = True
    app.run()
