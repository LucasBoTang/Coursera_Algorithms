def karatsuba(int1, int2):
    """
    recursive integer multiplication and Karatsuba's algorithm
    """
    # base case
    if len(int1) == 1 and len(int2) == 1:
        return int(int1) * int(int2)
    # number of digits
    n = max(len(int1), len(int2))
    n += n % 2
    # fill zeros
    int1 = str(int1).zfill(n)
    int2 = str(int2).zfill(n)
    # partition
    a = int1[:n//2]
    b = int1[n//2:]
    c = int2[:n//2]
    d = int2[n//2:]
    # recrusion
    X = karatsuba(a, c)
    Y = karatsuba(b, d)
    Z = karatsuba(str(int(a)+int(b)), str(int(c)+int(d))) - X - Y
    return int(str(X) + '0' * n) + Y + int(str(Z) + '0' * (n // 2))

int1 = input('Enter first intger: ')
int2 = input('Enter second intger: ')
print('Result:', karatsuba(int1, int2))
