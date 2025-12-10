class Clientes:
    def __init__(self, nombre, email, telefono, fecha_alta, fecha_vencimiento,pagos=None):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.fecha_alta = fecha_alta
        self.fecha_vencimiento = fecha_vencimiento
        self.pagos_realizados = pagos or []
    
    def to_dict(self):
        return {
                "nombre": self.nombre,
                "email": self.email,
                "telefono": self.telefono,
                "fecha_alta": self.fecha_alta,
                "fecha_vencimiento": self.fecha_vencimiento,
                "pagos": self.pagos_realizados
                }
