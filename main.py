from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Sergey Ushakov, TI-71'

@app.route('/first')
def helloo():
    num=24
    st='Chiki-briki'
    b=None
    return f'{num}, {st}, {b}'

if __name__ == '__main__':
    app.run('0.0.0.0')
