"""
Single Responsibility Principle

Uma classe deve ter somente uma responsabilidade
ou
Uma classe deve ter somente um motivo para mudar
"""

#(Aqu classe possui 2 responsabilidades muito distintas: armazenar o nome do animal, e salvar outros animais no DB. Seria ideal usar 2 classes diferetes.)
'''
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    # salva no DB
    def save(self, animal: Animal):
        pass 

'''



#SOLUÇÃO

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

class Animal_Saver:
    def __init__(self) -> None:
        pass

    # salva no DB
    def save(self, animal: Animal):
        pass




