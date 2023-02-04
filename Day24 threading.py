import threading
print("Current Executing Thread:",threading.current_thread().name)

from threading import *
def display():
    for i in range(1,11):
        print("Child Thread")

t=Thread(target=display)
t.start()

for i in range(1,11):
    print("Main Thread")

from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("Child Thread-1")

t=MyThread()
t.start()
for i in range(10):
    print("Main Thread-1")


from threading import *
class Test:
    def display(self):
        for i in range(10):
            print("Child Thread-2")

obj=Test()
t=Thread(target=obj.display)
t.start()
for i in range(10):
    print("Main Thread-2")

