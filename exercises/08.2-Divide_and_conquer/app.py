list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:
def merge_two_list(lists):

    
    two_lists = []
    odd = []
    even = []

    for i in range(len(lists)):
        if lists[i]%2 == 0:
            even.append(lists[i])

        else:
            odd.append(lists[i])
        
    two_lists.append(odd)
    two_lists.append(even)

    return two_lists



print(merge_two_list(list_of_numbers))

