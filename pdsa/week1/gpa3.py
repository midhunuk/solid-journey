def GetType(element):
    if type(element) == int:
        return 'int'
    if type(element) == float:
        return 'float'
    if type(element) == str:
        return 'str'
    if type(element) == bool:
        return 'bool'

def odd_one(L):
    if(GetType(L[0]) == GetType(L[1])):
        group = GetType(L[0])
        for i in range(2, len(L)):
            if(GetType(L[i]) != group):
                return GetType(L[i])
    else:
        if(GetType(L[0]) == GetType(L[3])):
            return GetType(L[1])
        else:
            return GetType(L[0])
    

print(odd_one(eval(input().strip())))