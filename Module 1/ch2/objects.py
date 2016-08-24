# objects.py

# code block # 1
>>> age = 42
>>> age
42
>>> age = 43  #A
>>> age
43


# code block # 2
>>> age = 42
>>> id(age)
10456352
>>> age = 43
>>> id(age)
10456384


# code block # 3
>>> class Person():
...     def __init__(self, age):
...         self.age = age
...
>>> fab = Person(age=39)
>>> fab.age
39
>>> id(fab)
139632387887456
>>> fab.age = 29  # I wish!
>>> id(fab)
139632387887456  # still the same id
