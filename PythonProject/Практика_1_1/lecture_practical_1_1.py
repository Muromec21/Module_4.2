#  Практика. Часть 1
#
# В этом уроке мы займёмся созданием надстройки для программы,
# которая позволит перенести алгоритмы сортировки в отдельный модуль.
# Несмотря на то, что алгоритмы сортировки уже существуют,
# представим, что мы их разработали,
# и наша задача — подготовить код
# для использования другими участниками проекта.
#
# Чтобы облегчить распространение и повторное использование кода,
# логично вынести алгоритмы в отдельный файл.
# Это позволит импортировать готовые функции в любой проект,
# минимизируя дублирование кода.
#
# Мы уже подготовили рабочую среду:
# создали отдельную директорию,
# внутри которой находится файл с именем "sortfunc".
# Этот файл станет самостоятельным модулем,
# который в будущем можно будет передавать коллегам
# и подключать к другим проектам (Рис.1).
#
# Для реализации задачи рассматриваются два алгоритма сортировки:
# метод сортировки пузырьком и метод выбора.
# Эти алгоритмы применяются в образовательных
# целях благодаря их простоте и доступности для понимания,
# несмотря на наличие более производительных методов.
#
# Процесс начинается с создания функции,
# реализующей алгоритм сортировки пузырьком.
# Предварительно формируется массив,
# обозначаемый как «nums» (Рис.2).
# Этот массив представляет собой последовательность чисел,
# расположенных в произвольном порядке.
#
# Данный массив будет использоваться в качестве тестового примера.
# Успешная сортировка чисел с применением разработанного
# алгоритма будет свидетельствовать о его корректной реализации.
#
# Пузырьковая сортировка
#
# Далее рассматривается процесс реализации алгоритма
# сортировки пузырьком. Для этого создаётся функция,
# которая выполняет циклический обход элементов массива.
# В качестве входного параметра функции используется список,
# условно обозначаемый как «ls» (Рис.3),
# хотя в исходных данных он представлен как массив «nums».
#
# Перед началом рассмотрения алгоритма сортировки необходимо
# уточнить несколько ключевых аспектов.
# Алгоритм пузырьковой сортировки функционирует следующим образом:
# два первых элемента массива сравниваются между собой.
# Если первый элемент превышает второй
# (или наоборот, в зависимости от заданных условий),
# выполняется их обмен.
# Процесс продолжается с последующими парами элементов.
# Однако однократное прохождение массива не гарантирует
# полной сортировки, поэтому требуется выполнить несколько
# таких проходов.
#
# Общее число необходимых повторений может быть
# значительным из-за сложности алгоритма,
# которая оценивается с использованием асимптотической
# нотации «О большое» (Big O).
# Данный метод измеряет рост числа выполняемых операций
# в худшем случае в зависимости от количества
# обрабатываемых элементов.
# Для пузырьковой сортировки временная сложность
# оценивается как «O(n²)», что указывает на
# квадратичное увеличение числа операций с ростом
# количества элементов.
# Именно поэтому данный алгоритм не относится к числу наиболее
# эффективных методов сортировки.
#
# Для повышения эффективности алгоритма может быть
# применена оптимизация. В этом случае вводится
# вспомогательная переменная «swapped»,
# предназначенная для отслеживания факта обмена элементов
# в ходе прохода. При отсутствии перестановок на текущей
# итерации выполнение цикла прекращается досрочно,
# что существенно сокращает общее время выполнения для
# уже отсортированных или частично отсортированных массивов (Рис.4).
#
# Далее целесообразно организовать выполнение цикла,
# основанного на состоянии ранее введённой переменной.
# Этот цикл продолжит свою работу до тех пор,
# пока происходят обмены элементов.
# Как только перестановки прекратятся,
# выполнение цикла «while» завершится,
# предотвращая дальнейшие итерации в рамках внутреннего цикла «for».
#
# При отсутствии изменений во время прохода значение
# переменной «swapped» останется равным «False»,
# что приведёт к досрочному выходу из цикла (Рис.5).
# Такой подход позволяет минимизировать количество
# избыточных итераций, тем самым повышая эффективность алгоритма,
# особенно при работе с уже отсортированными массивами.
#
# Далее организуется выполнение цикла «for»,
# осуществляющего последовательный обход всех элементов списка.
# Количество повторений цикла определяется числом
# элементов в списке за вычетом единицы.
# Это необходимо для предотвращения выхода за пределы
# допустимых индексов при обращении к элементам массива.
#
# Такой подход обеспечивает корректное сравнение пар элементов,
# включая предпоследний и последний элементы массива.
# Исключение из итераций последнего индекса предотвращает
# попытку обращения к несуществующему элементу,
# что могло бы привести к возникновению ошибки (Рис.6).
#
# На следующем этапе осуществляется проверка,
# превышает ли элемент списка с индексом «i» значение элемента
# с индексом «i + 1». В случае выполнения данного
# условия два соседних элемента подлежат обмену местами.
# Для реализации этой операции применяется стандартный
# метод перестановки значений переменных,
# широко используемый в алгоритмических задачах (Рис.7).
#
# Указанный метод предполагает простую процедуру
# обмена значениями двух переменных посредством
# лаконичной записи (Рис.8).
# Данный подход широко применяется в программных решениях,
# особенно в задачах, требующих перестановки значений
# между двумя элементами. Его использование обеспечивает
# эффективность и читабельность кода.
#
# Каждый раз при выполнении обмена значений между двумя
# элементами массива переменная «swapped» получает
# значение «True» (Рис.9). Это указывает на то,
# что в текущей итерации произошла перестановка элементов.
# Назначение данной переменной состоит в сигнализации
# о необходимости продолжения выполнения цикла,
# поскольку наличие обменов свидетельствует о том,
# что массив остаётся не полностью отсортированным и требует
# дальнейших проверок и корректировок.
#
# В случае отсутствия перестановок в процессе выполнения
# цикла «for» переменная «swapped» сохраняет значение «False»
# после завершения цикла. Это свидетельствует об отсутствии
# изменений на текущем этапе, что позволяет алгоритму завершить
# выполнение без дополнительных итераций.
# Введение флага «swapped» представляет собой элемент оптимизации,
# обеспечивающий досрочное завершение работы алгоритма в ситуациях,
# когда массив уже отсортирован.
#
# Следует отметить, что существует множество вариантов
# реализации данного алгоритма, и описанный подход
# представляет собой одну из возможных версий пузырьковой
# сортировки.
#
# Для проверки корректности работы алгоритма осуществляется
# вызов функции «bubble_sort», в качестве аргумента которой
# передаётся массив «nums». По завершении выполнения функции
# возможно вывести отсортированный список,
# чтобы удостовериться в правильности полученного результата (Рис.10).
#
# Наблюдается, что функция не возвращает отсортированный
# список как новый объект, а выполняет сортировку исходного
# списка непосредственно, изменяя порядок его элементов.
# В результате, при повторном выводе списка он уже оказывается
# отсортированным (Рис.11).
#
# В первом вызове отсутствие использования функции «print»
# не является необходимым, однако важно отметить,
# что функция выполнила свою задачу,
# и сортировка была успешно произведена (Рис.12).
#
# Сортировка выборкой
#
# Для улучшения функциональности кода добавим дополнительную функцию,
# реализующую сортировку выборкой.
# Этот алгоритм основывается на разделении списка на две части:
# отсортированную и неотсортированную.
# Мы будем поочередно обрабатывать все элементы
# в неотсортированной части,
# находить минимальный элемент и перемещать его
# в отсортированную часть списка.
#
# Начнём с разработки функции,
# которая будет принимать список для сортировки (Рис.13).
#
# Затем следует отметить, что для реализации алгоритма
# потребуются вложенные циклы.
# Первый цикл будет использовать индекс «i»,
# который будет изменяться в пределах диапазона,
# соответствующего количеству элементов в списке (Рис.14).
# Этот индекс «i» будет отражать количество отсортированных значений.
#
# На первом этапе необходимо выбрать элемент,
# который будет служить опорным. Предполагается,
# что первым элементом списка является наименьший.
# Для этого переменной «lowest» присваивается значение индекса «i»,
# чтобы определить индекс минимального элемента на текущем этапе (Рис.15).
#
# Затем необходимо пройти по неотсортированной части списка,
# начиная с элемента, следующего за индексом «i»
# (то есть с индекса «i + 1»). Для этого используется дополнительный
# цикл, который будет инициализироваться с этого индекса (Рис.16).
#
# В данном цикле осуществляется сравнение каждого элемента
# неотсортированной части списка с текущим минимальным элементом.
# Если элемент с индексом «j» в неотсортированной части
# списка меньше элемента с индексом «lowest»,
# значение переменной «lowest» обновляется,
# принимая значение «j» (Рис.17).
#
# После завершения данного цикла необходимо произвести обмен
# значениями между элементом с индексом «i» и
# элементом с индексом «lowest» (Рис.18).
#
# Реализация сортировки выборкой является достаточно простой
# и логичной. Теперь можно проверить
# как будет работать эта функция на примере списка «nums».
# Для этого следует закомментировать ранее использованный код
# пузырьковой сортировки, вызвать функцию сортировки выборкой
# и вывести результат (Рис.19).
#
# В результате получаем отсортированный список (Рис.20).
#
# Таким образом, задача была успешно решена.
# Были написаны функции внутри модуля,
# которые могут быть использованы в различных проектах
# и обменены с коллегами.
