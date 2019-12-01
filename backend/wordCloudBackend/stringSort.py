from operator import itemgetter
from collections import OrderedDict


def sort(dictionary, cutoff):
    if len(dictionary) <= cutoff:
        sort_dictionary = sorted(dictionary.items(), key=itemgetter(1))
        return list(reversed(sort_dictionary))
    else:
        sort_dictionary = sorted(dictionary.items(), key=itemgetter(1))
        new_dictionary = list(reversed(sort_dictionary))[:cutoff]
        return new_dictionary

