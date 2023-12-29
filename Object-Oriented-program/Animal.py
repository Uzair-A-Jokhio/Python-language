class Dog:
    def __init__(self, name,bred,age):
        self.name = name
        self.bred = bred
        self.age = age
    def dog_age(self):
        return self.age * 7
    def __str__(self):
        return f"This is a dog {self.name} he is a {self.bred}, his age {self.age}. "



fox = Dog("hendrick","german sherpard", 3)

print(fox.dog_age())
print(fox.bred)
print(fox)


class Apple:
    def __init__(self, color, taste):
        self.color = color
        self.taste = taste

    def __str__(self):
        return f"this is an apple {self.color} and it is {self.taste}"