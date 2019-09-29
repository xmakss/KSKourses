mass = [-1, 2, -3, 4, -5, 2, -4, 1, -2, 10, 0]
print("Положительный список: "+str(list(filter(lambda x: x >= 0, mass))))
print("Отрицательный список: "+str(list(filter(lambda x: x < 0, mass))))
