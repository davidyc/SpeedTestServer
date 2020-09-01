from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime


import speedtestserviece as st

app = Flask("Speed Test Server")

def getCurrentTimeSTR():
    now = datetime.now()
    return now.strftime("%d-%B-%Y %H:%M:%S")


@app.route('/')
def info():
    return render_template('main.html', name="Info API page")

@app.route('/ping', methods=['GET', 'POST'])
def ping():
    if request.method == 'POST':
        return "ALL DATA"
    ping = st.getPing()
    time = getCurrentTimeSTR()
    return { "Ping": ping, "Time stamp" : time}


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        return "ALL DATA"
    ping = st.getUploadKB()
    time = getCurrentTimeSTR()
    return { "Upload": ping, "Time stamp" : time}


app.run()