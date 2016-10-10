from flask import *
app = Flask(__name__)

def parse(units):
    expr_array = []
    for i in units.split('*'):
        for j in i.split('/'):
            for k in i.split('('):
                for l in k.split(')'):
                    expr_array.append(l)
    return expr_array

@app.route('/units/si')
def convert():
    try:
        units = request.args['units']
    except KeyError:
        abort(400)
    
    expr = parse(units)

    converted_units = 1
    mult_factor = 1
    d = {
        'unit_name': expr,
        'multiplication_factor': mult_factor
    }
    return jsonify(**d)
