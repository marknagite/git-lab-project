def find_max(numbers):
    """
    Находит максимальное число в списке.
    
    Args:
        numbers (list): Список чисел
        
    Returns:
        int/float: Максимальное число в списке
    """
    if not numbers:
        return None
    
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

# Пример использования
if __name__ == "__main__":
    sample_list = [3, 7, 2, 9, 1, 4]
    result = find_max(sample_list)
    print(f"Максимальное число в списке {sample_list} равно: {result}")