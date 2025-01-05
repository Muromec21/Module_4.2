from Module import *

d = 7

def square(x):
    d = x ** 2
    def even(x):
        nonlocal d
        d = x / 2
        if d % 2 == 0:
            print('Четное')
        else:
            print('Нечетное')
    even(x)
    return d

a = 5
b = square(4)
print(a)
print(b)

# Лекция. Пространства имен часть II и области видимости
#
# Пространства имен часть II и области видимости
#
# На этом занятии продолжается изучение пространства имён и
# вводится понятие области видимости. Как мы уже знаем,
# пространство имён — это система, которая работает как словарь,
# связывая имена с объектами.
# Однако это не гарантирует корректного использования переменных в коде,
# поскольку одни и те же имена могут встречаться в разных местах.
#
# Примеры повторения имён:
#
# Переменные цикла: в циклах for часто используется одна и та же
# переменная, например, i. Это допустимо,
# так как область видимости переменной i ограничена блоком цикла.
#
# Переменные функций: переменные, определённые внутри функции,
# существуют только в её локальной области видимости и не конфликтуют
# с глобальными переменными с теми же именами.
#
# Область видимости (Scope)
#
# Область видимости определяет, где именно в программе переменная доступна.
# В Python существует четыре уровня области видимости,
# которые следуют принципу LEGB:
#
# 1) Локальная (Local): переменные, созданные внутри функций.
#
# 2) Закрывающая (Enclosing): переменные внешней функции
# (для вложенных функций).
#
# 3) Глобальная (Global): переменные, определённые на уровне модуля.
# Например, наша переменная aнаходится
# в глобальной области видимости (Рис.1).
#
# 4) Встроенная (Built-in): стандартные функции и имена Python,
# такие как "print", "len", "int" и др.
#
# Проблемы глобальной области видимости
#
#Глобальная область видимости может быть небезопасной в сложных программах,
# особенно при подключении нескольких модулей.
# Если два или более модулей содержат переменные с одинаковыми именами,
# возникает конфликт.
# Переменные с совпадающими именами находятся в одной глобальной области
# видимости, если они подключены без указания пространства имён.
#
# В результате может быть трудно понять,
# какое значение в конкретный момент времени хранится в переменной,
# что усложняет отладку программы.
#
#Локальная область видимости
#
#Локальная область видимости относится к переменным,
# которые существуют только в пределах определённых конструкций кода,
# таких как функции или циклы for.
# Эти переменные создаются при выполнении конструкций
# и уничтожаются после завершения их работы.
#
# Например, переменная "d", используемая внутри функции "square",
# существует только в её локальной области видимости (Рис.2).
# Это означает, что она недоступна за пределами функции.
# Такое поведение позволяет использовать одно и то же имя переменной
# несколько раз в разных местах программы,
# при этом значения этих переменных не будут пересекаться.
#
# Встроенная область видимости
#
# Встроенная область видимости включает стандартные модули и функции,
# доступные в Python по умолчанию. Это такие элементы,
# как "print", "len", "int" и другие стандартные функции,
# доступные без дополнительного импорта.
# Когда мы используем встроенные функции,
# Python автоматически находит их в этом пространстве имён,
# если они не переопределены в глобальной или локальной области.
#
# Объемлющая область видимости
#
# Объемлющая область видимости создаётся,
# когда одна функция определяется внутри другой.
# В этом случае внешняя функция формирует объемлющую область
# видимости по отношению к внутренней функции.
# Это позволяет внутренней функции использовать переменные,
# объявленные в объемлющей области, даже если они не определены
# в локальной области самой внутренней функции.
#
# Рассмотрим пример, когда создаётся функция "even",
# принимающая значение x (Рис.3).
#
# Далее подвинем так:
# функция "square" будет вычислять квадрат значения переменной "d",
# а функция "even" — проверять, является ли результат чётным (Рис.4).
#
# Рассмотрим пример,
# в котором переменная "d" создаётся в функции "even".
# Пусть "d" будет равна x, умноженному на 2.
# После этого можно проверить, делится ли "d" на 2 без остатка:
#
# Если d делится на 2 без остатка, выводится сообщение «Чётное».
# В противном случае выводится сообщение «Нечётное» (Рис.5).
#
# В обновлённой структуре функция "even" остаётся вспомогательной,
# ничего не возвращая, а функция "square" будет возвращать
# значение переменной "d" после выполнения необходимых вычислений (Рис.6).
#
# Функция "square" создаёт объемлющую область видимости
# для "even" (Рис.7), в то время как сама остаётся
# в локальной области глобального пространства.
# Это демонстрирует вложенные области видимости,
# где внешняя функция предоставляет переменные для внутренней,
# а внутренняя остаётся изолированной.
#
# Внутри функции "even" создаётся локальная область видимости,
# которая существует только во время выполнения функции
# и доступна только изнутри "even" (Рис.8).
#
# Когда внутри функции "even" требуется доступ к переменной,
# Python следует определённому приоритету поиска,
# начиная изнутри и двигаясь наружу (Рис.9).
#
# Этапы поиска переменной:
#
# 1) Локальная область видимости (Local):
# переменная сначала ищется внутри функции "even".
# Если она найдена, поиск прекращается.
#
# 2) Объемлющая область видимости (Enclosing):
# если переменной нет в "even",
# интерпретатор ищет её в объемлющей функции,
# которая находится уровнем выше. Это происходит,
# если even вложена в другую функцию.
#
# 3) Глобальная область видимости (Global):
# если переменная не найдена в объемлющей функции,
# Python проверяет глобальную область видимости,
# где находятся переменные, определённые на уровне модуля.
#
# 4) Встроенная область видимости (Built-in):
# если переменной нет и в глобальной области,
# интерпретатор обращается к встроенной области видимости,
# содержащей стандартные функции и объекты Python, такие как "print",
# "len", "int" и т.д.
#
# Однако внутри функции есть несколько особенностей поведения.
# Допустим, мы вызываем функцию «square».
# Давайте запишем вызов функции «even» и будем передавать
# в неё переменную «x» (Рис.10).
#
# При запуске программы (Рис.11) переменная "b" принимает значение 4,
# а функция выводит "чётное".
# Это происходит из-за порядка выполнения программы
# и механизма передачи данных между функциями.
#
# Когда в функцию "square" передаётся значение x = 2,
# переменная "d" внутри этой функции вычисляется как 2 ** 2 = 4.
# Это значение сохраняется для последующего возврата.
# Однако прежде чем вернуть "d", функция "square"
# вызывает функцию "even", передавая в неё значение x = 2.
#
# Внутри функции "even" создаётся новая локальная переменная d,
# которая вычисляется как "x * 2 = 2 * 2 = 4". Это переменная,
# существующая только в области видимости функции "even",
# и она не связана с переменной "d" из функции "square".
# После вычисления "d" в "even" программа проверяет,
# делится ли это значение на 2 без остатка. Так как "4 % 2 == 0",
# условие выполняется,
# и функция "even" выводит сообщение "чётное" на экран.
#
# Затем выполнение возвращается в "square",
# которая возвращает свою переменную "d", равную 4.
# Именно это значение сохраняется в глобальной переменной "b".
# Таким образом, "b" становится равной 4, а функция "even",
# будучи вызванной до возврата результата,
# отдельно выводит сообщение о чётности числа.
#
# Интересно отметить,
# что в данном случае обе переменные "d" (в функциях "square" и "even")
# получают одинаковое значение 4, но это совершенно разные переменные,
# каждая из которых существует только в своей
# локальной области видимости. Их совпадение обусловлено тем,
# что "2 ** 2" и "2 * 2" дают один и тот же результат.
# Однако при передаче другого значения "x" эти переменные
# могли бы принимать разные значения,
# демонстрируя принцип изоляции данных и последовательного
# выполнения кода в Python (Рис.12).
#
# Давайте напишем 4, запустим программу и увидим 16 (Рис.13).
#
# По логике может показаться,
# что переменная "d" должна была изменить
# своё значение и стать равной 8,
# поскольку функция "even" умножает x на 2. Однако этого не происходит,
# потому что функция even имеет своё собственное пространство имён.
# Внутри неё создаётся локальная переменная "d",
# существующая только в пределах этой функции (Рис.14).
#
# Но если мы уберём создание переменной "d" в функции "even"
# и запустим программу, ничего не изменится (Рис.15).
# Мы всё ещё видим сообщение «чётное» и "4 в квадрате — 16",
# потому что рассматриваем другую функцию,
# то есть поднимаемся на уровень выше.
#
# Область видимости в Python позволяет получить доступ
# к переменным объемлющей функции,
# если они не объявлены в локальной области текущей функции.
# В данном случае функция "even" получает доступ
# к переменной "d" из функции "square" (Рис.16).
#
# Если в глобальном пространстве объявить переменную "d = 5",
# программа всё равно будет работать правильно
# и результат останется неизменным,
# поскольку локальная область видимости
# функции "square" имеет приоритет над глобальной областью (Рис.17).
#
# Если удалить переменную "d" из функции "square",
# интерпретатор перейдёт на уровень выше и найдёт "d"
# в глобальной области видимости, где её значение равно 5 (Рис.18).
#
# Почему? Потому что вызывается функция "even".
# Мы проверяем наличие переменной "d" в ней.
# Если её там нет, мы смотрим в функции выше, в "square", и не находим.
# Поднимаемся ещё выше и, в итоге, находим её.
# Таким образом, мы берём значение оттуда.
#
# Эти области видимости позволяют нам «прыгать», так сказать,
# по пространству имён и просматривать значения у других объектов.
#
# Если мы создадим свой модуль, например, "module3",
# и создадим в нем переменную "d = 10" (Рис.19).
#
# В модуле "namespaces" добавим строку "from module3 import *",
# а переменную "d", объявленную ранее, удалим (Рис.20).
# Это действие импортирует все объекты из модуля "module3"
# в глобальное пространство имён модуля "namespaces".
# Теперь переменная "d" из "module3" будет доступна напрямую,
# без указания имени модуля.
#
# При запуске файла "namespaces" (Рис.21)
# на экране выводится "чётное". Это происходит потому,
# что переменная "d", импортированная из модуля "module3",
# равна 10, а "10 % 2 == 0", что соответствует чётному числу.
#
# При запуске программы (Рис.22) результат остаётся неизменным.
# Это связано с тем, что переменная "d" не найдена в локальной,
# объемлющей или глобальной области модуля "namespaces".
# Вследствие этого интерпретатор обращается к модулю "module3",
# откуда была импортирована "d", равная 10.
#
# Если в модуле "namespaces" объявить переменную "d = 8"
# и затем запустить программу (Рис.23),
# на экране отобразится значение 8,
# а функция выведет сообщение "чётное".
#
# Если записать "d = 7" в модуле "namespaces"
# и запустить программу (Рис.24), результат изменится
# на "нечётное". Это подтверждает,
# что поиск переменных в Python происходит изнутри наружу,
# согласно правилу LEGB (Local, Enclosing, Global, Built-in).
#
# Чтобы изменить глобальную переменную изнутри функции,
# необходимо использовать ключевое слово global.
# Это позволяет получить доступ к глобальной области видимости
# и переопределить переменную внутри функции.
#
# Что происходит при запуске программы?
#
# 1) Объявление d в глобальной области:
# до запуска программы переменная "d" равна 7,
# определённая в глобальной области модуля "namespaces".
#
# 2) Использование ключевого слова global:
#
# Внутри функции добавляется строка "global d", указывающая,
# что работа будет вестись с глобальной переменной "d".
# Python не создаёт локальную переменную "d",
# а обращается к глобальной "d", равной 7.
#
# 3) Переопределение переменной d:
#
# Переменная "d" возводится в квадрат с помощью "d = d ** 2".
# Теперь глобальная переменная "d" перезаписана и равна 49.
#
# 4) Вывод результата:
#
# В глобальной области переменная "d" изменила своё значение с 7 на 49.
# При следующем обращении к "d" программа выводит 49 (Рис.25).
#
# Принцип работы с глобальным пространством имён ясен: если требуется использовать или изменить глобальную переменную внутри функции, применяется ключевое слово global.
#
# Но как быть с объемлющим пространством имён,
# которое также может содержать собственные значения?
# В этом случае глобальная область не затрагивается.
# Например, предположим,
# что в объемлющей функции существует переменная "d",
# представляющая x в квадрате.
# Теперь стоит задача изменить это значение (Рис.26).
#
# Напишем "d=х/2", так уменьшим её в 2 раза (Рис.27).
#
# В текущем состоянии переменная "d" принадлежит локальной области
# видимости функции "even", существуя только во время её выполнения.
# Если требуется изменить переменную "d",
# находящуюся в объемлющей функции "square",
# нужно применить ключевое слово "nonlocal",
# а затем указать имя переменной,
# с которой будет происходить взаимодействие (Рис.28).
# Это позволяет изменить "d" из объемлющего пространства,
# не создавая новую локальную переменную в "even".
#
# Таким образом, в результате мы должны получить уже не 49,
# а 3,5. Почему?
#
# Давайте добавим "global d" (Рис.29).
#
# Использование "nonlocal" позволяет обратиться к переменной
# из объемлющей функции, изменив её значение.
# В данном случае мы пытаемся уменьшить значение переменной "d"
# в два раза. Однако,
# если одновременно присутствует ключевое слово "global",
# возникает ошибка выполнения (Рис.30).
#
# Значит, уберем "global", запустим код,
# и в результате получим "2.0" (Рис.31).
#
# Почему? Потому что мы передали 4 (Рис.32).
#
# Наша функция «square» возводит число 4 в квадрат и должна его вернуть.
# Однако перед тем, как вернуть значение, мы вызвали функцию "even",
# которая взяла это значение 4 (поскольку мы его передали),
# разделила на 2 и вывела текст «чётное» или «нечётное».
# При этом значение переменной "d" было изменено.
# Мы переопределили значение "d",
# и функция вернула уже не 4 или 4 в квадрате, а 4,
# уменьшенное в два раза. Если мы хотим работать с такими значениями,
# необходимо использовать "nonlocal",
# если в нашем коде есть функции внутри других функций.
#
# Пространства имён в Python — это системы управления данными,
# которые хранят объекты и связывают имена с их значениями,
# напоминая словари.
# Благодаря такой системе переменные с одинаковыми именами
# могут существовать в разных областях, не конфликтуя друг с другом.
#
# Ключевые аспекты работы с пространством имён:
#
# 1) Локальное и объемлющее пространство:
#
# Функции могут содержать локальные переменные,
# которые существуют только во время выполнения.
# Переменные в объемлющей функции могут быть изменены через "nonlocal",
# что позволяет управлять значениями, находящимися на уровне выше.
#
# 2) Глобальное пространство:
# переменные из глобальной области видимости можно изменить
# с помощью "global", чтобы не создавать новые локальные переменные.
#
# 3) Встроенное пространство:
# если переменная не найдена в локальной,
# объемлющей или глобальной области,
# Python обращается к встроенным функциям, таким как "print" или "len".
#
# Работа с вложенными функциями
#
# Функции могут быть вложены на нескольких уровнях.
# Например, функция even может содержать другую функцию,
# которая создаст собственное пространство имён,
# причём каждая из вложенных функций будет иметь доступ
# к своим объемлющим функциям, но не к глобальной области,
# если не указано обратное.
#
# Если функция "even" изменяет переменную из "square",
# но при этом создаёт локальную переменную с таким же именем,
# значение не изменится в объемлющей функции
# без использования "nonlocal".
#
# Важные замечания:
#
# Проблемы конфликта имён:
# при работе с импортом следует избегать дублирования имён,
# особенно при использовании "from module import *",
# поскольку это перекроет ранее объявленные переменные.
#
# Избегайте сложных структур:
# если код слишком сложный из-за многоуровневых вложений,
# стоит пересмотреть его структуру для улучшения читаемости и поддержки.
#
# Система пространств имён и областей видимости в Python
# обеспечивает гибкость, безопасность и управление данными,
# позволяя изменять переменные локально,
# глобально и в объемлющих функциях.
# Правильное понимание этой системы помогает управлять сложностью кода,
# минимизировать конфликты имён и строить масштабируемые программы.