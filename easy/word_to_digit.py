# Having a string representation of a set of numbers you need to print this numbers.
# All numbers are separated by semicolon. There are up to 20 numbers in one line.
# The numbers are "zero" to "nine".

# INPUT SAMPLE:
# zero;two;five;seven;eight;four
# three;seven;eight;nine;two
# two;nine;seven;one;four;six;five
# eight;nine;two;nine;seven;two;five;seven

# OUTPUT SAMPLE:
# 025784
# 37892
# 2971465
# 89297257

my_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}


# def replace(test):
# 	string = test.split(";")
# 	for m,i in enumerate(string):
# 	    if i in my_dict:
# 	        string[m]=my_dict[i]
#         print ''.join("{0}".format(n) for n in string)

# replace(test)

# Testing
def change(file):
	with open(file, 'r') as f:
		for line in f:
			no_return = line.rstrip('\n')
			string = no_return.split(";")
			for m,i in enumerate(string):
			    if i in my_dict:
			        string[m]=my_dict[i]
		        print ''.join("{0}".format(n) for n in string)

change('test_file.txt')


# Final solution
import sys

f = open(sys.argv[1], 'r')
my_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
for line in f:
	no_return = line.rstrip('\n')
	string = no_return.split(";")
	for m,i in enumerate(string):
	    if i in my_dict:
	        string[m]=my_dict[i]
        print ''.join("{0}".format(n) for n in string)
