immutable_var = 1, 2, 3, True, 'string'
print(immutable_var)
#immutable_var[1] = 5
#print(immutable_var) #элементы в кортеже неизменны
mutable_list = [1, 2, 3, True, 'string']
print(mutable_list)
mutable_list.append(False)
print(mutable_list)
mutable_list.remove(2)
print(mutable_list)