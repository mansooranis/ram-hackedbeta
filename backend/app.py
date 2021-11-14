import flask
from flask import Flask
from flask import request
from flask import url_for
import sqlite3
from flask import g
from flask import render_template
from flask import redirect
from flask_cors import CORS
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
CORS(app)

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
def index():
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
    dataValue = asyncio.run(getAll('goals'))
    randomValue = random.choices(dataValue, k=3)
    finalList = []
    for i in randomValue:
        resultDict = {'id': i[0], 'tip': i[1]}
        finalList.append(resultDict)
    return flask.jsonify(finalList)

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
    try:
        dataValue = asyncio.run(getCurrentUser(userID))
        resultDict = {'id':dataValue[0], 'userID':dataValue[1]}
        return flask.jsonify(resultDict)
    except:
        return "not user exists", 200

@app.route('/user/add', methods=['GET','POST'])
def addUser():
    if request.method() == 'POST':
        userID = request.json['userID']
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
        emotion = request.form['emotion']
        db_conn = get_db()
        db_conn.cursor().execute(f'insert into questions(DAY, QUESTION, EMOTION) values("{day}", "{question}", "{emotion}");')
        db_conn.commit()
        return redirect('/questions/create')

async def getlastUserInput(userID):
    return get_db().cursor().execute(f'select * from {userID} where ID=(select max(ID) from {userID});').fetchone()

async def getOneSpecQuestion(highestEmotion):
    return get_db().cursor().execute(f'select * from questions where EMOTION="{highestEmotion}";').fetchone()

@app.route('/machineLearning/<string:userID>')
def machineLearning(userID):
    getLastUserInput = asyncio.run(getlastUserInput(userID))
    highestEmotion = asyncio.run(userDataProcessed(getLastUserInput[2]))
    db_conn = get_db()
    db_conn.cursor().execute(f'update {userID} set EMOTION="{highestEmotion}" where id={getLastUserInput[0]};')
    db_conn.commit()
    newQuestion = asyncio.run(getOneSpecQuestion(highestEmotion))
    resultDict = {'question': newQuestion[2]}
    return flask.jsonify(resultDict)

@app.route('/getUserData', methods=['POST'])
def getUserData():
    if request.method == 'POST':
        userID = request.json['userID']
        db_conn = get_db()
        users = asyncio.run(getAll('users'))
        userIDRegisterd = []
        for i in range(len(users)):
            userIDRegisterd.append(users[i][1])
        if userID not in userIDRegisterd:
            userIDRegisterd.append(userID)
            db_conn.cursor().execute(f'create table if not exists {userID}(ID INTEGER PRIMARY KEY AUTOINCREMENT, QUESTION TEXT, ANSWER TEXT, EMOTION TEXT);')
            db_conn.cursor().execute(f'insert into users(USERID) values("{userID}");')
            db_conn.commit()
            return "User Added Successfully", 200
        else:
            userDBData = asyncio.run(getAll(userID))
            return flask.jsonify(userDBData)
    else:
        return "The Route only accepts POST request", 400

@app.route('/submitUserData/<string:userID>', methods=['POST'])
def submitUserData(userID):
    print(request.json)
    question = request.json['question']
    answer = request.json['answer']
    db_conn = get_db()
    db_conn.cursor().execute(f'insert into {userID}(QUESTION, ANSWER, EMOTION) values("{question}", "{answer}", "");')
    db_conn.commit()
    return "Data Added Successfully"

@app.route('/finalResult/<string:userID>')
def finalResult(userID):
    allTableVal = asyncio.run(getAll(userID))
    finalList = []
    for i in range(len(allTableVal)):
        newDict = {"id":allTableVal[i][0], "emotion":allTableVal[i][3]}
        finalList.append(newDict)
    return flask.jsonify(finalList)

if __name__ == '__main__':
    app.run()
