from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        current_date = (datetime.today().date())
        difference = current_date - input_date
        print(difference.days)
    except ValueError:
        return ("Wrong date format! Please reenter it!")
    

get_days_from_today("2025-10-09")

'''
спасибо за наводку! Исправил

Сначала создаем функцию, с аргументом date. 
Далее переводим строку в значение datetime, на 5ой строке.
Узнаем значение таймдаты данного момента.
Создаем таймдельту путем вычитания input от current.
Далее возвращаем таймдельту в виде целого числа дней. 

'''