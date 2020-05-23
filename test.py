class F:
    def __init__(self):
        self.value = 2
        self.name = 'A'
        print(self.__dict__)
        if self.__dict__['name'] is None:
            print('name is None')

f = F()