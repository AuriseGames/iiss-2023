class Aceite:
    def operar(self):
        print("El motor está funcionando con aceite.")
        
class Combustible:
    def operar(self):
        print("El motor está funcionando con combustible.")

def usa_aceite(cls):
    cls.dependency = Aceite()
    return cls

def usa_combustible(cls):
    cls.dependency = Combustible()
    return cls

@usa_aceite
class Motor1:
    def operar(self):
        self.dependency.operar()
        
@usa_combustible
class Motor2:
    def operar(self):
        self.dependency.operar()
        
class Motor3:
    def operar(self):
        self.dependency.operar()


motor1 = Motor1()
motor1.operar() # Output: El motor está funcionando con aceite.
motor2 = Motor2()
motor2.operar() # Output: El motor está funcionando con combustible.
motor3 = Motor3()
motor3.operar() # Output: AttributeError: 'Motor3' object has no attribute 'dependency'
