# @SEENPAY
from flask import Flask, escape, request, render_template
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


@app.route('/second', methods=['GET', 'POST'])
def second():
    if request.method == 'GET':
        return render_template('second.html')
    if request.method == 'POST':
        lst = request.form.get('text')
        comprehension = "".join([a for a in reversed(lst)])
        rev = "".join(list(reversed(lst)))
        sl = "".join(lst[::-1])
        # 
        return f'{comprehension}<br> {rev}<br> {sl}\n'


@app.route('/third', methods=['GET', 'POST'])
def third():
    if request.method == 'GET':
        return render_template('./third.html')
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


@app.route('/fourth/1', methods=['GET', 'POST'])
def fourth1():
    if request.method == 'GET':
        return render_template('./fourth.html')
    if request.method == 'POST':
        input1 = int(request.form.get('text1'))
        input2 = int(request.form.get('text2'))
        lst = range(input1, input2)
        result = []
        result = list(filter(lambda x: x % 3 == 0, lst))
        return render_template('./fourth.html', content=result)


@app.route('/fourth/2', methods=['GET', 'POST'])
def fourth2():
    if request.method == 'GET':
        return render_template('./fourth2.html')
    if request.method == 'POST':
        result = []
        str1 = str(request.form.get('text3'))
        check = len(str1)
        if check % 2 == 0 and ' ' + ' ' not in str1:  # or '  ' not in str1
            result = True
        else:
            result = False
        return render_template('./fourth2.html', content=result)


if __name__ == '__main__':
    app.run('0.0.0.0')
