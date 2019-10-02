class MyClass:
    frst=0
    scnd=1

    def show(self):
        print("\nПервая переменная - ", self.frst)
        print("Вторая переменная - ", self.scnd)

    def remake(self,f,s):
        self.frst = f
        self.scnd = s

    def plus(self):
        print("\nСумма переменных - ", self.frst+self.scnd)

    def biggest(self):
        print("\nМаксимальная переменная - ", max(self.frst,self.scnd))

make = MyClass()
make.show()
make.remake(5,3)
make.show()
make.plus()
make.biggest()
