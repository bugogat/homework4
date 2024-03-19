immutable_var = 1, 2, '3', True, False
print(immutable_var)
#immutable_var [2] = 100 - кортеж не поддерживает обращение по элементам.
mutable_list = ['apple', 'pineapple', 3, True]
print(mutable_list)
mutable_list[0] = 'tomato'
print(mutable_list)