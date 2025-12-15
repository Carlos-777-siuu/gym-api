class Usuario:
    def __init__(self,id, nombre, email, rol):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.rol = rol

    def to_dict(self):
        return {
                "id": self.id,
                "nombre": self.nombre,
                "email": self.email,
                "rol": self.rol
                }

