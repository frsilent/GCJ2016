#!/usr/bin/python

import sys
print sys.argv[1]

class TestCase():
    pass

with open(sys.argv[1], 'r') as f:
    test_cases = int(f.readline())
    print test_cases
    for i in xrange(0, test_cases):
        shy = {}
        test = f.readline()
        shy_max = test[0]
        print "Case #{}: {}", i, 1

f.close()
"""
The first line of the input gives the number of test cases, T.
T test cases follow. Each consists of one line with Smax,
the maximum shyness level of the shyest person in the audience,
followed by a string of Smax + 1 single digits. The kth digit of this
string (counting starting from 0) represents how many people in the
audience have shyness level k. For example, the string "409" would mean
that there were four audience members with Si = 0 and nine audience
members with Si = 2 (and none with Si = 1 or any other value). Note that
there will initially always be between 0 and 9 people with each shyness level.

The string will never end in a 0. Note that this implies that there will always be at least one person in the audience.

Output

For each test case, output one line containing "Case #x: y", where x is the
test case number (starting from 1) and y is the minimum number of friends you must invite.
"""
