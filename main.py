# # Метод read ЧТЕНИЕ ФАЙЛА
# f = open('file1.txt')
# x = f.read()
# print(x)
# f.close()

# # метод readline
# f = open('file1.txt')
# x = f.readline()
# x2 = f.readline()
# x3 = f.readline()
# print(x)
# print(x2)
# print(x3)
# f.close()

# # метод readlins() считывает все строки в виде списка
# f = open('file1.txt')
# res = f.readlines()
# # print(res)
# print(res[0])
# # print(type(res))
# f.close()

# f = open('file1.txt')
# x = f.read()
# lines = x.split('\n')
# print(lines[1])
# f.close()

# # Относительный путь - от текущего места - указываем папку/имя файла
# f = open('inside/file.txt')
# print(f.read())
# f.close()

# # Абсолютный путь - полное указание пути к файлу
# f = open(r'D:\New\Read file\inside\file.txt')
# print(f.read())
# f.close()

# # ЗАПИСЬ В ФАЙЛ
# # Запись по 1й строчке
# with open('write.txt', 'w') as file:
#     file.write('7\n')
#     file.write('8\n')

# # ЗАПИСАТЬ НЕСКОЛЬКО СТТРОК СРАЗУ writelines() принимает итерируемый объект - список или кортеж
# with open('write.txt', 'w') as file:
#     file.writelines(['a\n', 'b\n', 'c\n'])

# # Запись, чтобы данные оставались 'a'
# with open('write.txt', 'a') as file:
#     file.write('d')

# # ПОСТРОИТЬ ПУТЬ независящий от ОС import os
# import os
# x = os.getcwd()
# folder_name = ('inside')
# file_name = ('file.txt')
# full_path = os.path.join(x, folder_name, file_name)
# file = open(full_path)
# print(file.read())
# file.close()

# # КОДИРОВКА
# with open('RU.txt', 'rt', encoding='utf8') as file:
#     print(file.read())

# # РЕШЕНИЕ ПРИМЕРА data.txt
# deps = []
# with open('data.txt', 'rt') as file:
#     for l in file:
#         department_name = l.strip()
#         dep = {"name": department_name, "employees": []}
#         employees_count = file.readline()
#         for i in range(int(employees_count)):
#             emp = file.readline()
#             name, last_name, date, city = emp.strip().split(' | ') 
#             dep["employees"].append({"name": name, "last_name": last_name, 'date': date, 'city': city})
#         blank_line = file.readline()
#         deps.append(dep)   
# print(deps)


