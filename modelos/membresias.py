class Membresias:
    def __init__(self,id,nombre,duracion_dias,precio):
        self.id = id
        self.nombre_membresia = nombre
        self.duracion_dias = duracion_dias
        self.precio_membresia = precio
        

    def to_dict(self):
        return {
            "membresia_id": self.id,
            "nombre_membresia": self.nombre_membresia,
            "duracion_dias": self.duracion_dias,
            "precio_membresia": self.precio_membresia,
            "pagos_membresia": self.pagos_membresia
        }