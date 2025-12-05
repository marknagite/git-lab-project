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

def get_user_list():
    """
    Запрашивает у пользователя ввод списка чисел.
    
    Returns:
        list: Список введенных чисел
    """
    numbers = []
    
    try:
        n = int(input("Введите количество элементов в массиве: "))
        
        if n <= 0:
            print("Количество элементов должно быть положительным!")
            return []
        
        print(f"Введите {n} чисел:")
        for i in range(n):
            while True:
                try:
                    num = float(input(f"Элемент {i+1}: "))
                    numbers.append(num)
                    break
                except ValueError:
                    print("Ошибка! Введите число.")
    
    except ValueError:
        print("Ошибка! Введите целое число для количества элементов.")
        return []
    
    return numbers

if __name__ == "__main__":
    print("=== Программа поиска максимального числа ===")
    
    # Получаем список от пользователя
    user_numbers = get_user_list()
    
    if user_numbers:
        # Находим максимум
        result = find_max(user_numbers)
        print(f"\nСписок чисел: {user_numbers}")
        print(f"Максимальное число: {result}")
    else:
        print("Не удалось получить список чисел.")