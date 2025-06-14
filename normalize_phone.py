import re

"""
Функція normalize_phone - нормалізує значення номера телефону,
що передається в якості параметра та повертає нормалізоване його значення
у вигляді +XXXXXXXXXXXX

phone: str - параметр, що представляє собою номер телефону

return: str - значення нормалізованого номера телефону
"""

def normalize_phone(phone: str) -> str:

    """
    Визначимо змінну pattern, значення якої є регулярним виразом,
    що допоможе отримати усі цифри з рядкової зміної phone
    """
    
    pattern_digits = r"(\d+)"

    """
    Знайдемо усі відповідності у рядку phone
    """

    matches = re.findall(pattern_digits, phone)

    """
    Якщо співпадінь немає, повертаємо None
    """

    if not matches:
        print("Не знайдено відповідностей у phone")
        return None
    """
    Конкатенація результату - цифри в єдиний рядок 
    """

    phone_concat = "".join(matches)

    """
    Перевіримо кількість символів у  рядку phone
    Якщо їх більше 12, некоректне значення у phone
    Якщо їх менше 9, знов некоректне значення у phone
    """

    if len(phone_concat) > 12 or len(phone_concat) < 9:
        print("Передане некоректне значення у функцію")
        return None
    

    """
    В нашому розпоряджені можуть бути номера з кількістю цифр від 12 до 9.
    Якщо цифр 9, додаємо міжнародний код 380; якщо цифр 12, то залишаємо як 
    є; якщо цифр 10 і попередній 0, то додаємо 38; якщо цифр 11 і попередня 8,
    то додаємо 3. 
    """
    if len(phone_concat) == 9:
        phone_concat = "380" + phone_concat
    
    elif len(phone_concat) == 10 and phone_concat.startswith('0'):
         phone_concat = "38" + phone_concat

    elif len(phone_concat) == 11 and phone_concat.startswith('8'):
        phone_concat = "3" + phone_concat
    else: 
        if len(phone_concat) != 12:
            print("Невірний формат номера телефона")
            return None
    
    """
    Додамо до отриманого нормалізованого номера телефона +
    """

    normalize_phone = "+" + phone_concat

    return normalize_phone



raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


    