"""
function to return an integer that denotes the value not in the right position when you order the list passed to it.
e.g input = [1,1,3,3,4,1], output = 3
"""

def correct_order(some_list):
    input_list  = some_list
    sorted_list = sorted(some_list)
    count = 0
    index = 0
    for item in input_list:
        if item != sorted_list[index]:
            count = count + 1
        index = index + 1;
    return count


print(correct_order([1,1,3,4,2,1]))


