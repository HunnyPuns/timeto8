#!/usr/bin/env python3

import argparse
import sys

class calculatx0r(object):

    def _permutations_(self):
        #permutations in an 8 character password using the following requirements:
        #8 characters
        #At least 1 upper case character
        #At least 1 lower case character
        #At least 1 special character
        #Defined in this Stack Exchange:
        #https://math.stackexchange.com/questions/739874/how-many-possible-combinations-in-8-character-password

        permutations = 3025989069143040

        return permutations

    def calculate(self, hashrate):
        myperms = self._permutations_()

        seconds = int(myperms) / int(hashrate)

        return seconds


calcparse = argparse.ArgumentParser()
calcparse.add_argument('-H', '--hashrate', required=True, type=int)

args = calcparse.parse_args(sys.argv[1:])

calc = calculatx0r()

seconds = calc.calculate(args.hashrate)
minutes = seconds / 60
hours = minutes / 60
days = hours / 24

if(hours < 10):
    print("minutes to run through all permutations of a standard 8 character password: %s" % (minutes))

print("hours to run through all permutations of a standard 8 character password: %s" % (hours))
print("days to run through all permutations of a standard 8 character password: %s" %(days))

if(days > 365):
    print("years to run through all permutations of a standard 8 character password: %s" % (days / 365))
