# #
# #итератор, генерирующий целые числа, начиная с указанного;
# #  итератор, повторяющий элементы некоторого списка, определённого заранее.
# # Подсказка: используйте функцию count() и cycle() модуля itertools.
# # Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# # Предусмотрите условие его завершения. #### Например, в первом задании выводим целые числа, начиная с 3.
# # При достижении числа 10 — завершаем цикл.
# # Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
#


from itertools import count
from itertools import cycle

def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)
my_count_func(start_number=int(input("enter start number: ")), stop_number=int(input("enter stop number: ")))
def my_cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i+=1
my_cycle_func([1, 2], int(input("enter iteration: ")))