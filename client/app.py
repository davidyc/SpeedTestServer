from flask import Flask
from flask import render_template
from flask import request
import ai

app = Flask("Speed Test Client")
infomess = 'Item was added to queue with intervat {} and repeat {} times'

@app.route('/', methods=['post', 'get'])
def setserver():
    message = 'Add test to queue'
    if request.method == 'POST':
        count = request.form.get('count')
        interval = request.form.get('interval')
        keyid = request.form.get('keyid')
        typereq = request.form.get('type')
        url = request.form.get('url')
        if count == None or int(count) < 1:
            count = 1
        if interval == None or int(interval) < 1:
            interval = 0
        ai.execute(count,int(interval)*60, url, typereq, keyid)
        return render_template('result.html', message=infomess.format(interval, count))
    return render_template('main.html', message=message)


app.run(host='0.0.0.0')