class Cliente:
    def __init__(self, id, nombre, email, telefono, fecha_alta, fecha_vencimiento):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.fecha_alta = fecha_alta
        self.fecha_vencimiento = fecha_vencimiento
    
    def to_dict(self):
        return {
                "id": self.id,
                "nombre": self.nombre,
                "email": self.email,
                "telefono": self.telefono,
                "fecha_alta": self.fecha_alta,
                "fecha_vencimiento": self.fecha_vencimiento,
                }
