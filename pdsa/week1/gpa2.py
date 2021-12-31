def IsPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def GetPrimes(n):
    output = []
    for i in range(2, n+1):
        if(IsPrime(i)):
            output.append(i)
    return output

def Goldbach(n):
    output = []
    primes = GetPrimes(n)
    p1 = [num for num in primes if num <= n//2]
    p2 = [num for num in primes if num >= n//2]
    for i in p1:
        for j in p2:
            if(i+j) == n:
                output.append((i,j))
                break
    return output
print(Goldbach(26))