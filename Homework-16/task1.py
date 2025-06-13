#Write a Python function called merge_lists that takes two lists as input and returns
#a new list that contains all the elements from both input lists in the same order.

def merge_lists (list1, list2):
    return  list1 + list2
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

merged_list = merge_lists(list1, list2)

print(merged_list)
