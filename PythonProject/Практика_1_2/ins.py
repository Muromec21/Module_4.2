from Practic_1_1.sortfunc import *

data_1 = list(map(int, input('Введите числа через пробел ').split()))
data_2 = list(map(int, input('Введите числа через пробел ').split()))
data_3 = list(map(int, input('Введите числа через пробел ').split()))
# .split() - Создает список
# map - отношение к каждому элементу
# int - из str(строка) преобразует в int(целое число)
# list - преобразует map object в список

bubble_sort(data_1)
selection_sort(data_2)
insertion_soft(data_3)
print('Пузырьковая сортировка:', data_1)
print('Сортировка выбором:', data_2)
print('Сортировка вставкой:', data_3)