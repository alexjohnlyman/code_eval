# TESTING
# The first one is provided by developers, and the second one is mentioned in design. 
# You have to find and count the number of bugs, and also prioritize them: 
# 'Low', 'Medium', 'High', 'Critical' or 'Done'.

# Each line includes a test case with two strings separated by a pipeline '|'. 
# The first string is from the developers, and the second one is from design.

# Write a program that counts the number of bugs and prioritizes them: 
# 'Low' - 2 or fewer bugs; 
# 'Medium' - 4 or fewer bugs; 
# 'High' - 6 or fewer bugs; 
# 'Critical' - more than 6 bugs; 
# 'Done' - all is done; 

# INPUT SAMPLE:
# Heelo Codevval | Hello Codeeval
# hELLO cODEEVAL | Hello Codeeval
# Hello Codeeval | Hello Codeeval
# THIS IS A TEST | this is a test

# OUTPUT SAMPLE:
# Low
# Critical
# Done
# Critical

# CONSTRAINTS:
# Strings are of the same length from 5 to 40 characters.
# Upper and lower case matters.
# The number of test cases is 40.


# Testing
def testing(file):
    with open(file, 'r+') as f:
        for line in f:
        	pair = line.split("|")
        	compare_1 = pair[0].strip()
        	compare_2 = pair[1].strip()
        	errors = 0
        	loopnum = 0
        	if len(compare_1) < len(compare_2):
        		word = compare_1
    		else:
    			word = compare_2
		for i in word:
			if compare_1[loopnum] != compare_2[loopnum]:
				errors += 1
			loopnum += 1
		if errors > 6:
			print "Critical"
		elif errors < 6 and errors >= 5:
			print "High"	
		elif errors < 5 and errors>= 3:
			print "Medium"
		elif errors < 3 and errors>= 1:
			print "Low"
		else:
			print "Done"

testing("testing.txt")



# Final solution
# import sys

# f = open(sys.argv[1], 'r')
# for line in f:
# 	pair = line.split("|")
# 	compare_1 = pair[0].strip()
# 	compare_2 = pair[1].strip()
# 	errors = 0
# 	loopnum = 0
# 	if len(compare_1) < len(compare_2):
# 		word = compare_1
# 	else:
# 		word = compare_2
# for i in word:
# 	if compare_1[loopnum] != compare_2[loopnum]:
# 		errors += 1
# 	loopnum += 1
# if errors > 6:
# 	print "Critical"
# elif errors < 6 and errors >= 5:
# 	print "High"	
# elif errors < 5 and errors>= 3:
# 	print "Medium"
# elif errors < 3 and errors>= 1:
# 	print "Low"
# else:
# 	print "Done"

