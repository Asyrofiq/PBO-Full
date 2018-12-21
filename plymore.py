class Animal(object):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print self.name, 'says', self.sound()

class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)

    def sound(self):
        return 'meaw'

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)

    def sound(self):
        return 'Guuk'

class Snake(Animal):
    def __init__(self, name):
        super(Snake, self).__init__(name)

    def sound(self):
        return 'sssss'

if __name__ == '__main__':
    s = Dog('CJ')
    s.speak()
    c = Cat('Bessie')
    c.speak()
    Snake('Little Lamb').speak()
