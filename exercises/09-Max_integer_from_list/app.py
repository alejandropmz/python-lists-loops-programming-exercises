my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

#Your code go from here:

def maxInteger(lists):

    validator = 0

    for i in range(len(lists)):
        if validator < lists[i]:
            validator = lists[i]

    return validator




print(maxInteger(my_list))

"""     new_list = []

    for i in range(len(lists)):
        new_list.append(lists[i])



    return sorted(new_list)[len(new_list)-1] """