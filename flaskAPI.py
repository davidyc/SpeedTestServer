from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
import uuid
import speedtestserviece as st
import dcconnection as db

app = Flask("Speed Test Server")
dbname = "SpeedTest"

def getCurrentTimeSTR():
    now = datetime.now()
    return now.strftime("%d-%B-%Y %H:%M:%S")

def createJSONResponse(typeReq, value, guid = None):
    d = dict()
    if guid == None:
        guid = (str(uuid.uuid4()))
    time = getCurrentTimeSTR()
    d["key"] = guid
    d["time"] = time
    d["type"] = typeReq
    d["value"] = value
    return d

@app.route('/')
def info():
    return render_template('main.html', name="Info API page")

@app.route('/ping', methods=['GET', 'POST'])
def ping():
    if request.method == 'POST':
        req_body = request.get_json(silent=True)
        if req_body == None:
            key = None
        else:
            key = req_body['key']
        value = st.getPing()
        dictData = createJSONResponse("ping", value, key)
        return dictData
    return db.getallrowbytype(dbname,"ping")

@app.route('/ping/<key>', methods=['GET'])
def pingByKey(key):
    return db.getallrowbykey(dbname,"ping", key)


db.initTable(dbname)
app.run()