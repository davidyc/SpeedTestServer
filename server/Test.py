import speedtestserviece

res = getUploadKB()
print("{} Kb/s".format(str(res)))
print("{} s".format(str(res/8)))
res = getDownloadKB()
print("{} Kb/s".format(str(res)))
print("{} s".format(str(res/8)))
res = getPing()
print("{} s".format(str(res)))

#res = getFullReport()
#print(res["download"], res["upload"], res["ping"])
