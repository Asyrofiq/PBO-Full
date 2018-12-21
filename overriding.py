class Parent(object):
    def __init__(self):
        pass
    def Create(self):
        return 'sandi'

class Child(Parent):
    def __init__(self):
        self.Create()
    def Create(self):
        return 'Kata ' + super(Child, self).Create()


print Child().Create()
