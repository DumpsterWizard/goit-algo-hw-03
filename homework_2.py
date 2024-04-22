import random


def get_numbers_ticket(min_num, max_num, quantity_num):
    if min_num < 1 or max_num > 1000 or min_num >= max_num or quantity_num <= 0 or quantity_num > (max_num - min_num + 1):
        return []
    unique_nums = set()

    while len(unique_nums) < quantity_num:
        unique_nums.add(random.randint(min_num, max_num))
    sorted_nums = sorted(list(unique_nums))

    return sorted_nums


min_num = 1
max_num = 49
quantity_num = 2
lottery_nums = get_numbers_ticket(min_num, max_num, quantity_num)
print("Your lottery nums are:", lottery_nums)

'''
На этой задаче пришлось попыхтеть. 
В третьей строчке мы делаем проверку введенных данных, и если какое-то из условий не подходит под условия функции, то
мы получаем пустой список. 
До (max - min + 1) так сам и не додумался. Не мог никак решить такую проблему - если квантити у нас больше макс велью, то ничего не возвращается.
На стак оверфлоу нашёл похожий немного вопрос с кодом, и решил вставить это выражениеи о чудо, оно подошло! Хотя до сих пор до конца не понимаю как оно работает...
Дальше цикл while у нас добавляет рандомные числа в наше множество в заданном диапазоне min max. Добавляет пока не достигнет значения quantity.
Далее множество мы конвертируем в список, чтобы его можно было отсортировать. 
Ну и мы возвращаем уже отсортированный список уникальных чисел в нашем диапазоне.
Задача посложнее чем первая, и опять же, с наскоку не решил бы ее и без дополнительных материалов.
'''
