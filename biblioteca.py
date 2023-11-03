class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print('O {} foi comer.'.format(self.nome))

    def som(self):
        print('O {} está fazendo um som'.format(self.nome))

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def som(self):
        print('O {} foi miando.'.format(self.nome))

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def som(self):
        print('O {} foi latindo'.format(self.nome))


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def som(self):
        print('O {} foi mugindo'.format(self.nome))


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def som(self):
        print('O {} fazendo barulho kk'.format(self.nome))