chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:

    merge_list = []

    for i in range(len(list1)):
        merge_list.append(list1[i])

    for i in range(len(list2)):
        merge_list.append(list2[i])

    return merge_list
    
print(merge_list(chunk_one, chunk_two))
