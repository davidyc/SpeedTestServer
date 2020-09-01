from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
import uuid
import speedtestserviece as st

app = Flask("Speed Test Server")

def getCurrentTimeSTR():
    now = datetime.now()
    return now.strftime("%d-%B-%Y %H:%M:%S")

def createJSONResponse(typeReq, value, guid = None):
    d = dict()
    if guid == None:
        guid = (str(uuid.uuid4()))
    time = getCurrentTimeSTR()
    d["ID"] = guid
    d["Time stamp"] = time
    d["Type"] = typeReq
    d["Value"] = value
    return d

@app.route('/')
def info():
    return render_template('main.html', name="Info API page")

@app.route('/ping', methods=['GET', 'POST'])
def ping():
    print(request.args)
    if request.method == 'POST':
        value = st.getPing()
        dictData = createJSONResponse("Ping", value)
        return dictData
    data = dict()
    data['Data'] = "Data"
    return data

app.run()