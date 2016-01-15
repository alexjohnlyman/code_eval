# TRY TO SOLVE IT
# The word can include from 2 to 40 symbols.
# All letters are lowercase.

# INPUT SAMPLE:
# mke
# mh
# lhsby
# pm

# OUTPUT SAMPLE:
# try
# to
# solve
# it

# Testing
import re
my_dict = {'a':'u', 'b':'v', 'c':'w', 'd':'x', 'e':'y', 'f':'z', 'g':'n', 'h':'o', 'i':'p', 'j':'q', 'k':'r', 'l':'s', 'm':'t', 'n':'g', 'o':'h', 'p':'i', 'q':'j', 'r':'k', 's':'l', 't':'m', 'u':'a', 'v':'b', 'w':'c', 'x':'d', 'y':'e', 'z':'f'}

def solve(file):
	with open(file, 'r') as f:
		for line in f:
			string = list(re.sub("[^a-z]+", '', line))
			for m,i in enumerate(string):
				if i in my_dict:
					string[m]=my_dict[i]
		        print ''.join("{0}".format(n) for n in string)

solve('solveit.txt')


# Final solution
import sys
import re
my_dict = {'a':'u', 'b':'v', 'c':'w', 'd':'x', 'e':'y', 'f':'z', 'g':'n', 'h':'o', 'i':'p', 'j':'q', 'k':'r', 'l':'s', 'm':'t', 'n':'g', 'o':'h', 'p':'i', 'q':'j', 'r':'k', 's':'l', 't':'m', 'u':'a', 'v':'b', 'w':'c', 'x':'d', 'y':'e', 'z':'f'}
f = open(sys.argv[1], 'r')
for line in f:
	string = list(re.sub("[^a-z]+", '', line))
	for m,i in enumerate(string):
		if i in my_dict:
			string[m]=my_dict[i]
        print ''.join("{0}".format(n) for n in string)

