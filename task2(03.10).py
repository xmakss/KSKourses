import math


class Triangle:
    A = {"x": 5, "y": 3}
    B = {"x": 1, "y": 9}
    C = {"x": -3, "y": 4}
    a = math.sqrt((pow((B["x"] - C["x"]), 2)) + (pow((B["y"] - C["y"]), 2)))
    b = math.sqrt((pow((A["x"] - C["x"]), 2)) + (pow((A["y"] - C["y"]), 2)))
    c = math.sqrt((pow((B["x"] - A["x"]), 2)) + (pow((B["y"] - A["y"]), 2)))

    def square(self):
        p=(self.a+self.b+self.c)/2
        print("Площадь = ",math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c)))

    def perim(self):
        print("Периметр = ",self.a+self.b+self.c)

    def sost(self):
        print("\nТреугольник с координатами:\nA","(",self.A["x"],",",self.A["y"],")")
        print("B","(",self.B["x"],",",self.B["y"],")")
        print("C", "(", self.C["x"], ",", self.C["y"], ")")
        print("BC = ", self.a, "\tAC = ", self.b, "\tBA = ", self.c)

    def peres_median(self):
        x = (1/3)*(self.A["x"]+self.B["x"]+self.C["x"])
        y = (1/3)*(self.A["y"]+self.B["y"]+self.C["y"])
        print("Точка пересечения медиан - (",x,",",y,")")


treyg = Triangle()
treyg.square()
treyg.perim()
treyg.peres_median()
treyg.sost()
