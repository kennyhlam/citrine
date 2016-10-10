# -*- coding: utf-8 -*-

from flask import *
from conversion import *

app = Flask(__name__)

@app.route('/units/si')
def convert():
    try:
        units = request.args['units']
    except KeyError:
        abort(400)
    
    expr = parse(units)
    conversion_factor, si_units = get_value(expr)

    d = {
        'unit_name': stringify_expr(si_units),
        # format to 14 decimal places
        'multiplication_factor': float("{0:.14f}".format(conversion_factor))
    }
    return jsonify(**d)
