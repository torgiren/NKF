#!/usr/bin/env python
import os
import glob
import json
import jsonschema
from jsonschema import validate
schemas = glob.glob('*schema*')
for i in schemas:
    j = i.replace("schema","example")
    if os.path.isfile(i) and os.path.isfile(j):
        print(i + ":\t "),
        try:
            s = json.load(open(i))
            validate(json.load(open(j)), json.load(open(i)))
            print("OK")
        except ValueError as e:
            print("Skladnia: " + str(e))
        except jsonschema.exceptions.ValidationError as e:
            print("Validacja: " + str(e))
    else:
        print("{}:\t no example".format(i))
