from flask import Flask
from flask import request
from flask import url_for
import sqlite3
from flask import g

DATABASE = '' # TODO: add path to the DATABASE

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/tips/allTips')
def allTips():
    return "AllTIps"

@app.route('/tips/oneTip/<int:id>')
def oneTip(id):
    pass

@app.route('/tips/randomTip')
def randomTip():
    pass

@app.route('/goals/allGoals')
def allGoals():
    pass

@app.route('/goals/oneGoal/<int:id>')
def oneGoal(id):
    pass

@app.route('/goals/randomGoal')
def randomGoal():
    pass

@app.route('/goals/suggestedGoals/<int:userID>')
def suggestedGoal(userID):
    pass

@app.route('/user/get/<int:userID>')
def getUser(userID):
    pass

@app.route('/user/add', methods=['GET','POST'])
def addUser():
    if request.method() == 'POST':
        return
    else:
        return

@app.route('/questions/allQuestions')
def allQuestions():
    pass

@app.route('/questions/oneQuestion/<int:day>')
def oneQuestion(day):
    pass

@app.route('/questions/randomQuestion')
def randomQuestion():
    pass

if __name__ == '__main__':
    app.run()
