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


def initTable(dbname):
    try:
        cur.execute("CREATE TABLE {} (keyid VARCHAR(50), dateandtime VARCHAR(45),  typetest VARCHAR(15), valuetest VARCHAR(45))".format(dbname))
    except Exception as e:
        print(str(e))

def getallrowbytype(dbname, typetest):
    cur.execute("select * from {} where typetest = '{}'".format(dbname, typetest))
    row_headers=[x[0] for x in cur.description]
    rv = cur.fetchall()
    rows =[]
    for row in rv:
        rows += [{"keyid":row[0], "dateandtime":row[1], "typetest":row[2], "valuetest":row[3]}]
    return json.dumps(rows, sort_keys=True, indent=4, separators=(',', ': '))

def getallrowbykey(dbname, typetest, keyid):
    cur.execute("select * from {} where keyid = '{}' and typetest = '{}' ".format(dbname, keyid, typetest))
    row_headers=[x[0] for x in cur.description]
    rv = cur.fetchall()
    rows =[]
    for row in rv:
        rows += [{"keyid":row[0], "dateandtime":row[1], "typetest":row[2], "valuetest":row[3]}]
    return json.dumps(rows, separators=(',', ': '))