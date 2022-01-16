def DishPrepareOrder(orders):
    output =[]
    dictbyorder ={}
    for order in orders:
        if order in dictbyorder:
            dictbyorder[order] = dictbyorder[order] + 1
        else:
            dictbyorder[order] = 1
    dictbyordernumber = {}
    for order, number in dictbyorder.items():
        if number in dictbyordernumber:
            dictbyordernumber[number] = dictbyordernumber[number] + [order]
        else:
            dictbyordernumber[number] = [order]
    for order_number in sorted(dictbyordernumber.keys(), reverse=True):
        output += sorted(dictbyordernumber[order_number])
    return output

nums = [1006, 1008, 1009, 1008, 1007, 1005, 1008, 1001, 1003, 1009, 1006, 1003, 1004, 1002, 1008, 1005, 1004, 1007, 1006, 1002, 1002, 1001, 1004, 1001, 1003, 1007, 1007, 1005, 1004, 1002]
[1002, 1004, 1007, 1008, 1001, 1003, 1005, 1006, 1009]
print(DishPrepareOrder(nums))