# Практика. Часть 2
#
# В предыдущем уроке был начат процесс разработки модуля,
# содержащего функции с алгоритмами сортировки.
# Код был дополнен, а также добавлены комментарии,
# что позволяет тем, кто не полностью понимает
# принцип работы этих алгоритмов,
# более подробно ознакомиться с их реализацией.
# Этот код будет включен в материалы урока.
# Кроме того, был создан новый проект,
# в который был перенесён данный код.
#
# Предположим, что алгоритм переносится в другой проект.
# На данный момент мы не обсуждаем создание собственных
# библиотек и их публикацию на PyPI,
# а ограничиваемся просто переносом кода, чего вполне достаточно.
#
# Стоит обратить внимание на структуру проекта.
# В проекте имеется пакет под названием «module4»,
# в котором находится файл «alg.py»,
# содержащий все указанные функции (Рис.1).
#
# Основная логика будет реализована в другом месте.
# Задача заключается в том,
# чтобы пользователи вводили определённое количество данных,
# из которых будет сформирован список,
# и наши алгоритмы смогут помочь в сортировке этих данных.
# Предположим, что пользователь введёт данные трижды,
# причем всё будет вводиться в одну строку.
#
# На данном этапе мы научимся создавать список из одной строки.
# Для этого потребуется использовать ввод пользователя.
# Создадим переменную «data_1» и с помощью команды
# «input» запросим у пользователя ввод данных.
# Если пользователь введёт значения, разделённые пробелами,
# мы получим строку (Рис.2). Важно отметить, что всё,
# что поступает через команду «input», изначально является строкой.
#
# С помощью метода «split» можно преобразовать эту строку в список,
# используя пробел в качестве разделителя (Рис.3).
#
# Если выполнить вывод переменной «data_1»,
# то в результате будет представлен список.
# При запуске программы и вводе значений, мы получим список,
# состоящий из строк — "1", "2", "1", "2" (Рис.4).
# Однако в дальнейшем нам потребуется работать с числами.
#
# При использовании команды «int» невозможно напрямую
# преобразовать строки в числа из списка, что приведет к ошибке.
# Для преобразования каждого элемента списка в число
# необходимо применить команду «int» к каждому элементу индивидуально.
#
# Для того чтобы применить функцию ко всем элементам
# последовательности, используется функция «map».
# В качестве аргументов функции «map» передаются
# команда «input» и метод «split».
# Однако предварительно нужно указать функцию,
# которая будет применена к каждому элементу,
# в нашем случае это функция «int».
# Таким образом, каждый элемент списка будет преобразован
# в целое число. Однако, если обратиться к результату,
# то вместо списка будет получен объект «map» (Рис.5).
#
# Для получения списка необходимо обернуть результат
# в команду «list». После выполнения программы,
# при вводе значений, мы получим список,
# содержащий целые числа (Рис.6).
#
# Для удобства добавим сообщение с просьбой:
# "Введите числа через пробел".
# Поскольку нам нужно выполнить этот процесс трижды,
# создадим три переменные: «data_1», «data_2» и «data_3» (Рис.7).
#
# После того как пользователь введёт три списка, необходимо,
# чтобы каждый из этих списков был отсортирован
# с использованием соответствующей функции.
#
# Для использования кода требуется его импортировать.
# Для этого следует вернуться к первой строке и добавить
# команду импорта: «from module4.alg import *» (Рис.8).
#
# Будем поочередно вызывать функцию «bubble_sort»,
# передавая ей первый список, затем функцию «selection_sort»,
# передавая второй список, и наконец функцию «insertion_sort»,
# передавая третий список.
# После выполнения этих операций выведем все три списка,
# добавив в комментариях соответствующие уточнения:
# "Пузырьковая сортировка", "Сортировка выбором"
# и "Сортировка вставкой" (Рис.9).
#
# После запуска программы, система запросит ввод чисел через пробел.
# Вводим неотсортированные числа и получаем следующие результаты:
# пузырьковая сортировка выдала 1, 2, 3, 4, 5, 7;
# сортировка выбором — 0, 1, 3, 4, 4, 5, 6;
# сортировка вставками — 2, 3, 7, 9, 9 (Рис.10).
# Каждый из этих списков был обработан функциями,
# написанными на предыдущем занятии,
# и все алгоритмы успешно выполнили свою задачу.
# Таким образом, можно переносить важные и полезные
# фрагменты кода из одного проекта в другой.
#
# В ходе данного занятия были рассмотрены конструкции «map»,
# «int» и «list», а также повторена работа с пакетами и импортами.
