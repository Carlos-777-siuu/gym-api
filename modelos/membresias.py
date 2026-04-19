class Membresia:
    def __init__(self,id,nombre_membresia,duracion_dias,precio_membresia):
        self.id = id
        self.nombre_membresia = nombre_membresia
        self.duracion_dias = duracion_dias
        self.precio_membresia = precio_membresia

    @classmethod
    def from_row(cls, row: dict):
        return cls(
            id= row["id"],
            nombre_membresia=row["nombre"],
            duracion_dias = row["duracion_dias"],
            precio_membresia = row["precio"]
        )

    def to_dict(self):
        return {
            "membresia_id": self.id,
            "nombre_membresia": self.nombre_membresia,
            "duracion_dias": self.duracion_dias,
            "precio_membresia": self.precio_membresia,
        }