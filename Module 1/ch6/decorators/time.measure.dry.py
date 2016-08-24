from time import sleep, time


def f():
    sleep(.3)

def g():
    sleep(.5)

def measure(func):
    t = time()
    func()
    print(func.__name__, 'took:', time() - t)

measure(f)  # f took: 0.30041074752807617
measure(g)  # g took: 0.5006198883056641
