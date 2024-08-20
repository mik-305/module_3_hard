def calculate_nested_sum(data_structure):
    total_sum = 0
    if isinstance(data_structure,(list, tuple, set)):            # Если список, кортеж, множество
        for item in data_structure:
           total_sum = total_sum + calculate_nested_sum(item)
    elif isinstance(data_structure, dict):                      # Если словарь
        for key, value in data_structure.items():               # Разбираем словарь на ключ и значение
            total_sum = total_sum + calculate_nested_sum(key)
            total_sum = total_sum + calculate_nested_sum(value)
    elif isinstance(data_structure, int):                       # Если целое число
        total_sum = total_sum + data_structure
    elif isinstance(data_structure, str):                       # Если строка
        total_sum = total_sum + len(data_structure)
    return total_sum

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
print('Итоговая сумма :',calculate_nested_sum(data_structure))
