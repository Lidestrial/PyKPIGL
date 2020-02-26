# @SEENPAY
from flask import Flask, escape, request,render_template
app = Flask(__name__)

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
        return render_template('index.html')
    if request.method == 'POST':
        test = request.form.get('text')
        print(test)
     
        rev = [a for a in reversed(test)] 
        lst=request.form.get('text')
        return f'{lst[::-1]} {list(reversed(lst))}, {rev}\n'


    
    # lst=request.form.get("text")
    # return f'{reverse(lst)}\n'

# # def reverse3():
# #     lst=request.form.get("text")
# #     return f'{[ for i in lst.reversed]}\n'

if __name__ == '__main__':
    app.run('0.0.0.0')
