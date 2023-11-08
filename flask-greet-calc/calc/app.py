from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add():
    ''' add a and b '''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)

    return str(result)

@app.route('/sub')
def sub():
    ''' subtract a - b '''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)

    return str(result)

@app.route('/mult')
def mult():
    ''' multiply a and b '''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)

    return str(result)

@app.route('/div')
def div():
    ''' divide a and b '''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)

    return str(result)

operators = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div,
}

@app.route('/math/<oper>')
def do_math(oper):
    ''' do math to a and b '''

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operators[oper](a, b)

    return str(result)
