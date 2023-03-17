class Cliente:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    def pagar(self, monto):
        print(f"{self.nombre} paga {monto}")

class Compra:
    def __init__(self, cliente, monto):
        self.cliente = cliente
        self.monto = monto

    def realizar_pago(self):
        self.cliente.pagar(self.monto)

cliente = Cliente("Juan", "Calle 123")
compra = Compra(cliente, 100)
compra.realizar_pago()  # Output: "Juan paga 100"