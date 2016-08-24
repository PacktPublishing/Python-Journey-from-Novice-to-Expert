# d comes from a JSON payload we don't control
d = {'first': 'v1', 'second': 'v2', 'fourth': 'v4'}
# keys also comes from a JSON payload we don't control
keys = ('first', 'second', 'third', 'fourth')

def do_something_with_value(value):
    print(value)

import ipdb
ipdb.set_trace()  # we place a breakpoint here

for key in keys:
    do_something_with_value(d[key])

print('Validation done.')


"""
$ python ipdebugger_ipdb.py
> /home/fab/srv/l.p/ch11/ipdebugger_ipdb.py(12)<module>()
     11
---> 12 for key in keys:  # this is where the breakpoint comes
     13     do_something_with_value(d[key])

ipdb> keys  # let's inspect the keys tuple
('first', 'second', 'third', 'fourth')
ipdb> !d.keys()  # now the keys of d
dict_keys(['first', 'fourth', 'second'])  # we miss 'third'
ipdb> !d['third'] = 'something dark side...'  # let's put it in
ipdb> c  # ... and continue
v1
v2
something dark side...
v4
Validation done.
"""
