#! /usr/bin/env python
from queue import Queue
import logging

# Create logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
log = logging.getLogger()

# dictionary
dictionary = {
        'place': 'Chicago',
        'date': 'Dec 3'
        }

# List
L = [1, 5, 45, 7, 834]

# tuple
tup = (1, 5, 45, 7, 834)

# strings
my_string = "This is a tutorial"

# char
my_char = "a" # I am just a string with one character

# stacks
# queues
q = Queue("imported")

# Python coding conventions - Read up on PEP-8
# variable names / function names usually all small and _ separated
# contanst = ALL CAPS
# Class name - camel case Ex: class CamelCase(object):


def list_iterate_and_print(input_list):
    """ This function gives examples of list iterations """
    for val in input_list:
        print val

    for i in range(len(input_list)):
        print i, input_list[i]

    for i, val in enumerate(input_list):
        print i, val


def dictionary_iteration(input_dict):
    # >>> ["{} = {}".format(k, v) for k, v in dict.items()]
    # ['date = dec3', 'place = chicago']
    for k, v in dictionary.items():
        print k, "=", v

def dict_ret_keys(input_dict):
    return input_dict.keys()

def dict_ret_keyandvalue(input_dict):
    return input_dict.keys(), input_dict.values()

def list_comprehension(in_list, in_dict):
    out_list = ["Rs {}".format(val) for val in in_list]
    out_dict_list = ["{} = {}".format(k, v) for k,v in in_dict.items()]
    print out_list
    print out_dict_list

if __name__ == '__main__':
    list_iterate_and_print(L)
    dict_ret_keys(dictionary)
    q.push(1)
    q.push(2)
    q.push(3)
    print q
    q.pop()
    print q

    # Try except example
    # THis is really BAAD practice
    log.warning("I am parsing string as an int. This could be bad")
    try:
       int("asagsdgd")
    except Exception as err:
        log.error("something happend and it was bad: {}".format(err))

    log.warning("Trying this again with specific exception")
    try:
       int("asagsdgd")
       print dictionary['kiran']
    except KeyError:
        log.error("We had a key error")
    except ValueError:
        log.error("We had a int parsing error")

    # Example of key error and nested exception catching
    try:
       print dictionary['kiran']
    except KeyError:
        log.error("We had a key error")
    except ValueError:
        log.error("We had a int parsing error")

    # Example to print an actual error
    try:
       print dictionary['kiran']
    except KeyError as err:
        log.error("We had a key error: {}".format(err))
    except ValueError as err:
        log.error("We had a int parsing error: {}".format(err))

    # When do you use exceptions
    # case 1: External apis are not reliable


## Exercise
# Read: Binary search and implement in python
# Write a class for stacks
