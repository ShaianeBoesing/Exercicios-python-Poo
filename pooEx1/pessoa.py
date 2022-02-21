class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando


    def outroMetodo(self):
        print(f'...objeto cujo atributo é {self.nome} está executando outro método da classe Pessoa')
    
    
    def comer(self, comida):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        
        print(f'{self.nome} está comendo {comida}.')
        self.comendo = True
    
    def parar_comer(self):
        if self.comendo:
            self.comendo = False
            print(f'{self.nome} parou de comer.')
            return
        print(f'{self.nome} não está comendo.')
    
    def falar(self, palavras):
        if self.falando == True:
            print(f'{self.nome} já está falando')
            return
        
        print(f'{self.nome} está falando "{palavras}".')
        self.falando = True
        
    def parar_falar(self):
        if self.falando:
            self.falando = False
            print(f'{self.nome} parou de falar.')
            return
        print(f'{self.nome} não está falando.')


    
    def imprime_dados(self):
        print(f'''{self.nome} tem {self.idade} anos.
{self.nome} está comendo? {self.comendo}.
{self.nome} está falando? {self.falando}
''')
        
        