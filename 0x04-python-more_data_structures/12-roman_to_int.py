#!/usr/bin/python3
def roman_to_int(roman_string):
    ns = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    h = 0
    tot = 0
    if isinstance(roman_string, str):
        for h in range(len(roman_string) - 1):
            if ns[roman_string[h]] >= ns[roman_string[h + 1]]:
                tot += ns[roman_string[h]]
            else:
                tot -= ns[roman_string[h]]
            h += 1
        tot += ns[roman_string[h]]
        return tot
    else:
        return 0
