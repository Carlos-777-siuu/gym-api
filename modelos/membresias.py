class Membresias:
    def __init__(self,nombre,duracion_dias,precio, pagos=None):
        self.nombre_membresia = nombre
        self.duracion_dias = duracion_dias
        self.precio_membresia = precio
        self.pagos_membresia = pagos or []

    def to_dict(self):
        return {
            "nombre_membresia": self.nombre_membresia,
            "duracion_dias": self.duracion_dias,
            "precio_membresia": self.precio_membresia,
            "pagos_membresia": self.pagos_membresia
        }