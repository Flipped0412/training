# 아래 클래스를 수정하시오.
class Animal:
    num_of_animals = 0

    def __init__(self):
        Animal.num_of_animals += 1


class Dog(Animal):
    def __init__(self):
        super().__init__()
    
    def bark(self):
        print('멍 멍 !')


class Cat(Animal):
    def __init__(self):
        super().__init__()

    def meow(self):
        print('야 옹 !')


class Pet(Dog, Cat):
    def __init__(self, sound):
        super().__init__()
        self.sound = sound

    def access_num_of_animal(self):
        return f'동물의 수는 {Animal.num_of_animals}마리 입니다.'

    def make_sound(self):
        print(self.sound)

    def play(self):
        print('애완동물과 놀기')

# dog = Dog()
# print(Pet.access_num_of_animal())
# cat = Cat()
# print(Pet.access_num_of_animal())

# dog1 = Dog()
# dog1.bark()

# cat1 = Cat()
# cat1.meow()

pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
