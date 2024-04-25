a = 'привет' #одинарные кавычки
b = "привет" #двойные кавычки
c = "я 'знаю' python" #комбинированые
d = 'я "знаю" python' #можно и так
e = 'я "знаю' python" #так нельзя
a = 123 #ЦЕЛОЧИСЛЕННЫЙ ТИП
a = str(a) # результат а
str([1, 1.1, 'a']) #результат "[1, 1.1 'a']"
str(True) #результат 'true'
str(None) #результат 'none'
a = 'привет'
b = 'Иван'
c = f"{a}я{b}" # "привет я Иван"
a = 'привет'
a = print(a)
a = print("Иван")
a = 'привет'
a[0] #п
a[1] #р
a[2] #и
a[3] #в
a[4] #е
a[5] #т
a[6] #ошибка выход за границы
a[-1] #т
a[-2] #е
a[-3] #в
a[-4] #и
a[-5] #р
a[-6] #п
a[-7] #ошибка вышли за границы
a = 'привет'
a[0] = 'б'
help(str)
a = 'привет мир'
a.count('р')
a.find('вет')
a.index('вет')
a.tfind('р')
a.rindex('р')
a = 'привет Мир'
a.removeprefix('пр')
a.removesuffix('ир')
a.replace('р', 'Р')
a.replace('р', 'Р', 1)
a.capitalize()
a.lower()
a.upper()
a.swapcase()
'привет'.isalpha()
'привет мир'.isalpha()
'123'.isdigit()
'123abc'.isalnum()
'привет'.isascii()
'\n\t\r'.isspace()
'123\n'.isprintable()
'привет мир'.istitle()
'привет мир'.islower()
'ПРИВЕТ МИР'.isupper()
'int'.isidentifier()
'привет мир'.startswith('пр')
'привет мир'.endswith('мир')
' \t привет \n'.strip()
'ww привет ww'.strip('w')
'ww привет ww'.rstrip('w')
'ww привет ww'.lstrip('w')
'привет мир'.partition('и')
'привет мир'.rpartition("и")
'www \t привет \n www'.split()
'www_привет_www'.split('_')
'www_привет_www'.rsplit('_' 1)
a = ['www','привет','мир']
'-'.join(a)
'abc'.encode()
a = 'w\nпривет\tw мир'.split()
'_'.join(a)
a = input('Введи данные разделенные пробелом').split()