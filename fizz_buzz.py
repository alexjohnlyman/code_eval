
def fizz_buzz(file_name):
    with open(file_name, 'r+') as f:
        # line = []
        lines = f.read()
        str(lines)
        # for i in lines:
        #     line.append(i)
        print lines[2]


        # X = lines[0]
        # Y = lines[1]
        # N = lines[2]
        # return lines

fizz_buzz('test.txt')




