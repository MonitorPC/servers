import flask
from flask import render_template

app = flask.Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def train(prof):
    return render_template('in.html', prof=prof)


@app.router('/list_prof/<list>')
def lists(list):
    profs = ['инженер-иследователь', 'пилот',
             'строитель', 'экзобиолог', 'врач',
             'инженер по терреформированию',
             'климатолог',
             'специалист по радиоционной защите',
             'астрогеолог','гляциолог',
             'инженер жизнеобеспечения',
             'метеоролог','оператор марсохода',
             'кибер инженер','штурман',
             'пилот дронов']
    return render_template('im.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
