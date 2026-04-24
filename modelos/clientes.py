class Cliente:
    def __init__(self, id, nombre, email, telefono, fecha_alta, fecha_vencimiento, usuario_id, activo):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.fecha_alta = fecha_alta
        self.fecha_vencimiento = fecha_vencimiento
        self.usuario_id = usuario_id
        self.activo = activo
    
    @classmethod
    def from_row(cls, row: dict):
        return cls(
            id= row["id"],
            nombre=row["nombre"],
            email = row["email"],
            telefono = row["telefono"],
            fecha_alta = row["fecha_alta"],
            fecha_vencimiento = row["fecha_vencimiento"],
            usuario_id = row["usuario_id"],
            activo = row["activo"]
        )
    
    def to_dict(self):
        return {
                "id": self.id,
                "nombre": self.nombre,
                "email": self.email,
                "telefono": self.telefono,
                "fecha_alta": self.fecha_alta,
                "fecha_vencimiento": self.fecha_vencimiento,
                "usuario_id": self.usuario_id,
                "activo": self.activo
                }
    
