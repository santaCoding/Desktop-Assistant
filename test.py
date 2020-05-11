class Main:
    def add(self):
        self.item = Item('google', 'santa', '1234')

class ItemDescriptor:
    def __get__(self, instance, owner):
        print('__get__')
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('__set__')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        print(name)
        self.name = name

class Item:
    site, login, password = ItemDescriptor(), ItemDescriptor(), ItemDescriptor()
    def __init__(self, site, login, password):
        self.site = site
        self.login = login
        self.password = password

m = Main()
m.add()
print(m.item.site)