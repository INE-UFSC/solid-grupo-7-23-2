"""
Open-Closed Principle

Classes devem estar fechadas para modificação, mas abertas para extensão
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        return
    
    # def get_name(self) -> str:
    #     pass

    def get_name(self) -> str:
        return self.__class__.__name__

    # def make_sound(self):
    #     if self.name == 'lion':
    #         print('roar')
    #     elif self.name == 'mouse':
    #         print('squeak')
    #     else:
    #         print('...')

    @abstractmethod
    def make_sound(self):
        pass


class Lion(Animal):
    def __init__(self):
        Animal.__init__(self)

    def make_sound(self):
        print('roar')


class Mouse(Animal):
    def __init__(self):
        Animal.__init__(self)

    def make_sound(self):
        print('squeak')

animals = [
    Lion(),
    Mouse()
]

def animal_sound(animals: list):
    for animal in animals:
        print(animal.get_name())
        animal.make_sound()

animal_sound(animals)


"""
Outro exemplo:

Imagine que você tem uma loja que dá desconto de 20% aos seus clientes favoritos
usando essa classe abaixo. Quando você decide dar 40% de desconto a clientes VIP,
você decide mudar a classe da seguinte forma:
"""

class Discount(ABC):
    def __init__(self, price):
        self.price = price

    # def give_discount(self):
    #         if self.customer == 'fav':
    #             return self.price * 0.2
    #         if self.customer == 'vip':
    #             return self.price * 0.4

    @abstractmethod
    def give_discount(self):
        pass

class FavDiscount(Discount):
    def __init__(self, price):
        Discount.__init__(self, price)
    
    def give_discount(self):
        return self.price * 0.2


class VipDiscount(Discount):
    def __init__(self, price):
        Discount.__init__(self, price)

    def give_discount(self):
        return self.price * 0.4

