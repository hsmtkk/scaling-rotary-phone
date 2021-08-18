import time
import socket

while True:
    host = socket.gethostname()
    date = time.strftime("%Y-%m-%d %H:%M:%S")
    now = str(date)
    with open("date.out", "a") as f:
        print(now, file=f)
        print(host, file=f)
    time.sleep(5)