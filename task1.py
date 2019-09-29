mass = [1, 2, 3, 4, 5, 2, 4, 1, 2, 10]
symb = input()
res = "Позиция:"
try:
    for i in range(len(mass)):
        if int(symb) == mass[i]:
            res += " [" + str(i) + "]"
    if len(res) == 8:
        print("Такого элемента нет")
    else:
        print(res)
except:
    print("Ошибка")
