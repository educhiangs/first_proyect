import time
import os
import pandas
while True:
    if os.path.exists("files/temps_today.csv"):
            data = pandas.read_csv("files/temps_today.csv")
            print(data.mean()["st1"])
    else:
        print("file doesn't exist")
    time.sleep(10)
# hora_local = time.localtime()
# result = time.strftime("%H:%M:%S", hora_local)
# print(result)
