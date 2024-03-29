"""
"Given a list of N numbers, use a single list comprehension to produce a new 
list that only contains those values that are even numbers, and from elements 
in the original list that had even indices

For example, if list[2] contains a value that is even, that value should be 
included in the new list, since it is also at an even index (i.e., 2) in the 
original list. However, if list[3] contains an even number, that number should 
not be included in the new list since it is at an odd index (i.e., 3) in the 
original list."
"""

def compress_list(some_list):
    try:
        return [i for i in some_list if some_list.index(i) %2 == 0 and i %2 == 0]
    except TypeError:
        pass
    


