# Write a program which checks input numbers and determines whether a number is even or not.
#
# INPUT SAMPLE:
# 701
# 4123
# 2936
# Your program should accept as its first argument a path to a filename. Input example is the following
#
# OUTPUT SAMPLE:
# Print 1 if the number is even or 0 if the number is odd.
# 0
# 0
# 1
# All numbers in input are integers > 0 and < 5000.



# Option to write out numbers to a new file
# def even_numbers(file_name):
#     input = open(file_name, 'r+')
#     output = open('new_file.txt', 'w+')
#     for line in list(input):
#         line = int(line)
#         if line % 2 == 0:
#             output.write("1\n")
#         else:
#             output.write("0\n")
#     output.close()
#     input.close()
#     return 'new_file.txt'
#
# even_numbers('evennumbers.txt')


#Option to 'print' the numbers (CORRECT ANSWER)

# import sys

# For Testing
# def even_numbers(input):
#     input = open(sys.argv[1], 'r+')
#     for line in list(input):
#         if line == "":
#             continue
#         else:
#             line = int(line)
#             if line % 2 == 0:
#                 print '{}' .format('1')
#             else:
#                 print '{}' .format('0')
#     input.close()
#
# even_numbers('evennumbers.txt')

# Final answer
# input = open(sys.argv[1], 'r+')
# for line in list(input):
#     if line == "":
#         continue
#     else:
#         line = int(line)
#         if line % 2 == 0:
#             print '{}' .format('1')
#         else:
#             print '{}' .format('0')
# input.close()