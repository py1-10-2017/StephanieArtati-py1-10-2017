def list_to_dict(list1, list2):
    new_dict = {}
    if (len(list2) > len(list1)):
        new_tuple = zip(list2, list1)
    else:
        new_tuple = zip(list1, list2)
    return dict(new_tuple)

list1 = [1,2,3,4,5,6]
list2 = ["one","two","three","four","five", "six"]
print(list_to_dict(list1, list2))

list1 = [1,2,3,4,5,6,7]
list2 = ["one","two","three","four","five", "six"]
print(list_to_dict(list1, list2))

list1 = [1,2,3,4,5]
list2 = ["one","two","three","four","five", "six"]
print(list_to_dict(list1, list2))
