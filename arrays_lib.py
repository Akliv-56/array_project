from logging import log_action
def filter_even(arr):
    print("Фильтрация четных эллементов массива",arr)
    newarr =[]
    for i in range(0,len(arr),1):
        if arr[i]%2 == 0:
            newarr.append(arr[i])
    return newarr

def filter_odd(arr):
    print("Фильтрация нечетных эллементов массива",arr)
    newarr =[]
    for i in range(0,len(arr),1):
        if arr[i]%2 != 0:
            newarr.append(arr[i])
    return newarr

def filter_postive_matrix(matrix):
    print("Фильтрация положительных чисел матрицы:",matrix)
    newarr =[]
    for i in range(0,len(matrix,1)):
        for j in range(0,len(matrix[i])):
            if matrix[i][j] >= 0:
                newarr.append(matrix[i][j])
    return newarr

def filter_even_matrix(matrix):
    print("Фильтрация четных эллементов матрицы",matrix)
    newmat =[]
    for i in range(0,len(matrix),1):
        for j in range(0,len(matrix[i]),1):
            if matrix[i][j]%2 == 0:
                newmat.append(matrix[i])
    return newmat

def sum_1d(array:list) -> int or float:
    if not isinstance(array,list):
        raise TypeError("Ожидает список для одномерного массива")
    message = f"вызвана функция sum_1d с параметрами:{array}"
    log_action(message)
    sum = 0
    for number in array:
        sum+=number
    filter_even(array)
    return sum

def prod_1d(array:list) -> int or float:
    if not isinstance(array,list):
        raise TypeError("Ожидает список для одномерного массива")
    message = f"вызвана функция prod_1d с параметрами:{array}"
    log_action(message)
    prod = 1
    for number in array:
        prod*= number
    filter_even(array)
    return prod

def mean_1d(array:list) -> int or float:
    if not isinstance(array,list):
        raise TypeError("Ожидает список для одномерного массива")
    message = f"вызвана функция mean_1d с параметрами:{array}"
    log_action(message)
    sum=0
    avg = 0
    for number in array:
        sum+=number
    avg = sum / len(array)
    filter_even(array)
    return avg

def max_1d(array:list) -> int or float:
    if not isinstance(array,list):
        raise TypeError("Ожидает список для одномерного массива")
    message = f"вызвана функция max_1d с параметрами:{array}"
    log_action(message)
    
    max = array[0]
    for number in array:
        if number > max:
            max = number
    filter_even(array)
    return max

def min_1d(array:list) -> int or float:
    if not isinstance(array,list):
        raise TypeError("Ожидает список для одномерного массива")
    message = f"вызвана функция min_1d с параметрами:{array}"
    log_action(message)
    
    min= array[0]
    for number in array:
        if number<min:
            min = number
    filter_even(array)
    return min

def sum_2d(array:list[list[int]]) -> int or float:
    if not isinstance(array,list[list]):
        raise TypeError("Ожидает список для двумерной матрицы")
    message = f"вызвана функция sum_2d с параметрами:{array}"
    log_action(message)
    
    sum = 0
    for i in range(0,len(array),1):
        for j in range(0,len(array[i]),1):
            sum+=array[i][j]
    filter_postive(array)
    return sum

def prod_2d(array:list) -> int or float:
    if not isinstance(array,list[list]):
        raise TypeError("Ожидает список для двумерной матрицы")
    message = f"вызвана функция prod_2d с параметрами:{array}"
    log_action(message)
    prod = 1
    for i in range(0,len(array),1):
        for j in range(0,len(array[i]),1):
            prod*= array[i][j]
    filter_postive(array)
    return prod

def mean_2d(array:list) -> int or float:
    if not isinstance(array,list[list]):
        raise TypeError("Ожидает список для двумерной матрицы")
    message = f"вызвана функция mean_2d с параметрами:{array}"
    log_action(message)
    sum = 0
    avg = 0
    for i in range(0,len(array),1):
        for j in range(0,len(array[i]),1):
            sum+=array[i][j]
    avg = sum / len(array)
    filter_postive(array)
    return avg

def max_2d(array:list) -> int or float:
    if not isinstance(array,list[list]):
        raise TypeError("Ожидает список для двумерной матрицы")
    message = f"вызвана функция max_2d с параметрами:{array}"
    log_action(message)
    max = array[0][0]
    for i in range(0,len(array),1):
        for j in range(0,len(array[i]),1):
            if array[i][j] > max:
                max = array[i][j]
    filter_postive(array)
    return max

def min_2d(array:list) -> int or float:
    if not isinstance(array,list[list]):
        raise TypeError("Ожидает список для двумерной матрицы")
    message = f"вызвана функция min_2d c параметрами:{array}"
    log_action(message)
    min= array[0][0]
    for i in range(0,len(array),1):
        for j in range(0,len(array[i]),1):
            if array[i][j] < min:
                min = array[i][j]
    filter_postive(array)
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


        
            