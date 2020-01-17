from operator import itemgetter
from backend.piazzaAPI import *
from backend.backend.freqdist import *
from collections import OrderedDict


def sort(email, password, coursecode, cutoff=30):
    dictionary = raw_dict_maker(piazza_reader(email, password, coursecode))
    if len(dictionary) <= cutoff:
        sort_dictionary = sorted(dictionary.items(), key=itemgetter(1))
        return list(reversed(sort_dictionary))
    else:
        sort_dictionary = sorted(dictionary.items(), key=itemgetter(1))
        new_dictionary = list(reversed(sort_dictionary))[:cutoff]
        return new_dictionary

print(sort('kevinpkf311@gmail.com', 'pkf88063302', 'MATH 253.ALL'))