import time
start = 11

for _ in range(10):
    start = start-1
    if start == 5:
        continue
    else:
        print(start)
        time.sleep(0.3)