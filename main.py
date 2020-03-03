# @SEENPAY
from flask import Flask, escape, request,render_template
from deck import Deck

app = Flask(__name__)
deck = Deck()

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Sergey Ushakov, TI-71'

@app.route('/first')
def helloo():
    chpek = None
    num = 42
    damki = 'chiki-briki'
    return f'{chpek}, {num}, {damki}'

@app.route('/second', methods=['GET','POST'])
def second():
    if  request.method == 'GET':
        return render_template('second.html')
    if request.method == 'POST':

        lst=request.form.get('text')
        comprehension  = "".join([a for a in reversed(lst)]) 
        rev ="".join(list(reversed(lst)))
        sl ="".join(lst[::-1])
        # 
        return f'{comprehension}<br> {rev}<br> {sl}\n'

@app.route('/third', methods=['GET','POST'])
def third():
    if  request.method == 'GET':
        return render_template('./third.html',content='\u0020',  deck=str(deck))
    if request.method == 'POST':
        if "shuffle" in request.form:
            deck.shuffle()
            message = "Deck was shuffled"
        elif "pop" in request.form:
            message = deck.pop()
        elif "get_random" in request.form:
            message = deck.get_random()
        else:
            num = request.form.get("index")
            message = deck.index(num)
        return render_template('third.html', content=message, deck=str(deck))


if __name__ == '__main__':
    app.run('0.0.0.0')
