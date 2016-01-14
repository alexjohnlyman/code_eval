# N MOD M
# Given two integers N and M, calculate N Mod M (without using any inbuilt modulus operator).

# INPUT SAMPLE:
# 20,6
# 2,3

# Your program should accept as its first argument a path to a filename. Each line in this file contains two comma separated positive integers. You may assume M will never be zero.
# Print out the value of N Mod M

# OUTPUT SAMPLE:
# 2
# 0

# Testing
def n_mod_m(file):
    with open(file, 'r') as f:
        for line in f:
        	numbers = line.rstrip()
        	numbers = numbers.split(",")
        	num_1 = int(numbers[0])
        	num_2 = int(numbers[1])
	    	if num_2 < num_1:
	    		print num_1 - (num_2 * (num_1 / num_2))
	    	else:
	    		print num_1

n_mod_m("nmodm.txt")



# Final solution
# import sys

# f = open(sys.argv[1], 'r')
# for line in f:
# 	numbers = line.rstrip()
# 	numbers = numbers.split(",")
# 	num_1 = int(numbers[0])
# 	num_2 = int(numbers[1])
# 	if num_2 < num_1:
# 		print num_1 - (num_2 * (num_1 / num_2))
# 	else:
# 		print num_1
