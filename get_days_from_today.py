from datetime import datetime
import re

"""
Функція для розрахунку кількості днів між поточною та 
заданою датами. 
param: date: str - рядок з шаблоном "PPPP-ММ-ДД"
return: int - ціле число як розрахунок між поточною
датою та вказаною користувачем датою.
"""

def get_days_from_today(date: str) -> int:

    """
    Визначимо чи отриманий рядок переданий у функцію
    у необхідному форматі
    """
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    match = re.search(pattern=pattern, string=date)
    if not match:
        print("Вкажіть вірне значення дати відповідно до шаблону")
        return None
    
    """
    Перетворимо рядок date на об'єкт типу datetime
    """
    date_split = date.split(sep='-')
    date_time = datetime(year=int(date_split[0]), month=int(date_split[1]), day=int(date_split[2]))

    """
    Отримаємо значення поточної дати
    """

    date_now = datetime.now()

    """
    Отримаємо різницю між датами, якщо date_time пізніше ніж поточна - результат від'ємний
    """

    date_diff = date_now - date_time

    """
    Повернемо кількість днів в об'єкті date_diff
    """

    return date_diff.days


print(get_days_from_today("2023-06-03"))

    

