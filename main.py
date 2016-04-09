#!/usr/bin/python

import sys

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
# t = int(raw_input())  # read a line with a single integer
# for i in xrange(1, t + 1):
#   n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
#   print "Case #{}: {} {}".format(i, n + m, n * m)
#   # check out .format's specification for more formatting options

# with open('qualifiers/primes.raw', 'r') as f:
#     data = f.read().split()
#     # print set(data.split())
#     file_output = 'primes = {}'.format(data).replace('[', '{').replace(']', '}')
#     output = open('output.dat', 'w')
#     output.write(file_output)
# f.close()


digits = 16
needed_coins = 50
between_digits = int(digits) - 2
end = int('1'*between_digits, base=2)
possibles = []
for i in range(0, end+1):
    between_string = format(bin(i)[2:]).zfill(between_digits)
    possible_coin = '1' + between_string + '1'
    possibles.append(possible_coin)

file_output = 'possibles = {}'.format(possibles)
output = open('qualifiers/possibles.py', 'w')
output.write(file_output)
