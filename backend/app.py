import flask
from flask import Flask
from flask import request
from flask import url_for
import sqlite3
from flask import g
from flask import render_template
from flask import redirect
import os
import asyncio
import platform
import random
from machineLearning import userDataProcessed

path = ''
system = platform.system()
if system == 'Windows':
    path = os.environ["userprofile"]
    path += "\\Documents\\RAMDatabase\RAMdatabase.db"

if system == 'Darwin':
    path = os.path.expanduser('~/Documents')
    path += "/RAMDatabase/RAMdatabase.db"

DATABASE = path

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

async def getAll(dbName):
    return get_db().cursor().execute(f'select * from {dbName};').fetchall()

async def getOne(dbName, id):
    return get_db().cursor().execute(f'select * from {dbName} where id={id};').fetchone()

@app.route('/')
def hello_world():
    return 'Welcome to RAM BACKEND!'

@app.route('/tips/allTips')
def allTips():
    dataValue = asyncio.run(getAll('tips'))
    return flask.jsonify(dataValue)

@app.route('/tips/oneTip/<int:id>')
def oneTip(id):
    dataValue = asyncio.run(getOne('tips', int(id)))
    resultDict = {'id':dataValue[0], 'tip':dataValue[1]}
    return flask.jsonify(resultDict)

@app.route('/tips/randomTip')
def randomTip():
    dataValue = asyncio.run(getAll('tips'))
    randomValue = random.choice(dataValue)
    resultDict = {'id':randomValue[0], 'tip':randomValue[1]}
    return flask.jsonify(resultDict)

@app.route('/tips/create')
def createTip():
    return render_template('createTip.html')

@app.route('/tips/create/process', methods=['POST'])
def addTip():
    if request.method == 'POST':
        tip = request.form['tip']
        db_conn = get_db()
        db_conn.cursor().execute(f'insert into tips(TIP) values("{tip}");')
        db_conn.commit()
        return redirect('/tips/create')

@app.route('/goals/allGoals')
def allGoals():
    dataValue = asyncio.run(getAll('goals'))
    return flask.jsonify(dataValue)

@app.route('/goals/oneGoal/<int:id>')
def oneGoal(id):
    dataValue = asyncio.run(getOne('goals', int(id)))
    resultDict = {'id':dataValue[0], 'goal':dataValue[1]}
    return flask.jsonify(resultDict)

@app.route('/goals/randomGoal')
def randomGoal():
    dataValue = asyncio.run(getAll('goals'))
    randomValue = random.choice(dataValue)
    resultDict = {'id': randomValue[0], 'tip': randomValue[1]}
    return flask.jsonify(resultDict)

@app.route('/goals/suggestedGoals/<int:userID>')
def suggestedGoal(userID):
    pass

@app.route('/goals/create')
def createGoal():
    return render_template('createGoal.html')

@app.route('/goals/create/process', methods=['POST'])
def addGoal():
    if request.method == 'POST':
        goal = request.form['Goal']
        db_conn = get_db()
        db_conn.cursor().execute(f'insert into goals(GOAL) values("{goal}");')
        db_conn.commit()
        return redirect('/goals/create')

async def getCurrentUser(userID):
    return get_db().cursor().execute(f'select * from users where USERID="{userID}";').fetchone()

@app.route('/user/get/<string:userID>')
def getUser(userID):
    dataValue = asyncio.run(getCurrentUser(userID))
    resultDict = {'id':dataValue[0], 'userID':dataValue[1]}
    return flask.jsonify(resultDict)

@app.route('/user/add', methods=['GET','POST'])
def addUser():
    if request.method() == 'POST':
        userID = request.json['userID']
        # TODO : Add the user to the database when the POST request is made
        db_conn = get_db()
        db_conn.cursor().execute(f'insert into users(USERID) values("{userID}");')
        db_conn.commit()
        return "User added Successfully", 200
    else:
        return "The Route only accepts POST request", 400

@app.route('/questions/allQuestions')
def allQuestions():
    dataValue = asyncio.run(getAll('questions'))
    return flask.jsonify(dataValue)

@app.route('/questions/oneQuestion/<int:id>')
def oneQuestion(id):
    dataValue = asyncio.run(getOne('questions', int(id)))
    resultDict = {"id":dataValue[0], "question": dataValue[2]}
    return flask.jsonify(resultDict)

@app.route('/questions/randomQuestion')
def randomQuestion():
    dataValue = asyncio.run(getAll('questions'))
    randomValue = random.choice(dataValue)
    resultDict = {'id': randomValue[0], 'tip': randomValue[2]}
    return flask.jsonify(resultDict)

@app.route('/questions/create')
def createQuestion():
    return render_template('createQuestion.html')

@app.route('/questions/create/process', methods=['POST'])
def addQuestion():
    if request.method == 'POST':
        day = request.form['day']
        question = request.form['question']
        db_conn = get_db()
        db_conn.cursor().execute(f'insert into questions(DAY, QUESTION) values("{day}", "{question}");')
        db_conn.commit()
        return redirect('/questions/create')

count = 1

@app.route('/machineLearning', methods=['POST'])
def machineLearning():
    global count
    userData = request.json['userData']
    highestEmotion = asyncio.run(userDataProcessed(userData))
    newQuestion = asyncio.run(getOne('questions', count))
    if count == len(asyncio.run(getAll('questions'))):
        count = 1
    resultDict = {'emotion':highestEmotion, 'question':newQuestion[2]}
    count += 1
    return flask.jsonify(resultDict)

if __name__ == '__main__':
    app.run()
