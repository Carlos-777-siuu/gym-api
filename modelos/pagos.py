class Pago:
    def __init__(self,id,fecha_pago,monto, cliente_id, usuario_id, membresia_id):
        self.id = id
        self.fecha_pago = fecha_pago
        self.monto = monto
        self.cliente_id = cliente_id
        self.usuario_id = usuario_id
        self.membresia_id = membresia_id

    @classmethod
    def from_row(cls, row: dict):
        return cls(
            id= row["id"],
            fecha_pago= row["fecha_pago"],
            monto = row["monto"],
            cliente_id= row["cliente_id"],
            usuario_id = row["usuario_id"],
            membresia_id= row["membresia_id"]
        )
    
    def to_dict(self):
        return {
                "id": self.id,
                "fecha_pago": self.fecha_pago,
                "monto": self.monto,
                "cliente_id": self.cliente_id,
                "usuario_id": self.usuario_id,
                "membresia_id": self.membresia_id
                }