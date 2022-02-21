from pessoa import Pessoa

p1 = Pessoa("Shaiane", 19, False, True)
print(p1.nome, p1.idade, p1.comendo, p1.falando)
p1.imprime_dados()

p2 = Pessoa("Eduardo", 19, True, False)
p2.falar('Oi, tudo bem?')
p2.parar_comer()
p2.comer('Manga')
p2.imprime_dados()
