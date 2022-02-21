from triangulo import Triangulo

correctValues = False

while not correctValues:
    try:
        l1, l2, l3 = list(map(int, input("Informe os três lados de um triângulo em cm: ").split()))
        correctValues = True
    except:
        print("Quantidade inválida. Tente novamente \n")

def isTriangle(l1, l2, l3):
    if (l1 + l2) > l3:
       return True
    return False

if isTriangle(l1, l2, l3):
    t1 = Triangulo(l1, l2, l3)
    type = t1.triangleType()
    print(type)
else:
    print("Não é um triângulo")
    
    