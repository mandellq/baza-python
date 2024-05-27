Create
b = set()
c = frozenset()
a = {1, 1.1, 'a', None, True, print}
d = frozenset({1, 1.1})
e = set([1, 2, 1])
f = set('слово')
g = frozenset('hello')
a = {1, 1, 1, 'a'}
a.add('привет!')
b = 1
a.add(b)
a = {1, 2, 3}
a.update({5, 2})
a = {1, 1.1, 'a'}
a.remove(1.1)
del a
a = {1, 2, 3, 4}
a.clear()
a = {1, 2, 3, 4}
element = a.pop()
a.remove(3)
a.discard(5)
a = {1, 2, 3}
b = {3, 5, 6}
c = a - b
print(c)
a -= b
a = {"сыр", "помидор", "молоко"}
b = {"яблоко", "хлеб", "молоко"}
a.intersection(b)
a.intersection_update(b)
a = {"сыр", "помидор", "молоко"}
b = {"яблоко", "хлеб", "молоко"}
a.union(b)
a.update(b)
a = {"сыр", "помидор", "молоко"}
b = {"яблоко", "хлеб", "молоко"}
c = {"сыр", "помидор", "молоко", "колбаса"}
a.difference_update(b)
a.symmetric_difference(b)
a.symmetric_difference_update(b)
a_b = a.intersection(b)
a_b_c = a_b.intersection(c)
unique_iliya = c.difference(b).difference(a)
print(unique_iliya)