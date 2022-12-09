#!/usr/bin/python3
def replace_element(lst, old, new):
    new_list = []
    for x in lst:
        if x == old:
            new_list.append(new)
        else:
            new_list.append(x)
    return new_list

#Test
lst = [1,2,3,4,5]
old = 3
new = 8

print(replace_element(lst, old, new)) #[1,2,8,4,5]
