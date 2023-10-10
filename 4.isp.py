"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC

#Aqui, ambas as classes concretas de janelas possuem métodos que nunca serão nescessários para ela, pelo fato de queles já pertencem a Interface.
#O ideal seria termos interfaces diferentes para janelas com menu, e janelas com tamanho variável

'''
class IJanela(ABC):
    def maximizar(self):
        raise NotImplementedError
    
    def minimizar(self):
        raise NotImplementedError
    
    def mostrar_menu(self):
        raise NotImplementedError
        
    def fechar(self):
        raise NotImplementedError

class JanelaTamanhoFixo(IJanela):
    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass

class JanelaSemMenu(IJanela):
    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass
'''
#SOLUÇÃO

class IJanelaComMenu(ABC):
    def mostrar_menu(self):
        raise NotImplementedError
        
    def fechar(self):
        raise NotImplementedError

class IJanelaTamanhoVariavel(ABC):
    def maximizar(self):
        raise NotImplementedError
    
    def minimizar(self):
        raise NotImplementedError

    def fechar(self):
        raise NotImplementedError

class JanelaTamanhoFixo(IJanelaComMenu):
    def mostrar_menu(self):
        pass
    def fechar(self):
        pass

class JanelaSemMenu(IJanelaTamanhoVariavel):
    def maximizar(self):
        pass
    def minimizar(self):
        pass