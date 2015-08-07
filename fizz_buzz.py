# Fizz Buzz, with a twist

# def change_fizz(x, y, n):
#     for i in my_list:
#         if i % x == 0:
#             i == "Fizz"
#         return my_list
#
# def change_buzz(x, y, n):
#     for j in my_list:
#         if j % y == 0:
#             j == "Buzz"
#         return my_list


# Test
# x = 2
# y = 7
# n = 42
#
# line = ""
# for k in range(1, n):
#     if (k % x == 0) and (k % y == 0):
#         k = " FB"
#         line += str(k)
#     elif k % x == 0:
#         k = " F"
#         line += str(k)
#     elif k % y == 0:
#         k = " B"
#         line += str(k)
#     else:
#         k = "{0: }".format(k)
#         line += str(k)
# print line.strip()

# Test 2
def test_this(filename):
    f = open(filename, 'r+')
    for line in f:
        x = int(line[0])
        y = int(line[2])
        n = int(str(line[4]) + str(line[5]))
        line = ""
        for k in range(1, n):
            if (k % x == 0) and (k % y == 0):
                k = " FB"
                line += str(k)
            elif k % x == 0:
                k = " F"
                line += str(k)
            elif k % y == 0:
                k = " B"
                line += str(k)
            else:
                k = "{0: }".format(k)
                line += str(k)
        print line.strip()
test_this("test.txt")


# Final Answer
import sys

f = open(sys.argv[1], 'r+')
for line in f:
    x = int(line[0])
    y = int(line[2])
    n = int(str(line[4]) + str(line[5]))
    line = ""
    for k in range(1, n):
        if (k % x == 0) and (k % y == 0):
            k = " FB"
            line += str(k)
        elif k % x == 0:
            k = " F"
            line += str(k)
        elif k % y == 0:
            k = " B"
            line += str(k)
        else:
            k = "{0: }".format(k)
            line += str(k)
    print line.strip()