# list_of_nums = ['70.920', '-38.797', '14.354', '99.323', '90.374', '7.581']
# list_of_nums = '70.920 -38.797 14.354 99.323 90.374 7.581'


# line_int = map(float, list_of_nums.split())
# print sorted(line_int)





# Testing
def simple_sort(file):
	with open(file, 'r') as f:
		for line in f:
			line_int = map(float, line.split())
			final_list = sorted(line_int)
			print " ".join(format(x, ".3f") for x in final_list)

simple_sort("simplesort.txt")


# Final solution
import sys

f = open(sys.argv[1], 'r')
for line in f:
	line_int = map(float, line.split())
	final_list = sorted(line_int)
	print " ".join(format(x, ".3f") for x in final_list)