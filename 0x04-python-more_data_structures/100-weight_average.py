#!/usr/bin/python3
def weight_average(the_list=[]):
    if the_list and len(the_list):
        no. = 0
        d = 0
        for tups in the_list:
            no. += (tups[0] * tups[1])
            d += tups[1]
        return (no. / d)
    return 0
