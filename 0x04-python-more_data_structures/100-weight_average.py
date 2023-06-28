#!/usr/bin/python3
def weight_average(the_list=[]):
    if the_list and len(the_list):
        no. = 0
        d = 0
        for t in the_list:
            no. += (t[0] * t[1])
            d += t[1]
        return (no. / d)
    return 0
