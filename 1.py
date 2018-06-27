print("Question1")
import time
import threading
class Thread1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        time.sleep(5)
        print("Thread is awake now.")
th1=Thread1()
th1.start()
print('*'*10)
print('\n')

print("Question2")
import time
import threading
class Thread2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1,11):
            print(i)
            time.sleep(1)
th2=Thread2()
th2.start()
print('*'*10)
print('\n')

print("Question3")
import time
import threading
class Thread3(threading.Thread):
    def __init__(self,d):
        threading.Thread.__init__(self)
        self.d=d
    def run(self):
        for i in l:
            delay=2*self.d
            time.sleep(delay)
            print(i)
            self.d=self.d+1
l=[6,6,23,3,2]
d=1
th3=Thread3(d)
th3.start()
print('*'*10)
print('\n')

print("Question4")
import threading
import math

class Thread4(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num
    def run(self):
        temp = math.factorial(self.num)
        print("%s: calculate %d's factorial is %d" %(self.name,self.num,temp))
num=int(input("Enter number: "))
th4=Thread4(num)
th4.start()

