class Usuario:
    def __init__(self, nombre, email, rol, contrasena, clientes=None, pagos=None):
        self.nombre = nombre
        self.email = email
        self.rol = rol
        self.contrasena = contrasena
        self.clientes_registrados = clientes or []
        self.pagos_registrados = pagos or []
    
    def to_dict(self):
        return {
                "nombre": self.nombre,
                "email": self.email,
                "rol": self.rol,
                "clientes_registrados": self.clientes_registrados,
                "pagos_registrados": self.pagos_registrados
                }

