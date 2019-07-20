class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(self.name.title()+"is sit here")

    def roll(self):
        print(self.name.title()+"is rolling")

my_dog = Dog('willian',2)

print('My dog name is '+my_dog.name.title())
print('My dog age is '+str(my_dog.age))
