#I want to test each number to see if the first and last digit are the same
# if they are, then i want to check that it is not divisible by any number other than 1 and itself.



numbers = range(1, 1000)
not_prime = []
potential_primes = []
potential_palin = []

def prime_check(x):
    for i in x:     #this is not printing out the right numbers........
        if i % 2 == 0:
            not_prime.append(i)
        elif i % 3 == 0:
            not_prime.append(i)
        elif i % 4 == 0:
            not_prime.append(i)
        elif i % 5 == 0:
            not_prime.append(i)
        elif i % 6 == 0:
            not_prime.append(i)
        elif i % 7 == 0:
            not_prime.append(i)
        elif i % 8 == 0:
            not_prime.append(i)
        elif i % 9 == 0:
            not_prime.append(i)
        else:
            potential_primes.append(i)
    return potential_primes

def palindrome_check(a):    # this is working like it should
    for i in a:
        if i > 1:
            x = str(i)
            if x[0] != x[-1]:
                pass
            if x[0] == x[-1]:
                y = int(x)
                potential_palin.append(y)
    return potential_palin


print prime_check(numbers)
print palindrome_check(numbers)

# print to "stdout" largest prime number