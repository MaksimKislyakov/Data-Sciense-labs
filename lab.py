import numpy as np

def one_hot_encoding(labels):
    # Находим количество уникальных классов (максимальное значение + 1)
    num_classes = np.max(labels) + 1
    
    # Создаем двумерный массив с нулями и заполняем его one-hot представлением
    one_hot = np.zeros((len(labels), num_classes), dtype=int)
    
    # Проставляем 1 в соответствующих позициях
    for idx, label in enumerate(labels):
        one_hot[idx, label] = 1
    
    return one_hot

labels = [0, 2, 3, 0]
one_hot_encoded = one_hot_encoding(labels)
print("One-hot encoding:\n", one_hot_encoded)
