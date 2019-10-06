import math


class Figure:

    def info(self):
        print("Родительский класс фигур")


class Volumetric(Figure):
    S = 1
    V = 1
    P = 1
    pi = 3.14

    def __init__(self,color):
        self.color = color

    def info(self):
        print("Объемные фигуры")


class Flat(Figure):
    S = 1
    P = 1

    def __init__(self, color):
        self.color = color

    def info(self):
        print("Плоские фигуры")


class S_Verh(Flat):

    def info(self):
        print("Фигуры с вершинами")


class Bez_Verh(Flat):

    pi = 3.14

    def info(self):
        print("Фигуры без вершин")


class Circle(Bez_Verh):

    Vpisan = False
    Opisan = False

    def info(self):
        print("Круг, наследник плоских фигур без вершин")
        if self.Vpisan == True:
            print("Круг вписан  ")
        if self.Opisan == True:
            print("Круг описан  ")

    def __init__(self, r, color, Vpisan = False, Opisan = False):
        print()
        super().__init__(color)
        self.radius = r
        self.diam = 2*self.radius
        self.Opisan = Opisan
        self.Vpisan = Vpisan

    def square(self):
        self.S = pow(self.radius,2)*self.pi
        print("Площадь (S) круга = ",self.S)

    def perim(self):
        self.P = 2*self.pi*self.radius
        print("Периметр (P) круга = ",self.P)


class Ellips(Bez_Verh):

    Focus_1 = [5,0]
    Foucs_2 = [-5,0]
    c = 5

    def info(self):
        print("Эллипс, наследник плоских фигур без вершин")

    def __init__(self,a,b,color):
        print()
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = math.sqrt(math.fabs(pow(self.a,2)-pow(self.b,2)))
        self.Focus_1 = [self.c, 0]
        self.Foucs_2 = [-self.c, 0]

    def square(self):
        self.S = self.a*self.b*self.pi
        print("Площадь (S) эллипса = ",self.S)

    def perim(self):
        self.P = 2*self.pi*math.sqrt((pow(self.a, 2)+pow(self.b, 2))/2)
        print("Периметр (P) эллипса = ", self.P)

    def focus(self):
        print("Фокусное расстояние эллипса = ", self.c)


class Parallel(S_Verh):

    def info(self):
        print("Параллелограмм, наследник плоских фигур с вершинами")

    def __init__(self,a,b,height,color):
        print()
        super().__init__(color)
        self.a = a
        self.b = b
        self.height = height

    def square(self):
        self.S = self.a*self.height
        print("Площадь (S) параллелограмма = ",self.S)

    def perim(self):
        self.P = (self.a+self.b)*2
        print("Периметр (P) параллелограмма = ",self.P)


class Triangle(S_Verh):

    a = 0
    b = 0
    c = 0
    alpha = 0
    beta = 0
    gamma = 0

    def __init__(self, x1, y1, x2, y2, x3, y3, color):
        print()
        super().__init__(color)
        self.A = {"x": x1, "y": y1}
        self.B = {"x": x2, "y": y2}
        self.C = {"x": x3, "y": y3}
        self.a = math.sqrt((pow((self.B["x"] - self.C["x"]), 2)) + (pow((self.B["y"] - self.C["y"]), 2)))
        self.b = math.sqrt((pow((self.A["x"] - self.C["x"]), 2)) + (pow((self.A["y"] - self.C["y"]), 2)))
        self.c = math.sqrt((pow((self.B["x"] - self.A["x"]), 2)) + (pow((self.B["y"] - self.A["y"]), 2)))
        self.beta = round(
            math.degrees(math.acos((pow(self.a, 2) + pow(self.c, 2) - pow(self.b, 2)) / (2 * self.a * self.c))))
        self.gamma = round(
            math.degrees(math.acos((pow(self.a, 2) + pow(self.b, 2) - pow(self.c, 2)) / (2 * self.a * self.b))))
        self.alpha = round(
            math.degrees(math.acos((pow(self.b, 2) + pow(self.c, 2) - pow(self.a, 2)) / (2 * self.c * self.b))))

    def info(self):
        print("Треугольник, наследник плоских фигур с вершинами")
        print("BC = ", self.a)
        print("AC = ",self.b)
        print("AB = ", self.c)
        print("alpha = ", self.alpha)
        print("beta = ", self.beta)
        print("gamma = ", self.gamma)

    def square(self):
        p = (self.a+self.b+self.c)/2
        self.S = math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        print("Площадь (S) треугольника = ", self.S)

    def perim(self):
        self.P = self.a+self.b+self.c
        print("Периметр (P) треугольника = ",self.P)

    def peres_median(self):
        x = (1/3)*(self.A["x"]+self.B["x"]+self.C["x"])
        y = (1/3)*(self.A["y"]+self.B["y"]+self.C["y"])
        print("Точка пересечения медиан треугольника - (",x,",",y,")")


class Сylinder(Volumetric):

    kosoy = False
    naklonnyi = False

    def __init__(self, height, radius, color, kos=False, nakl=False):
        super().__init__(color)
        self.height = height
        self.radius = radius
        self.kosoy = kos
        self.naklonnyi = nakl
        print()

    def info(self):
        print("Цилиндр, наследник объемных фигур")

    def s_bok(self):
        self.S = 2*self.pi*self.radius*self.height
        print("Площадь (S) боковой поверхности цилиндра = ", self.S)

    def vol(self):
        self.V = self.pi * pow(self.radius,2) * self.height
        print("Объем (V) цилиндра = ", self.V)

    def perim_bok(self):
        self.S = 2 * self.pi * self.radius * self.height
        D = self.S/self.height
        self.P = (D+self.height)*2
        print("Периметр (P) боковой поверхности цилиндра = ",self.P)


class Cube(Volumetric):

    diag = 0
    diag_grani = 0
    vpis_sfera = False
    opis_sfera = False

    def __init__(self, height, color, vpis_sf=False, opis_sf=False):
        print()
        super().__init__(color)
        self.diag = height*math.sqrt(3)
        self.diag_grani = height * math.sqrt(2)
        self.vpis_sfera = vpis_sf
        self.opis_sfera = opis_sf
        self.height = height

    def info(self):
        print("Куб, наследник объемных фигур")
        print("Диагональ куба = ", self.diag)
        print("Диагональ грани куба = ", self.diag_grani)
        if self.vpis_sfera == True:
            print("У куба есть вписанная сфера")
        if self.opis_sfera == True:
            print("У куба есть сфера описанная около него")


    def s_poverh(self):
        self.S = 6*pow(self.height,2)
        print("Площадь (S) поверхности куба = ", self.S)

    def vol(self):
        self.V = pow(self.height,3)
        print("Объем (V) куба = ", self.V)

    def perim(self):
        self.P = self.height*12
        print("Периметр (P) куба = ",self.P)


v = Volumetric("Green")

cyl = Сylinder(50, 5, "red")
cyl.info()
cyl.s_bok()
cyl.vol()
cyl.perim_bok()

cub = Cube(15, "yellow",True)
cub.info()
cub.s_poverh()
cub.vol()
cub.perim()

treyg = Triangle(5, 3, 1, 9, -3, 4, "blue")
treyg.info()
treyg.square()
treyg.perim()
treyg.peres_median()

parallelogram = Parallel(10,5,15,"coral")
parallelogram.info()
parallelogram.square()
parallelogram.perim()

krug = Circle(5,"green",True)
krug.info()
krug.square()
krug.perim()

ellps = Ellips(13, 4, "red")
ellps.info()
ellps.square()
ellps.perim()
ellps.focus()





