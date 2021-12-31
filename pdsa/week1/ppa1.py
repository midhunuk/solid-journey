def IsPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def Twin_Primes(n,m):
    lastPrime = None
    output = []
    for i in range(n, m+1):
        if(IsPrime(i)):
            if(lastPrime != None and (i - lastPrime == 2)):
                output.append((lastPrime, i))
            lastPrime = i    
    return output


n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))
