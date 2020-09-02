import mariadb
import json

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'password',
    'database': 'TestSpeedFlask'
}

conn = mariadb.connect(**config)
cur = conn.cursor()
_keyid = "keyid"
_dateandtime = "dateandtime"
_typetest = "typetest"
_valuetest = "valuetest"


def initTable(dbname):
    try:
        cur.execute("CREATE TABLE {} ({} VARCHAR(50), {} VARCHAR(45),{} VARCHAR(15), {} VARCHAR(45))"
        .format(dbname, _keyid,_dateandtime,_typetest,_valuetest))
    except Exception as e:
        print(str(e))

def getallrowbytype(dbname, typetest):
    cur.execute("select * from {} where {} = '{}'".format(dbname, _typetest, typetest))
    return _getjsonresponse(cur)

def getallrowbykey(dbname, typetest, keyid):
    cur.execute("select * from {} where {} = '{}' and {} = '{}'"
    .format(dbname, _keyid, keyid, _typetest, typetest))
    return _getjsonresponse(cur)

def addnewrow(dbname,keyid, timecurrent, typetest, value):
    sql = "INSERT INTO {} ({}, {}, {}, {}) VALUES (%s, %s, %s, %s)".format(dbname, _keyid, _dateandtime, _typetest, _valuetest)
    val = (keyid, timecurrent, typetest, value)
    cur.execute(sql, val)
    conn.commit()

def _getjsonresponse(cursor):
    row_headers=[x[0] for x in cursor.description]
    rv = cursor.fetchall()
    rows =[]
    for row in rv:
        rows += [{_keyid:row[0], _dateandtime:row[1], _typetest:row[2], _valuetest:row[3]}]
    return json.dumps(rows, sort_keys=True, indent=4, separators=(',', ': '))