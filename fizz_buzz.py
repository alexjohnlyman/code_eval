
# search a file
# replace x with

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
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)


def fizz_buzz(file_name):
    with open(file_name, 'r+') as f:
        lines = f.read()
        print lines
        x = lines[0]
        print x
        y = lines[2]
        print y
        # n = lines[4]
        for k in numbers:
            if (k % x == 0) and (k % y == 0):
                print "FB"
                # k == "FB"
            elif k % x == 0:
                print "F"
                # i == "F"
            elif k % y == 0:
                print "B"
                # j == "B"
            # return numbers


fizz_buzz('test.txt')


        # X = lines[0]
        # Y = lines[1]
        # N = lines[2]
        # return lines


