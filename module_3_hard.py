def calculate_structure_sum(data_structure):
    return


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])
                  ]

for i in range(len(data_structure)):  # Перечисление по количеству входных элементов списка
    elem_spi = data_structure[i]      # Получаем по очереди элемент списка
    print(type(elem_spi), '--', elem_spi, 'Длина элемента -', len(elem_spi))
    # print('Длина элемента -',len(data_structure[i]))
    # print(range(len(element)))
    # for j in range(len(element)):
    # print(element[j])

# 'Тип элемента -',
