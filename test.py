class kilo:
    count=0
    def vivod(self,name,age):
        self.name = name
        self.age = age
        kilo.count += 1

    @staticmethod
    def some_method():
        print("Статик")

    def __str__(self):
        return "Obj of kilo"

    def __init__(self, name="max"):
        kilo.count +=1
        self.__make="tyta"
        self._model=1999
        print(kilo.count)

    def start(self):
        msg2="a"
        return msg2

k = kilo()
print(k.count)
print(k._model)
k._model = 2000
print(k._model)