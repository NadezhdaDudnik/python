class Animal:
    def make_a_sound(self):
        print('GAV')

class Cat(Animal):
    def tgdk(self):
        print('tgdk-tgdk')
    def make_a_sound(self):
        print('Meow')

class Dog(Animal):
    def run(self):
        print('run')

    def make_a_sound(self):
        print('gav-gav')

murzik = Cat()
murzik.tgdk()
murzik.make_a_sound()

sharik = Dog()
sharik.make_a_sound()
sharik.run()

# ---------

class Table():
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height =h

class DeskTable(Table):
    def square(self):
        return self.width * self.length

t1 = DeskTable(1.5, 0.8, 1.5)
print(t1.square())

#переопределение
class ComputerTable(DeskTable):
    def square(self, monitor = 0.0):
        return self.width * self.length - monitor
t2 = ComputerTable(1.5, 0.8, 1.5)
print(t2.square(0.4))

#переопределение класс table
class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        self.length = l
        self.width = w
        self.height = h
        self.places = p

    def params(self):
        print('length', self.length)
        print('width', self.width)
        print('heigth', self.height)
        print('places', self.places)

class KitchenTable2(Table):
    def __init__(self, l, w, h, p):
        Table.__init__(self, l, w, h, p)
        self.places = p

    def params(self):
        print('length', self.length, '\n')
        print('width', self.width, '\n')
        print('heigth', self.height, '\n')
        print('places', self.places)

t3 = KitchenTable(1.5, 0.8, 1.5, 5)
t4 = KitchenTable(1.5, 0.8, 1.5, 3)

t3.params()
t4.params()

