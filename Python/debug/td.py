import threading

def hello():
    print "hello, world"


def hello2():
    print "hello, world 2!"


t = threading.Timer(5, hello)
t1 = threading.Timer(2, hello2)
t.start()
t1.start()
