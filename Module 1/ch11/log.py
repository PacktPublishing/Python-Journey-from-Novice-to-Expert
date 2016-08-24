import logging

logging.basicConfig(
    filename='ch11.log',
    level=logging.DEBUG,  # minimum level capture in the file
    format='[%(asctime)s] %(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p')

mylist = [1, 2, 3]
logging.info('Starting to process `mylist`...')

for position in range(4):
    try:
        logging.debug('Value at position {} is {}'.format(
            position, mylist[position]))
    except IndexError:
        logging.exception('Faulty position: {}'.format(position))

logging.info('Done parsing `mylist`.')


""" ch11.log
[10/08/2015 04:25:59 PM] INFO:Starting to process `mylist`...
[10/08/2015 04:25:59 PM] DEBUG:Value at position 0 is 1
[10/08/2015 04:25:59 PM] DEBUG:Value at position 1 is 2
[10/08/2015 04:25:59 PM] DEBUG:Value at position 2 is 3
[10/08/2015 04:25:59 PM] ERROR:Faulty position: 3
Traceback (most recent call last):
  File "log.py", line 15, in <module>
    position, mylist[position]))
IndexError: list index out of range
[10/08/2015 04:25:59 PM] INFO:Done parsing `mylist`.
"""
