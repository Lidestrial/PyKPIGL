# @SEENPAY
from flask import Flask, request, render_template
from classes.deck import Deck
from classes.farm import Farm
from flask_sqlalchemy import SQLAlchemy
import requests
from helpers import get_env_variable
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

#from helpers import get_env_variable

app = Flask(__name__)
deck = Deck()
farms = {}

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') #'postgres://ltgmovdvngewsc:c0ebb22749d43cf607977435a2454713eced2a89a5ee703bdc939081aee0ed58@ec2-3-222-30-53.compute-1.amazonaws.com:5432/d3qts4a8o2lf4p'
app.config['DATABASE_URL'] =  get_env_variable('DATABASE_URL') #'postgres://ltgmovdvngewsc:c0ebb22749d43cf607977435a2454713eced2a89a5ee703bdc939081aee0ed58@ec2-3-222-30-53.compute-1.amazonaws.com:5432/d3qts4a8o2lf4p'


db = SQLAlchemy(app)
migrate = Migrate(app, db)

#manager = Manager(app)
#manager.add_command('db', MigrateCommand)

class DBFarm(db.Model):
    __tablename__ = 'Farm'

    id = db.Column(db.Integer, primary_key=True)
    farm_name = db.Column(db.String(80), unique=True, nullable=False)
    squares = db.Column(db.Integer, unique=False, nullable=True)
    sheeps = db.Column(db.Integer, unique=False, nullable=True)
    cows = db.Column(db.Integer, unique=False, nullable=True)
    cheeks = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return f'{self.farm_name, self.squares, self.sheeps, self.cows, self.cheeks}'


def get_farms():
    rows = DBFarm.query.all()
    result = {}
    for row in rows:
        farm = Farm(row.farm_name, row.squares, row.sheeps, row.cows, row.cheeks)
        result[row.farm_name]=farm
    return result


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Sergey Ushakov, TI-71'


@app.route('/first')
def first():
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
        if not check % 2 and ' ' + ' ' not in str1:  # or '  ' not in str1
            result = True
        else:
            result = False
        return render_template('./fourth2.html', content=result)


@app.route('/fifth', methods=['GET', 'POST'])
def fifth():
    if request.method == 'GET':
        return render_template('./fifth.html')
    if request.method == 'POST':
        users = request.form.get('text4')
        res = requests.get(f'https://api.github.com/users/{users}')
        if res.status_code == 404:
            warning = "Person abandon"
            return render_template("fifth.html", warning=warning)
        avatar = res.json()['avatar_url']
        return render_template("./fifth.html", content=avatar)


@app.route('/sixth', methods=['GET', 'POST'])
def sixth():
    if request.method == 'GET':

        farms = get_farms()

        print(farms)
        return render_template('./sixths.html', content=farms)
    if request.method == 'POST':
        # print(request.form)

        if 'name' in request.form:
            try:

                new_farm = DBFarm(farm_name=request.form['name'], squares=int(request.form['square'] or 0),
                                  sheeps=int(request.form['sheeps'] or 0), cows=int(request.form['cows'] or 0),
                                  cheeks=int(request.form['chicks'] or 0))
                db.session.add(new_farm)
                db.session.commit()
                message = "Farm Created"
            except ValueError:
                message = "Enter valid input!(nums)"
                db.session.rollback()
            except:
                db.session.rollback()
                raise

        farms = get_farms()

        print(farms)

        try:
            if 'f1' in request.form:
                f1 = request.form['f1']
                f2 = request.form['f2']
                if farms[f1] > farms[f2]:
                    message = f'{f1} more pricey than {f2}'
                elif farms[f1] < farms[f2]:
                    message = f'{f2} more pricey than {f1}'
                elif farms[f1] == farms[f2]:
                    message = 'farms are equal ❤'
        except KeyError:
            message = 'Farm does not exist'
        return render_template('./sixths.html', content=farms, message=message)
        
        
@app.route('/seventh')
def seventh():
    return f'farm attached to db'


if __name__ == '__main__':
    app.run('0.0.0.0')
