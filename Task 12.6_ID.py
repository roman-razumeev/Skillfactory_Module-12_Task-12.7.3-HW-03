a = 5
b = 3+2
print('''a = 5
b = 3+2''')
print('a =', a, 'b =', b)
print('a is b ->', a is b)
print('a == b ->', a == b)
print('id(a) = ', id(a))
print('id(b) = ', id(b))
print('id(a) - id(b) = ', id(a) - id(b))
print('id(a) is id(b) ->', id(a) is id(b))
print('id(a) == id(b) ->', id(a) == id(b))

print('\n')

L = ['a', 'b', 'c']
print('L =', L)
print('id(L) =', id(L))
id_L_before = id(L)
L.append('d')
print("L.append('d')")
print('id(L) =', id(L))
id_L_after = id(L)
print('id_L_before is id_L_after ->', id_L_before is id_L_after)
print('id_L_before == id_L_after ->', id_L_before == id_L_after)
print('\n')


list_1 = ['a', 'b', 'c']
print("list_1 = ['a', 'b', 'c']")
list_2 = list_1
print('list_2 = list_1')
list_3 = list(list_1)
print('list_3 = list(list_1)')
print('list_1 = ', list_1)
print('list_2 = ', list_2)
print('list_3 = ', list_3)
print('id(list_1) =', id(list_1))
print('id(list_2) =', id(list_2))
print('id(list_3) =', id(list_3))
print('list_1 == list_2 ->', list_1 == list_2)
print('list_1 == list_3 ->', list_1 == list_3)

print('list_1 is list_2 ->', list_1 is list_2)
print('list_1 is list_3 ->', list_1 is list_3, '\n')

print('id(list_1) == id(list_2) ->', id(list_1) == id(list_2))
print('id(list_1) == id(list_3) ->', id(list_1) == id(list_3))
print('id(list_1) is id(list_2) ->', id(list_1) is id(list_2))
print('id(list_1) is id(list_3) ->', id(list_1) is id(list_3))


L = ['Hello', 'world']
M = L
print('''
L = ['Hello', 'world']
M = L''')
print('id_L =', id(L), '\nid_M =', id(M))
print('id(M) is id(L) ->', id(M) is id(L))
print('M is L ->', M is L)
# True
M.append('!')
print("M.append('!')")
print('id_L =', id(L), '\nid_M =', id(M))
print('id(M) is id(L) ->', id(M) is id(L))
print('M is L ->', M is L)
print('L =', L, '\nM =', M)
# ['Hello', 'world', '!']
print('M = L.copy()')
M = L.copy()
print('id_L =', id(L), '\nid_M =', id(M))
print('M is L ->', M is L)
# False
print('id(M) is id(L) ->', id(M) is id(L))
# False
print('\n')


shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
print('\nshopping_center =', shopping_center)
list_id_before = id(shopping_center[-1])
print('list_id_before = id(shopping_center[-1])')
print('list_id_before =', list_id_before)

shopping_center[-1].append("Uniqlo")
print('shopping_center[-1].append("Uniqlo")')
print('shopping_center =', shopping_center)
list_id_after = id(shopping_center[-1])
print('list_id_after = id(shopping_center[-1])')
print('list_id_after =', list_id_after)
print('list_id_before =', list_id_before)
print('\n')
# ('Галерея', 'Санкт-Петербург', 'Лиговский пр., 30', ['H&M', 'Zara', 'Uniqlo'])
print('list_id_before is list_id_after ->', list_id_before is list_id_after)
print('list_id_before == list_id_after ->', list_id_before == list_id_after)