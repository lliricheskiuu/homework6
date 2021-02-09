# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.

my_list = ['qwe', 'asd', 'zxc', 'vbn', 'fgh']

for index, item in enumerate(my_list):
    if index % 2:
        my_list[index] = my_list[index][::-1]

print(my_list)

###

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".

my_list = ['awe', 'asd', 'zxc', 'vbn', 'fgh']
result = []
for index, item in enumerate(my_list):
    if item[0] == 'a':
        result.append(item)

print(result)

###

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ['qwae', 'asd', 'zxac', 'vbn', 'fgh']
result = []

for index, item in enumerate(my_list):
    if item.count('a'):
        result.append(item)

print(result)

###

# 4. Дан список my_list в котором могум быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.

my_list = ['qwae', 23, 'asd', 12, 'zxac', 'vbn', 7, 'fgh']
result = []

for index, item in enumerate(my_list):
    if type(my_list[index]) == str:
        result.append(my_list[index])

print(result)

###

# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.

my_str = 'aacssfddt'
result = []

for symbol in my_str:
    if my_str.count(symbol) == 1:
        result.append(symbol)

print(result)

###

# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

str_1 = 'qwfsvmfebsml'
str_2 = 'fdnvburbubebv'
result = []

s_str_1 = set(str_1)
s_str_2 = set(str_2)

# for symbol_1 in s_str_1:
#     for symbol_2 in s_str_2:
#         if symbol_1 == symbol_2:
#             result.append(symbol_1)

for symbol in s_str_1.intersection(s_str_2):
    result.append(symbol)

print(result)

###

# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

str_1 = 'qwfsvmfebsmpl'
str_2 = 'fdpnvburbubebv'
result = []

s_str_1 = set(str_1)
s_str_2 = set(str_2)

# for symbol_1 in s_str_1:
#     if str_1.count(symbol_1) == 1:
#         for symbol_2 in s_str_2:
#             if str_2.count(symbol_2) == 1:
#                 if symbol_1 == symbol_2:
#                     result.append(symbol_1)

for symbol in s_str_1.intersection(s_str_2):
    if str_1.count(symbol) == 1 and str_2.count(symbol) == 1:
        result.append(symbol)

print(result)

###

# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность

person = {'last_name': 'Half',
           'name': 'Alex',
           'age': '25',
           'address': {'country': 'Ukraine',
                       'city': 'Odessa',
                       'street': 'Radyzniu'},
           'work': {'Availability': 'yes',
                   'position': 'Senior'}}

###

# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло

cake = {'constituents': {'layer': {'flour': '150g',
                                   'milk': '200ml',
                                   'butter': '100g',
                                   'egg': '1'},
                         'cream': {'sugar': '250g',
                                   'butter': '100g',
                                   'vanilla': '50g',
                                   'sour cream': '100g'},
                         'glaze': {'cacao': '20g',
                                   'sugar': '300g',
                                   'butter': '75g'}}}
