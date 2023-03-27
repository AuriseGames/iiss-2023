import injector

class ComponenteMotor:
    def operar(self):
        pass

class Combustible(ComponenteMotor):
    def operar(self):
        print("El motor está funcionando con combustible.")

class Aceite(ComponenteMotor):
    def operar(self):
        print("El motor está funcionando con aceite.")

class Motor:
    @injector.inject
    def __init__(self, componente: ComponenteMotor):
        self.componente = componente

    def operar(self):
        print("El motor está en marcha.")
        self.componente.operar()

def configurar_inyector(binder, seleccion):
    if seleccion == "combustible":
        binder.bind(ComponenteMotor, to=Combustible)
    elif seleccion == "aceite":
        binder.bind(ComponenteMotor, to=Aceite)
    else:
        raise ValueError("Selección inválida")

if __name__ == "__main__":
    seleccion = input("¿Desea utilizar combustible o aceite? ")
    inyector = injector.Injector(lambda binder: configurar_inyector(binder, seleccion))
    motor = inyector.get(Motor)
    motor.operar()
    seleccion = input("¿Desea utilizar combustible o aceite? ")
    inyector = injector.Injector(lambda binder: configurar_inyector(binder, seleccion))
    motor = inyector.get(Motor)
    motor.operar()