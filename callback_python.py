def copy_and_manipulate(array, callback):
    output = []
    for i in array:
        output.append(callback(i))
    return output

def add_one(num):
    num+=1 # freaking weird that python needs to evaluate this before it is returned
    return num


print(copy_and_manipulate([1,2,3], add_one))
