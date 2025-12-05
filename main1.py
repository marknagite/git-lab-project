def find_min(numbers):  # Изменили имя функции
    """
    Находит минимальное число в списке.  # Изменили описание
    
    Args:
        numbers (list): Список чисел
        
    Returns:
        int/float: Минимальное число в списке  # Изменили возвращаемое значение
    """
    if not numbers:
        return None
    
    min_number = numbers[0]  # Изменили название переменной
    for num in numbers:
        if num < min_number:  # Изменили знак сравнения
            min_number = num
    return min_number

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
    print("=== Программа поиска минимального числа ===")  # Изменили заголовок
    
    # Получаем список от пользователя
    user_numbers = get_user_list()
    
    if user_numbers:
        # Находим минимум  # Изменили комментарий
        result = find_min(user_numbers)  # Изменили вызов функции
        print(f"\nСписок чисел: {user_numbers}")
        print(f"Минимальное число: {result}")  # Изменили вывод
    else:
        print("Не удалось получить список чисел.")