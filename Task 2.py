# CREATE
a = 'Привет'  # Одиночные кавычки
b = "привет"  # Двойные кавычки
c = "Я 'знаю' Python"  # Комбинирование
d = 'я "знаю" Python'  # Можно и так
e = 'я"знаю' Python"  #так нельзя
a = 123 # цифры
a = str(a) # результат а
str([1, 1.1, 'a'])
str(True)
str(None)
a = 'привет'
print(a)
print('ДЖО-ЖО')
a = 'привет'
print(a)
print('Иван')
а = "привет" a[0] # 'n' a[1] # 'p'
a[0] # 'п'
a[1] # 'р'
a[2] # 'и'
a[3] # 'в'
a[4] # 'e'
a[5] # 'T'
[6] # Ошибка, вышли за границы
a[-1] # 'T'
a[-2] # 'e'
a[-3] # 'B'
a[-4] # 'и'
a[-5] # 'p'
a[-6] # 'п'
а[-7] # Ошибка, вышли за границы
a = [1, 2, 3]
a.clear()
print(a)
a = [1, 2, 3]
removed_element = a.pop()
print(removed_element)
print(a)
a = [1, 'ab', 3]
removed_element = a.pop(1)
print(removed_element)
print(a)
a = [1, 2, 'ab']
a.pop(3)
print(a)
a = [1, 2, 'ab']
a.remove('ab')
print(a)
a = [1, 2, 'ab']
a.remove('cd')
a = [1, 2, 3]
a.append(4)
print(a)
a.append(['a', "b"])
print(a)
a = [1, 2, 3]
a.insert(0, 4)
print(a)
a = [1, 2, 3]
a.insert(3, 4)
print(a)
a = [1, 2, 3]
a.insert(-1, 4)
print(a)
a = [1, 2, 3]
a.extend([4, 5, 6])
print(a)
a = (1, 1.1, 'a')
del a[0]
del a[-1]
del a[-1]
del a
a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Можно так
b = [[0] * 3] * 3 # А можно так. Только в этом случае есть небольшая особенность.
a[0][0] = 1 # Здесь всё будет как и планировалось. "а" [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
b[0][0] = 1 # А здесь, не так как  планировалось. "b" [[1, 0, 0], [1, 0, 0], [1, 0, 0]]