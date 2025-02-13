# Краткое описание проекта
Это библиотека для работы с массивами и матрицами
# Функции
## Одномерные массивы

###### sum_1d(arr1:list[int or float]) 
функция которая находит сумму всех элементов массива

_Пример 1_
```Python
array1 = [1,2,3]
sum_1d(array1)  # return 6
```

###### prod_1d(array:list[int or float])
функция которая находит произведение всех элементов массива

_Пример 1_
```Python
array1 = [1,2,3]
prod_1d(array1)  # return 6
```

###### mean_1d(array:list[int or float])
функция которая находит среднее арифмитическое всех элементов массива

_Пример 1_
```Python
array1 = [1,2,3]
mean_1d(array1)  # return 2
```
###### max_1d(array:list[int or float])
функция которая находит максимальное число среди всех элементов массива

_Пример 1_
```Python
array1 = [1,2,3]
max_1d(array1)  # return 3
```

###### min_1d(array:list[int or float])
функция которая находит минимальное число среди всех элементов массива

_Пример 1_
```Python
array1 = [1,2,3]
min_1d(array1)  # return 1
```
###### sum_2d(array:list[list[int or float]])
функция которая находит сумму всех элементов матрицы

_Пример 1_
```Python
matrix1 = [[1,2,3],[1,2,3],[1,2,3]]
sum_2d(matrix1)  # return 18
```

###### prod_2d(array:list[list[int or float]])
функция которая находит произведение всех элементов матрицы

_Пример 1_
```Python
matrix1 = [[1,2,3],[1,2,3],[1,2,3]]
prod_2d(matrix1)  # return 216
```

###### mean_2d(array:list[list[int or float]])
функция которая выводит среднее арифметическое всех элементов матрицы

_Пример 1_
```Python
matrix1 = [[1,2,3],[1,2,3],[1,2,3]]
mean_2d(matrix1)  # return 2
```

###### max_2d(array:list[list[int or float]])
функция которая выводит максимальный элемент среди всех элементов матрицы

_Пример 1_
```Python
matrix1 = [[1,2,3],[1,2,3],[1,2,3]]
max_2d(matrix1)  # return 3
```

###### min_2d(array:list[list[int or float]])
функция которая выводит максимальный элемент среди всех элементов матрицы

_Пример 1_
```Python
matrix1 = [[1,2,3],[1,2,3],[1,2,3]]
max_2d(matrix1)  # return 1
```

###### sum_arrays(array1:list[list[int or float]],array2:list[list[int or float]])
функция которая выводит новый массив в который вносится сумма элементов двух масивов с одинаковым размером

_Пример 1_
```Python
matrix1 = [1,2,3]
matrix1 = [1,2,3]
sum_arrays(matrix1,matrix2)  # return [2,4,6]
```
###### diff_arrays(array1:list[list[int or float]],array2:list[list[int or float]])
функция которая выводит новый массив в который вносится разница элементов двух масивов с одинаковым размером
_Пример1_
```Python
matrix1 = [2,4,6]
matrix1 = [1,2,3]
prod_arrays(matrix1,matrix2)  # return [1,2,3]
```

###### compare_arrays(array1:list[list[int or float]],array2:list[list[int or float]])
функция которая выводит новые массивы в которые вносится сравнение элементов двух масивов с одинаковым размером
_Пример1_
```Python
matrix1 = [4,10,3]
matrix2 = [2,14,3]
compare_arrays(matrix1,matrix2)  # return [4],[14],[3]
