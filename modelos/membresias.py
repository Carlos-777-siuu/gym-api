class Membresias:
    def __init__(self,id,nombre,duracion_dias,precio):
        self.id = id
        self.nombre_membresia = nombre
        self.duracion_dias = duracion_dias
        self.precio_membresia = precio

    @classmethod
    def from_row(cls, row: dict):
        return cls(
            id= row["id"],
            nombre_membresia=row["nombre_membresia"],
            duracion_dias = row["duracion_dias"],
            precio_membresia = row["precio_membresia"]
        )

    def to_dict(self):
        return {
            "membresia_id": self.id,
            "nombre_membresia": self.nombre_membresia,
            "duracion_dias": self.duracion_dias,
            "precio_membresia": self.precio_membresia,
        }