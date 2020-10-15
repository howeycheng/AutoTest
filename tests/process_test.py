from multiprocessing import Process
import os
import time
def test():
    while True:
        print()
        time.sleep(1)
        print(1)


print(Process.pid)
p1 = Process(target=test)
p1.start()
while True:
    time.sleep(1)
    print(2)
print(Process.pid)
