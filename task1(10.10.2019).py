class Human:

    position = {'x': 0, 'y': 0}
    making = None

    def __init__(self, name):
        self.name = name

    def move(self,x,y):
        self.position['x'] = x
        self.position['y'] = y
        print("Координаты ,%s, X:%s , Y:%s"%(self.name,self.position['x'],self.position['y']))

    def make(self, obj):
        self.making.make(self.name, obj)


class Do:

    def make(self, name, obj):
        raise NotImplementedError()


class Built(Do):
    def make(self,name,obj):
        print("%s(строитель), воплотил в жизнь %s"%(name,obj))


class Create(Do):
    def make(self, name, obj):
        print("%s(ученый), придумал %s" % (name, obj))


class Test(Do):
    def make(self, name, obj):
        print("%s(тестировщик), проверил %s" % (name, obj))


class Realise(Do):
    def make(self, name, obj):
        print("%s(директор), выпустил %s" % (name, obj))


class Made_all(Do):
    def make(self, name, obj):
        print("%s(программист), придумал %s, реализовал, проверил и выпустил eё" % (name, obj))


class Scientist(Human):
    making = Create()


class Builder(Human):
    making = Built()


class Tester(Human):
    making = Test()


class Boss(Human):
    making = Realise()


class Programmer(Human):
    making = Made_all()


s = Scientist("Максим")
s.make("игру")

t = Tester("Кирилл")
t.make("игру")

b = Boss("Георгий")
b.make("игру")

bui = Builder("Денис")
bui.make("дом")
bui.move(5, 2)

prog = Programmer("Олег")
prog.make("соц. сеть")


