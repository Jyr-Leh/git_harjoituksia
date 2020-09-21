class Person():

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
    
    def get_name(self):
        return self.name

    ## setter method to change the value name
    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    ## setter method to change the value age
    def set_age(self, age):
        self.age = age

    def __str__(self):
        return f'name: {}, age: {}'
