import random
import os

# Get the directory of this file
current_dir = os.path.dirname(__file__)

# Execute the bubble sort file
from sort.bubble_sort import bubble_sort

def shuffle_with_sort(array):
    """
    Embaralha um array usando conceitos de ordenação.
    Atribui valores aleatórios a cada item e depois ordena por esses valores.
    """
    if not array:
        return array
    
    # Cria pares (valor_aleatorio, item_original)
    paired_array = []
    for item in array:
        random_value = random.random()
        paired_array.append((random_value, item))
    
    # Ordena pelos valores aleatórios usando bubble sort
    sorted_pairs = bubble_sort(paired_array)
    
    # Extrai apenas os itens originais
    shuffled_array = [pair[1] for pair in sorted_pairs]
    
    return shuffled_array

def fisher_yates_shuffle(array):
    """
    Implementação do algoritmo Fisher-Yates shuffle.
    Mais eficiente que o shuffle_with_sort.
    """
    shuffled = array.copy()
    
    for i in range(len(shuffled) - 1, 0, -1):
        j = random.randint(0, i)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    
    return shuffled