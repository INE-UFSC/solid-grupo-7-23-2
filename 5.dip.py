"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""
#No código original, Player e StatsReporter, 2 classes concretas, dependem uma da outra. Ao invés disso, fizemos com que Stats Reporter dependesse uma classe abstrata ICharacter
'''class Player:
    def __init__(self, name):
        self.stats = StatsReporter(self)
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name

class StatsReporter:
    def __init__(self, char: Player):
        self.char = char

    def report(self):
        print(f'Name:{self.char.name()}')
        print(f'HP:{self.char.hp()}')
        '''

#SOLUÇÃO

from abc import ABC, abstractmethod

class ICharacter(ABC):

    @abstractmethod
    def hp(self):
        pass
    @abstractmethod
    def name(self):
        pass

class Player (ICharacter):
    def __init__(self, name):
        self.__name = name
        self.__hp = 100
        self.__speed = 1
        super().__init__()

    @property
    def name(self):
        return self.__name
    
    @property
    def hp(self):
        return self.__hp

class StatsReporter:
    def __init__(self, char: ICharacter):
        self.char = char

    def report(self):
        print(f'Name:{self.char.name()}')
        print(f'HP:{self.char.hp()}')
