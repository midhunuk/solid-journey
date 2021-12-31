def find_Min_Difference(L,P):
    L.sort()
    currentIndex = P - 1
    minDiff = 9999 # asuming no large numbers
    while (currentIndex < len(L)):
        diff = L[currentIndex] - L[(currentIndex + 1) - P ]
        if(diff < minDiff):
            minDiff = diff
        currentIndex += 1
    return minDiff

L=[3,4,1,9,56,7,9,12]
P=5
print(find_Min_Difference(L,P))