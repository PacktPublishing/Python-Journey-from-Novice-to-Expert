# -*- coding: utf-8 -*-


def calc_triples(mx):
    triples = []
    for a in range(1, mx + 1):
        for b in range(a, mx + 1):
            hypotenuse = calc_hypotenuse(a, b)
            if is_int(hypotenuse):
                triples.append((a, b, int(hypotenuse)))
    return triples


def calc_hypotenuse(a, b):
    return (a*a + b*b) ** .5


def is_int(n):  # n is expected to be a float
    return n.is_integer()


triples = calc_triples(1000)

"""
def calc_hypotenuse(a, b):
    return (a**2 + b**2) ** .5


$ python -m cProfile triples.py
1502538 function calls in 0.750 seconds

Ordered by: standard name

ncalls  tottime  percall filename:lineno(function)
500500    0.469    0.000 triples.py:14(calc_hypotenuse)
500500    0.087    0.000 triples.py:18(is_int)
     1    0.000    0.000 triples.py:4(<module>)
     1    0.163    0.163 triples.py:4(calc_triples)
     1    0.000    0.000 {built-in method exec}
  1034    0.000    0.000 {method 'append' of 'list' objects}
     1    0.000    0.000 {method 'disable' of '_lsprof.Profil...
500500    0.032    0.000 {method 'is_integer' of 'float' objects}
"""


"""
def calc_hypotenuse(a, b):
    return (a*a + b*b) ** .5


$ python -m cProfile triples.py
         1502538 function calls in 0.447 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   500500    0.179    0.000    0.179    0.000 triples.py:14(calc_hypotenuse)
   500500    0.084    0.000    0.113    0.000 triples.py:18(is_int)
        1    0.000    0.000    0.447    0.447 triples.py:4(<module>)
        1    0.155    0.155    0.447    0.447 triples.py:4(calc_triples)
        1    0.000    0.000    0.447    0.447 {built-in method exec}
     1034    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   500500    0.029    0.000    0.029    0.000 {method 'is_integer' of 'float' objects}
"""


"""
def is_int(n):
    return n == int(n)


$ python -m cProfile triples.py
         1002038 function calls in 0.466 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   500500    0.173    0.000    0.173    0.000 triples.py:14(calc_hypotenuse)
   500500    0.141    0.000    0.141    0.000 triples.py:18(is_int)
        1    0.000    0.000    0.466    0.466 triples.py:4(<module>)
        1    0.151    0.151    0.466    0.466 triples.py:4(calc_triples)
        1    0.000    0.000    0.466    0.466 {built-in method exec}
     1034    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
