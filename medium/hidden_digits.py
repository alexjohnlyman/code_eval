# HIDDEN DIGITS
# In this challenge you're given a random string containing hidden and visible digits. 
# The digits are hidden behind lower case latin letters as follows: 0 is behind 'a', 1 is behind ' b ' etc., 9 is behind 'j'. 
# Any other symbol in the string means nothing and has to be ignored. 

# So the challenge is to find all visible and hidden digits in the string and print them out in order of their appearance.
# You may assume that there will be no white spaces inside the string.
# For each test case print out all visible and hidden digits in order of their appearance. 
# Print out NONE in case there is no digits in the string.

# INPUT SAMPLE:
# abcdefghik
# Xa,}A#5N}{xOBwYBHIlH,#W
# (ABW>'yy^'M{X-K}q,
# 6240488

# OUTPUT SAMPLE:
# 012345678
# 05
# NONE
# 6240488

# Testing
# import re

# my_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}

# def hidden(file):
# 	with open(file, 'r') as f:
# 		for line in f:
# 			string = list(re.sub("[^a-j0-9]+", '', line))
# 			for m,i in enumerate(string):
# 			    if i in my_dict:
# 			        string[m]=my_dict[i]
# 		        final_string = ''.join("{0}".format(n) for n in string)
# 		        if final_string == "":
# 		        	print "None"
# 	        	else:
# 	        		print final_string

# hidden('hiddendigits.txt')


# Final solution
# import sys
# import re
# my_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
# f = open(sys.argv[1], 'r')
# for line in f:
# 	string = list(re.sub("[^a-j0-9]+", '', line))
# 	for m,i in enumerate(string):
# 	    if i in my_dict:
# 	        string[m]=my_dict[i]
#         final_string = ''.join("{0}".format(n) for n in string)
#         if final_string == "":
#         	print "None"
#     	else:
#     		print final_string

