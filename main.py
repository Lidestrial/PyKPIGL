from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/first')
def hello():
    name = request.args.get("name", "World")
    num=24
    st='Chiki-briki'
    b=None
    return f'{num}, {st}, {b}
    return f'Sergey Ushakov, TI-71'
    
if __name__ == '__main__':
    app.run('0.0.0.0')
