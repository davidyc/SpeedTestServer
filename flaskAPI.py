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

def createJSONResponse(guid, time, typeReq, value):
    d = dict()
    time = getCurrentTimeSTR()
    d["keyid"] = guid
    d["dateandtime"] = time
    d["typetest"] = typeReq
    d["valuetest"] = value
    return d

@app.route('/')
def info():
    return render_template('main.html', name="Info API page")

@app.route('/ping', methods=['GET', 'POST'])
def ping():
    if request.method == 'POST':
        req_body = request.get_json(silent=True)
        if req_body == None:
            key = (str(uuid.uuid4()))
        else:
            key = req_body['keyid']
        time =getCurrentTimeSTR()
        value = st.getPing()
        db.addnewrow(dbname, key, time, "ping", value)
        dictData = createJSONResponse(key, time, "ping", value)
        return dictData
    return db.getallrowbytype(dbname,"ping")

@app.route('/ping/<key>', methods=['GET'])
def pingByKey(key):
    return db.getallrowbykey(dbname,"ping", key)

@app.route('/download', methods=['GET', 'POST'])
def dowmload():
    if request.method == 'POST':
        req_body = request.get_json(silent=True)
        if req_body == None:
            key = (str(uuid.uuid4()))
        else:
            key = req_body['keyid']
        time =getCurrentTimeSTR()
        value = st.getDownloadKB()
        db.addnewrow(dbname, key, time, "download", value)
        dictData = createJSONResponse(key, time, "download", value)
        return dictData
    return db.getallrowbytype(dbname,"download")

@app.route('/download/<key>', methods=['GET'])
def dowmloadByKey(key):
    return db.getallrowbykey(dbname,"download", key)


db.initTable(dbname)
app.run()