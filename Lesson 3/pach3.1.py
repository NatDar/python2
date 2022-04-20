def div(*args):

    try:
        arg1 = int(input("Ввести делимое"))
        arg2 = int(input("Ввести делитель"))
        res = arg1 / arg2
    except ValueError:
        return "Ошибка значения"
    except ZeroDivisionError:
        return "Внимание делитель! 0 не может быть делителем!"
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Внимание! Делитель не может быть 0")
    return res



print(f'результат  {div()}')