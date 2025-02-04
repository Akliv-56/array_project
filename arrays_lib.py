def sum_1d(array:list) -> int or float:
    sum = 0
    for number in array:
        sum+=number
    return sum
def prod_1d(array:list) -> int or float:
    prod = 1
    for number in array:
        prod*= number
    return prod

def mean_1d(array:list) -> int or float:
    sum=0
    avg = 0
    for number in array:
        sum+=number
    avg = sum / len(array)
    return avg

def max_1d(array:list) -> int or float:
    max = array[0]
    for number in array:
        if number > max:
            max = number
    return max

def min_1d(array:list) -> int or float:
    min= array[0]
    for number in array:
        if number<min:
            min = number
    return min

def sum_2d(array:list[list[int]]) -> int or float:
    sum = 0
    for i in range(0,len(array),1):
        for j in range(0,len(array),1):
            sum+=array[i][j]
    return sum

def prod_2d(array:list) -> int or float:
    prod = 1
    for i in range(0,len(array),1):
        for j in range(0,len(array),1):
            prod*= array[i][j]
    return prod

def mean_2d(array:list) -> int or float:
    sum = 0
    avg = 0
    for i in range(0,len(array),1):
        for j in range(0,len(array),1):
        sum+=array[i][j]
    avg = sum / len(array)
    return avg

def max_1d(array:list) -> int or float:
    max = array[0][0]
    for i in range(0,len(array),1):
        for j in range(0,len(array),1):
            if array[i][j] > max:
                max = array[i][j]
    return max

def min_1d(array:list) -> int or float:
    min= array[0][0]
    for i in range(0,len(array),1):
        for j in range(0,len(array),1):
            if array[i][j] < min:
                min = array[i][j]
    return min

def diff_arrays(arr1:list[int or float], arr2:list[int or float]):
    new_arr = []
    if len(arr1) != len(arr2):
        return None
    else:
        for i in range(0,len(arr1),1):
            new_arr.append(arr1 - arr2)
    return new_arr