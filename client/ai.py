import requests
import time

def _setdelay(interval):
    time.sleep(interval)

def execute(count, interval, url, ping, keyid):
    i = 1
    s = url + '/' + ping
    while True:
        requests.post(s, json={"keyid":keyid})
        if i >= int(count):
            break
        _setdelay(int(interval))
        i += 1


