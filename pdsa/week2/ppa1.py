def MyMethod(L,k,n):
    if L == []:
        return(False, n)
    n += 1
    m = len(L)//2

    if L[m] == k:
        return (True, n)
    
    if k > L[m]:
        return MyMethod(L[m+1 : ], k, n)
    else:
        return MyMethod(L[: m], k, n)

def binarySearchIndexAndComparisons(L,k):
    return MyMethod(L, k, 0)   

print(binarySearchIndexAndComparisons([2, 6, 8, 11, 17, 23, 33, 44, 46, 50, 65], 11))