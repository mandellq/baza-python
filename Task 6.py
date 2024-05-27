str_ = "Строка с цифрой 1"
is_substr = "Строка" in str_
print("В строке есть слово 'Строка'?", is_substr)
#задача 2
number = 12
condition_1 = number % 2 == 0
condition_2 = number % 3 == 0

if condition_1 and condition_2:
    print("Число кратно 2 и 3")
else:
    print("Число не кратно 2 и 3")
#задача 3
month = 12
good_condition = month in [12, 1, 2]

if good_condition:
    print("Зима!!!")
#задача 4
hour = 7
good_condition = 6 <= hour < 12

if good_condition:
    print("Утро!!!")
#задача 5
list_ = [5, 6, 7, 8, 9]
result = (4 in list_) and (8 in list_)
print(result)