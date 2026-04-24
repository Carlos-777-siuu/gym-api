class ExcepcionRepositorio(Exception):
    def __init__(self, mensaje: str):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class RegistroDuplicado(ExcepcionRepositorio):
    def __init__(self, campo:str):
        super().__init__(mensaje=f"Ya existe un registro con ese {campo}.")


class CampoFaltante(ExcepcionRepositorio):
    def __init__(self, campo_faltante: str):
        super().__init__(campo_faltante)



