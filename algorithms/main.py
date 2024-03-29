
''' String Formating '''
# age = 26
# name = 'Swaroop'

# print('Why {} is having fan with {}?'.format(name, age))

# a, *b=[65,41,27,77]

# points = [ { 'x' : 2, 'y' : 3 }, { 'x' : 4, 'y' : 1 } ]
# points.sort(key=lambda i : i['y'])
# print(points)
''' For and Enumerate '''
# arr = [65,41,27,77]
# for i in range(len(arr)):
#     arr[i] *= 2
# arr = [ i * 2 for i in arr ]
# print(arr)

# arr = [[1, 2], [3, 4], [5, 6]]
# arr = [ j * 10 for i in arr for j in i if j % 2 == 0 ]

'''enumerate() can be used to iterate over elements in a sequence while keeping track of their indices.'''
# arr = [1, 2, 3, 4, 5, 6]
# for i, elem in enumerate(arr):
#     if elem % 2 == 0:
#         arr[i] *= 2
#     print(f"{i}:{elem}")
# print(arr)


# fruits = {'a':'apple', 'b':'banana', 'c':'cherry', 'd':'date'}
# for index, key in enumerate(fruits):
#     print(index, key, fruits[key])
#     0 a apple
#     1 b banana
#     2 c cherry
#     3 d date


''' Copy and Deepcopy 
    Функция d e e p c o p y  создает копию каждого объекта, при этом сохраняя внутреннюю
    структуру списка. Иными словами, если в списке существуют два элемента, ссылающиеся
    на один объект, то будет создана копия объекта, и элементы будут ссылаться на этот новый
    объект, а не на разные объекты.
'''
# x=[65,41,27,77]
# y=list(x) #or y=x[:] or y=x.copy() x is y-False
# y[1] = 100
# print('y', y) # y [65, 100, 27, 77]
# print('x', x) # x [65, 41, 27, 77]

# x = [1, [2, 3, 4, 5]]
# y = list(x)
# print('y', y) # y [1, [2, 3, 4, 5]]
# print('x', x) # x [1, [2, 3, 4, 5]] 
# x is y        # False
# y[1][1] = 100
# print('y', y) # y [1, [2, 100, 4, 5]]
# print('x', x) # x [1, [2, 100, 4, 5]] 

# import copy
# y=copy.deepcopy(x)
# y[1][1] = 200
# print('y-deepcopy', y) # y-deepcopy [1, [2, 200, 4, 5]]
# print('x-deepcopy', x) # x-deepcopy [1, [2, 100, 4, 5]]

''' Dictionaries deepcopy() 
При создании словаря в переменной сохраняется ссылка на объект, a не сам объект. Это
обязательно следует учитывать при групповом присваивании. Групповое присваивание
можно использовать для чисел и строк, но для списков и словарей этого делать нельзя. '''
# d1 = d2 = {"a":1, "b":2}
# d2["b"] = 10
# d1 is d2 # False
# print('d1', d1) # d1 {'a': 1, 'b': 10}
# print('d2', d2) # d2 {'a': 1, 'b': 10}
# d3 = {"a":1, "b":2}
# d4 = dict(d3) # or d4 = d3.copy() shallow copy
# d4['b'] = 10
# print('d3', d3) # d1 {'a': 1, 'b': 2}
# print('d4', d4) # d2 {'a': 1, 'b': 10}
# d5 = {"a":1, "b":[20, 30, 40]}
# d6 = dict(d5) # or d4 = d3.copy() shallow copy
# d6['b'][0] = 200
# print('d5', d5) # d5 {'a': 1, 'b': [200, 30, 40]}
# print('d6', d6) # d6 {'a': 1, 'b': [200, 30, 40]}

''' map(), zip(), filter() and reduce() '''
# def func(el1, el2, el3):
#     return el1 + el2 + el3
# arr1 = [23,34,45,11,22,33]
# arr2 = [45,56,67]
# arr3 = [56,67,78]
# print(list(map(func, arr1, arr2, arr3))) # [124, 157, 190]

# squared_numbers = list(map(lambda x: x**2, arr1))
# print(squared_numbers)

# arr4 = [x + y + z for (x,y,z) in zip(arr1, arr2, arr3)]
# print('arr4', arr4)                      # arr4 [124, 157, 190]

# def func1(elem):
#     return elem >= 150
# arr5 = list(filter(func1, arr4))
# print('arr5', arr5)

# from functools import reduce
# def func2(x, y):
#     print("{}, {}".format(x, y), end=' ') # 23, 34 57, 45 102, 11 113, 22 135, 33
#     return x + y
# sum = reduce(func2, arr1)
# print('sum', sum)

# arr = ["word1", "word2", "word3"]
# word = "-".join(arr)
# print('word', word)   # word word1-word2-word3
# arr1 = ["word1", "word2", "word3", 65, 45]
# word1 = "-".join( (str(i) for i in arr1) )
# print('word1', word1) # word1 word1-word2-word3-65-45
# word2 = word1[::-1]   # word2 54-56-3drow-2drow-1drow
# print('word2', word2)

''' Множество — это неупорядоченная последовательность уникальных элементов. Объявить
множество можно c помощью функции s e t (): 
| и union () — объединяют два множества:
a |= b и a.update(b) — добавляют элементы множества b во множество a:
a.difference(set([1,2,4])) — вычисляют разницу множеств:
a.difference_update(b) — удаляют элементы из множества a, которые сущест-
вуют и во множестве a, и во множестве b:
intersection() — пересечение множеств. Позволяет получить элементы, которые
существуют в обоих множествах:
'''


a = 10

def addition(x):
    y=x+10
    print(y)
    return y

addition(a)
print(a)



