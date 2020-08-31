import speedtest


st = speedtest.Speedtest()
#st.get_best_server()
#st.download()
st.upload()

res = st.results.dict()
#print(res["download"], res["upload"], res["ping"])
print(type(res["upload"]))
print(res["upload"]/1024)
