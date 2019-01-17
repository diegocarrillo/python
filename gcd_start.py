# Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcd(a, b):
    while (b != 0):
        t = a # 12 5 2
        a = b # 5 2 1
        b = t % b # 12/5 = 2, 5/2 = 1, 2/1 = 0

    return a

# try out the function with a few examples
print(gcd(5, 12))  # should be 12
print(gcd(34, 8))   # should be 4
