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
    def access_num_of_animal():
        return f'동물의 수는 {Animal.num_of_animals}마리 입니다.'


# dog = Dog()
# print(Pet.access_num_of_animal())
# cat = Cat()
# print(Pet.access_num_of_animal())

# dog1 = Dog()
# dog1.bark()

cat1 = Cat()
cat1.meow()