#!/usr/bin/python3
def weight_average(the_list=[]):
    if the_list and len(the_list):
        num = 0
        dem = 0
        for tup in the_list:
            num += (tup[0] * tup[1])
            dem += tup[1]
        return (num / dem)
    return 0
