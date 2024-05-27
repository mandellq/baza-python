# Create
a = [1, 2.1, 3]
tuple_a = tuple(a)
print(tuple_a)
print(type(tuple_a))
b = tuple('abc')
print(b)
# Retrive
a = (1, 1.1, 'a')
a[0] = 'a'
a = (1, 2, 3)
del a[0]
del a
Delete
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)
d = a * 2
print(d)
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
first_tuple = nested_tuple[0]
print(first_tuple)
element_T = first_tuple[0]
print(element_T)
last_tuple = nested_tuple[-1]
last_element = last_tuple[-1]
print(last_element)
count_ones = a.count(1)
print(count_ones)
index_two = a.index(2)
print(index_two)
a = {"а": 1}
b = {1: 1, 0: 2}
c = dict([("a", 1), ("b", 2)])
d = dict(a=1, b=2)
empty_dict = dict()
e = dict([['a', 1], ['b', 2]])
f = dict((('a', 1), ('b', 2)))
g = {1: 'a', 1.1: 'b', 'c': 3, (1, 2): [1, 2, 3], frozenset({1, 2}): (1, 2), 44: (112, 314), 'print': 4}
h = {'a': 3, 'b': 2}
print(a)
print(b)
print(c)
print(d)
print(empty_dict)
print(e)
print(f)
print(g)
print(h)
var_b = 'b'
print(a[var_b])
print(a[1])
Вера = {5: 1, 6: 11}
b = {'fat': 1, 'b': {'fe': 10}}
print(b['b']['fe'])  # Вывод: 10
a = {'a': 1, 'b': 1.1}
print(a.copy())
print(a.values())
print(a.keys())
print(a.items())
print(dict.fromkeys(['a', 'b', 'c'], 10))
products = {
    'апельсин': {'цена': 100, 'вес': 0.5},
    'банан': {'цена': 110, 'вес': 10}
}
цена_апельсина = products['апельсин']['цена']
print(цена_апельсина)
банан = products['банан']
print(банан)
вес_банана = банан['вес']
print(вес_банана)