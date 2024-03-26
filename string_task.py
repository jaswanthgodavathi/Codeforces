a = input()
b = ['A', 'a', 'E', 'e', 'i', 'I', 'O', 'o', 'U', 'u', 'Y', 'y']
result = ''.join([char for char in a if char not in b])
upper = result.lower()
print('.',end = '')
result_string = '.'.join(upper)
print(result_string)
