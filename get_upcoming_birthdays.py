from datetime import datetime
import math

"""
Функція get_upcoming_birthdays повертає список співробітників,
котрі мають дні народження в найближчі 7 днів

users: list - містить список співробітників об'єктів у вигляді асоційованого списка з ключами
name - ім'я співробітника та birthday - дата народження у вигляді YYYY.MM.DD

return: list - повертає список асоційованих об'єктів співробітників, у кого в найближчі 7 дні день народження
"""

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:

    result_users = []
    
    """
    Отримаємо сьогоднішню дату
    """
    today_date = datetime.today().date()

    """


    Отримуємо об'єкт datetime для дати з users 
    і визначимо які співробітники мають шанс отримати поздоровлення в наступні 7 днів
    Визначимо також кількість високосних літ між датою дня народження та сьогоднішньою датою
    Отримаємо об'єкт типу deltatime, визначивши кількість днів між датою народження та сьогоднішньою датою
    Поділемо кількість отриманих днів за моделум на 365 днів і визначимо скільки реальних днів 
    між сьогоднішнім числом та датою народження, віднявши також у якості поправки кількість 
    днів, що додалися за високосні роки
    """
    
    for val in users:
        birthday = datetime.strptime(val["birthday"], "%Y.%m.%d").date()
        diff_years = today_date.year - birthday.year
        leap_years = round(diff_years/4) 
        diff_date = today_date - birthday
        days = diff_date.days%365 - leap_years

        """
        Визначаємо чи потрапляє обрана дата у інтервал в 7 наступних днів
        """

        if days <= 7 and days > 0:
            user = {
                'name': val['name'],
                'birthday_congratulation': val["birthday"]
            }
            result_users.append(user)
    return result_users
            
    
users = [
    {"name": "John Doe", "birthday": "1985.06.10"},
    {"name": "Jane Smith", "birthday": "1990.01.31"},
    {"name": "Jane Smither", "birthday": "1979.06.12"},
    {"name": "J.H Robertson", "birthday": "1980.06.16"},
    {"name": "Jane Smith", "birthday": "1965.06.01"}
]

print(get_upcoming_birthdays(users))



