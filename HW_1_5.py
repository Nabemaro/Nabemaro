def alternate_extract(list1, list2):
    result = [None]*(len(list1)+len(list2))
    result[::2] = list1
    result[1::2] = list2
    print(result)


list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

alternate_extract(list1, list2)
