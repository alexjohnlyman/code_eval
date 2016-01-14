# Unique Elements

# You are given a sorted list of numbers with duplicates. 
# A file containing a list of sorted integers, comma delimited, one per line. E.g. 
# Print out the sorted list with duplicates removed, one per line. 

# INPUT SAMPLE:
# 1,1,1,2,2,3,3,4,4
# 2,3,4,5,5


# OUTPUT SAMPLE:
# 1,2,3,4
# 2,3,4,5

# Testing
def unique(file):
	with open(file, 'r') as f:
		for line in f:
			list_of_num = []
			for i in line:
				if i in list_of_num:
					pass
				elif i.isdigit() == False:
					pass
				else:
					list_of_num.append(i)
			print ','.join(list_of_num)

unique("uniqueelements.txt")


# Final solution
import sys

f = open(sys.argv[1], 'r')
for line in f:
	list_of_num = []
	for i in line:
		if i in list_of_num:
			pass
		elif i.isdigit() == False:
			pass
		else:
			list_of_num.append(i)
	print ','.join(list_of_num)
