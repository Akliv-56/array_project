from logging import log_action
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

def max_2d(array:list) -> int or float:
    max = array[0][0]
    for i in range(0,len(array),1):
        for j in range(0,len(array),1):
            if array[i][j] > max:
                max = array[i][j]
    return max

def min_2d(array:list) -> int or float:
    message = "вызвана функция min_1d"
    log_action(message)
    min= array[0][0]
    for i in range(0,len(array),1):
        for j in range(0,len(array),1):
            if array[i][j] < min:
                min = array[i][j]
    return min

def sum_arrays(arr1:list[int or float], arr2:list[int or float]):
    message = "вызвана функция sum_arrays"
    log_action(message)
    new_arr = []
    if len(arr1) != len(arr2):
        return None
    else:
        for i in range(0,len(arr1),1):
            new_arr.append(arr1[i] + arr2[i])
    return new_arr

def diff_arrays(arr1:list[int or float], arr2:list[int or float]):
    message = "вызвана функция diff_arrays"
    log_action(message)
    new_arr = []
    if len(arr1) != len(arr2):
        return None
    else:
        for i in range(0,len(arr1),1):
            new_arr.append(arr1[i] - arr2[i])
    return new_arr

def prod_arrays(arr1:list[int],arr2:list[int]):
    message = "вызвана функция prod_arrays"
    log_action(message)
    new_arr = []
    for i in range(0,len(arr1),1):
        prod = arr1[i] * arr2[i]
        new_arr.append(prod)
    return new_arr

def compare_arrays(arr1:list[int],arr2:list[int]):
    message = "вызвана функция compare_arrays"
    log_action(message)
    arr1bigger = []
    arrequal = []
    arr2bigger = []
    for i in range(0,len(arr1),1):
        if arr1[i] > arr2[i]:
            bigger = f"{arr1[i]} > {arr2[i]}"
            arr1bigger.append(bigger)
        if arr1[i] == arr2[i]:
            equal = f"{arr1[i]} = {arr2[i]}"
            arrequal.append(equal)
        if arr1[i] < arr2[i]:
            bigger2 = f"{arr1[i]} < {arr2[i]}"
            arr1bigger.append(bigger2)
    return arr1bigger, arrequal, arr2bigger

def list_maxpos(array:list[int or float]):
    #[1,2,3,4,5]
    array_maxpos = []
    max = 0
    for i in range(0,len(array),1):
        if array[i] > array[max]:
            max = i
    array_maxpos.append(max)
    for i in range(0,len(array),1):
        if array[i] == array[max]:
            array_maxpos.append(i)
    return array_maxpos


        
            