# Swap Case
# Write a program which swaps letters' case in a sentence. 
# All non-letter characters should remain the same.
# Your program should accept as its first argument a path to a filename. 

# INPUT SAMPLE:
# Hello world!
# JavaScript language 1.8
# A letter

# OUTPUT SAMPLE:
# hELLO WORLD!
# jAVAsCRIPT LANGUAGE 1.8
# a LETTER


# Testing
def swap_case(file):
	with open(file, 'r') as f:
		for line in f:
			word = ""
			line = line.strip()
			for letter in line:
				if letter.isupper():
					word += letter.lower()
				else:
					word += letter.upper()
			print word

swap_case("swapcase.txt")



# Final solution
import sys

f = open(sys.argv[1], 'r')
for line in f:
	word = ""
	line = line.strip()
	for letter in line:
		if letter.isupper():
			word += letter.lower()
		else:
			word += letter.upper()
	print word
