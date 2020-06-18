from pip._vendor.distlib.compat import raw_input


def get0():
    print (0)
def get1():
    print (1)
def get2():
    print (2)
def get3():
    print (3)

dict = {0:get0, 1:get1, 2:get2, 3:get3}

while True:
    n = raw_input()
    i = int(n) % 10
    dict[i]()
