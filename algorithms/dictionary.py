######################################  General  ###########################################


# A dictionary is a mutable (Changeable), unordered collection of many values. indexes for dictionaries can use different data types, not just integer. 
# Indexes for dictionaries are called keys, and a key with its associated value is called a key-value pair.

# python_dict={"name": "sachin", "headline": "Software Engineer", "github_username": "Sachin-chaurasiya"}

# sequence = [("name", "sachin"),("headline" , "Software Engineer"), ("github_username", "Sachin-chaurasiya")]

# python_dict = dict(sequence)
# name1 = python_dict["name"]
# name2 = python_dict.get('name')
# python_dict["headline"]="FrontEnd Developer"
# python_dict["profession"]="Software Engineer"
# python_dict.pop("name")
# python_dict.popitem()
# python_dict.clear()
# print(python_dict.keys())
# print(python_dict.values())
# print(python_dict.items())
# dict_variable = {key:value for (key,value) in dictonary.items()}
# dict_variable_mod = {key: sum(value) / len(value) for (key, value) in dictionary.items()}

###################################### Задача 1: Скрабл ######################################

# import re
# def isCyrillic (text):
#     return bool (re.search('[а-яА-Я]', text))
# points_en = {
#     1:   'AEIOULNSTR',
#     2:   'DG',
#     3:   'BCMP',
#     4:   'FHVWY',
#     5:   'K',
#     8:   'JZ',
#     10:  'QZ' 
# }
# points_ru = {
#     1:  'АВЕИНОРСТ',
#     2:  'ДКЛМПУ',
#     3:  'БГЁЬЯ',
#     4:  'ЙЫ',
#     5:  'ЖЗХЦЧ',
#     8:  'ШЭЮ',
#     10: 'ФЩЪ'
#     }

# text = input('Enter the word').upper()
# if isCyrillic(text):
#     print(sum([k for i in text for k, v in points_ru.items() if i in v]))
# else:
#   # print(sum([k for i in text for k, v in points_en.items() if i in v]))
    # total_sum = 0
    # for i in text:
    #     for k, v in points_ru.items():
    #         if i in v:
    #             total_sum += k


######################################  Задача 2: Рюкзак  ######################################

# things = {
#     'зажигалка':        20, 
#     'компас':           100, 
#     'фрукты':           500, 
#     'рубашка':          300,
#     'термос':           1000, 
#     'аптечка':          200, 
#     'куртка':           600, 
#     'бинокль':          400, 
#     'удочка':           1200,
#     'салфетки':         40, 
#     'бутерброды':       820, 
#     'палатка':          5500, 
#     'спальный мешок':   2250, 
#     'жвачка':           10
# }

# beg_weight = int (input("Enter how much you can carry")) * 100
# sorted_things = dict(sorted(things.items(), key=lambda x: -x[1]))
# for k, v in sorted_things.items():
#     if v <= beg_weight:
#         print(k, sep='\n')
#         beg_weight -= v


######################################  Задача 3. Email-адреса ######################################

# emails = {
#     'mgu.edu':      ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
#     'gmail.com':    ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
#     'msu.edu':      ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
#     'yandex.ru':    ['ekaterina_ivanova', 'glebova_nastya'],
#     'harvard.edu':  ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
#     'mail.ru':      ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']
# }

# # print(*sorted({i + '@' + k for k, v in emails.items() for i in v}), sep='\n')
#   unique_emails=set() # set{}, not dictionary
#   for k,v in emails.items():
#       for i in v:
#           email = i + '@' + k
#           unique_emails.add(email)
#   print(*sorted(unique_emails), sep='\n')

######################################  Задача 4. Word list ######################################

# def match_in_index(strlist):
#     word_list = {}
#     for index, string in enumerate(strlist):
#         for word in string.split():
#             if word not in word_list.keys():
#                 word_list[word] = [index]
#             else: 
#                 word_list[word].append(index)
#     return word_list

# print (match_in_index(['hello world','hello','hello cat','hellolot of cats']))

######################################  Задача 5: Продажи ########################################

# sales = {}
# for _ in range (int(input())):
#     name, item, count = input().split()
#     sales[name][item] = sales.setdefault(name, {}).setdefault(item, 0) + int(count)
# for key in sorted(sales):
#     print(f'{key}:')
#     for i in sorted(sales[key].items()):
#         print(*i)

######################################  Задача 6: Объединение словарей ########################################

# dict1 = {
#     'яблоки'    : 100, 
#     'бананы'    : 333, 
#     'груши'     : 200,
#     'апельсины' : 300, 
#     'ананасы'   : 45, 
#     'лимоны'    : 98,
#     'сливы'     : 76, 
#     'манго'     : 34, 
#     'виноград'  : 90, 
#     'лаймы'     : 230
# }

# dict2 = {
#     'яблоки'    : 300, 
#     'груши'     : 200, 
#     'бананы'    : 400,
#     'малина'    : 777, 
#     'ананасы'   : 12, 
#     'лаймы'     : 123, 
#     'черника'   : 111, 
#     'арбузы'    : 666
# }
# # merged_dict = {**dict1, **dict2}
# # print({dict1.get(key) for key in dict1})
# merged_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}
# print('Merged dictionary', merged_dict)

# ######################################  Задача 7: Коты и владельцы ########################################

# cats = [
#         ('Мартин',   5,   'Алексей',    'Егоров'),
#     	('Фродо',    3,   'Анна',       'Самохина'),
#     	('Вася',     4,   'Андрей',     'Белов'),
#     	('Муся',     7,   'Игорь',      'Бероев'),
#     	('Изольда',  2,   'Игорь',      'Бероев'),
#     	('Снейп',    1,   'Марина',     'Апраксина'),
#     	('Лютик',    4,   'Виталий',    'Соломин'),
#     	('Снежок',   3,   'Марина',     'Апраксина'),
#     	('Марта',    5,   'Сергей',     'Колесников'),
#     	('Буся',     12,  'Алена',      'Федорова'),
#     	('Джонни',   10,  'Игорь',      'Андропов'),
#     	('Мурзик',   1,   'Даниил',     'Невзоров'),
#     	('Барсик',   2,   'Виталий',    'Соломин'),
#     	('Рыжик',    7,   'Владимир',   'Медведев'),
#         ('Матильда', 8,   'Андрей',     'Белов'),
#     	('Гарфилд',  3,   'Александр',  'Березуев')
# ]
# result = {}
# for cat in cats:
#     temp = (cat[0] + ', ' + str(cat[1]))
#     result.setdefault(cat[2:], []).append(temp) # creates key and array value in dictionary
# for k, v in result.items():
#     print(' '.join(k) + ':', '; '.join(v))

#     # output - Марина Апраксина: Снейп, 1; Снежок, 3

# ######################################  Задача 8: Редкое слово  ########################################

# words = {}
# for i in input().split():
#     i = i.strip('.,!>:;-').lower()
#     words[i] = words.get(i, 0) + 1
# print(min(words.items(), key=lambda x: (x[1], x[0]))[0])

# ######################################  Задача 9: Дубликаты  ########################################

# sp = input().split()
# result = {}
# for i in sp:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1

# ######################################  Задача 10: Анаграммы  ########################################
# def a(word):
#     result = {}
#     for i in word.lower():
#         if i.isalpha():
#             result[i] = result.get(i, 0) + 1
#         return result
# print("YES" if a(input()) == a(input()) else "NO")
# a('hello world')

# ######################################  Задача 10: лямбда-функциям  ########################################
fahrenheit = {'t1': -30, 't2': -20, 't3': -10, 't4': 0}
total = 10
counter = 2
average = total / counter

# celsius = list(map(lambda x: (float(5)/9) * (x-32), fahrenheit.values()))
# celsius_dict = dict(zip(fahrenheit.keys(), celsius))
# print(celsius_dict)

# celsuis = {k:(float(5)/9)* (v-32) for (k,v) in fahrenheit.items()}
# print(celsuis)
print('this is', average)