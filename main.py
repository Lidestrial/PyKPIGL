from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Sergey Ushakov, TI-71'

@app.route('/first')
def helloo():
    chpek = None
    num = 54
    damki = 'chikibriki'
    return f'{chpek}, {num}, {damki}'

if __name__ == '__main__':
    app.run('0.0.0.0')
