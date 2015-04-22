#I want to test each number to see if the first and last digit are the same

#Prime = A number is not divisible by any number other than itself.
#I would need to check that a number % every number underneath it != 0.


numbers = range(2, 1000)
# num = 1000
# potential_primes = []
# potential_palin = []

def is_palin(a):
    for i in a:
        if i > 1:
            x = str(i)
            if x[0] != x[-1]:
                pass
            if x[0] == x[-1]:
                y = int(x)
                prime_check(y)
            return y

def prime_check(n):
    z = range(2, n)
    if (n % z) != 0:
        return n

# print prime_check(numbers)
print is_palin(numbers)





# print to "stdout" largest prime number