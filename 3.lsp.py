"""
Liskov Substitution Principle

Uma subclasse deve ser substituível pela sua superclasse

R: A função animal_leg_count não funciona para a classe filha Snake, uma vez que o método leg_count da classe filha Snake não retorna (originalmente)
um número de pernas adequado. Nesse sentido, definimos que o método supracitado retorna 0, dessa maneira não violando o LSP.
"""
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        return self.name

    def leg_count(self) -> int:
        return 0

class Lion(Animal):
    def __init__(self):
        super().__init__('lion')

    def leg_count(self):
        return 4

class Snake(Animal):
    def __init__(self):
        super().__init__('snake')

    def leg_count(self):
        print('I have no legs, dummy')
        return 0


def animal_leg_count(animals: list):
    count = 0
    for animal in animals:
        count += animal.leg_count()
    return count



