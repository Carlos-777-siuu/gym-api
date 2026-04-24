class Usuario:
    def __init__(self,id, nombre, email, rol, hash_contrasena, activo):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.rol = rol
        self.contrasena = hash_contrasena
        self.activo = activo
    @classmethod
    def from_row(cls, row: dict):
        return cls(
            id= row["id"],
            nombre=row["nombre"],
            email = row["email"],
            rol = row["rol"],
            hash_contrasena= row["contrasena"],
            activo = row["activo"]
        )

    def to_dict(self):
        return {
                "id": self.id,
                "nombre": self.nombre,
                "email": self.email,
                "rol": self.rol,
                "activo": self.activo
                }

