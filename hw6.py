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