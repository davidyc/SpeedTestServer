import speedtest

def initObject():
    return speedtest.Speedtest()

def getUploadKB():
    st = initObject()
    bytespersec = st.upload()
    return bytespersec/1000

def getDownloadKB():
    st = initObject()
    bytespersec = st.download()
    return bytespersec/1000

def getPing():
    st = initObject()
    bytespersec = st.get_best_server()
    res = st.results.dict()
    return res["ping"]

def getFullReport():
    st = initObject()
    st.get_best_server()
    st.download()
    st.upload()
    return st.results.dict()


