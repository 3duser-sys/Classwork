"GET OUT! (exit program)"
import time
n = 10
for i in range(10):
    if n > 0:
        print(".", "\n")
        time.sleep(0.2)
        n = n-1
    elif n < 0:
        print("Shutting Down...")
        time.sleep(1)
        exit()
