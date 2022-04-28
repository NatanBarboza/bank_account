class People():
    def __init__(self, name, age:int, identity:str, address:str):
        self._name = name
        self._age = age 
        self.identity = identity
        self.address = address

    def __str__(self):
        return self._name

    @property
    def name(self):
        return print(self._name)

    @name.setter
    def name(self, name):
        print(name, type(name))
        if(type(name) == type(str())):
            self._name = name
        else:
            return print("Name must be type(str)")