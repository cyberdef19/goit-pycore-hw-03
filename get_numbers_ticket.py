import random

"""
Функція get_numbers_ticket - генерує набір
унікальних випадкових чисел відповідно до заданих
параметрів.

max: int - максимальне можливе число у наборі
min: int - мінімальне можливе число у наборі
quantity: int - кількість чисел, що має бути згенеровано функцією

return: list - повертає список унікальних чисел
"""

def get_numbers_ticket(max: int, min: int, quantity: int) -> list:

    """
    Перевіримо чи параметр min не менше від 1 та max не може бути більше 1000
    """

    if min < 1:
        print("Параметр min не може бути менше 1")
        return []
    
    if max > 1000:
        print("Параметр max не може бути більше від 1000")
        return []
    
    if min >= max:
        print("Вочевидь, невірно вказані мінімальне та максимальне числа вибірки") 
        return []
    
    if max - min < quantity:
        print("Кількість унікальних чисел між min та max не може бути менше quantity")
        return []

    """
    Генеруємо унікальні числа. Якщо зегенероване випадкове число
    вже є у списку випадкових чисел, продовжуємо цикл, інакше 
    додаємо число у список
    """
    
    random_list = []

    while len(random_list) < quantity:
        random_digit = random.randrange(min, max)
        if random_digit in random_list:
            continue
        else:
            random_list.append(random_digit)
    
    """
    Повертаємо список випадкових чисел
    """

    return random_list

print(get_numbers_ticket(37, 1, 36))
    

    
