my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:

def prom_value(lists):
    sumer = 0

    for i in lists:
        sumer += i
    
    return (sumer/len(lists))

print(prom_value(my_list))