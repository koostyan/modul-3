def print_params(a=1, b='строка', c=True):  # Функция с параметрами по умолчанию:
    print(a, b, c)


print_params()
print_params(2)
print_params(10, 'tree', False)
print_params(b=25)
print_params(c=[1, 2, 3])
print()

values_list = [7, False, 'Баффи']
values_dict = {'a': 1, 'b': 'строка', 'c': True}

print_params(*values_list)  # Распаковка параметров:
print_params(**values_dict)
print()
values_list_2 = [6, 'Баффи']  # Распаковка + отдельные параметры:
print_params(*values_list_2, 42)
