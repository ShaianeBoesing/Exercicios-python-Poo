class Triangulo:
    def __init__ (self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
    
    
    def triangleType(self):
        if self.l1 == self.l2 == self.l3:
            type = 'Equilátero'
        elif self.l1 == self.l2 or self.l2 == self.l3 or self.l3 == self.l1:
            type = 'Isósceles'
        elif self.l1 != self.l2 != self.l3:
            type = 'Escaleno'
        
        return type
    