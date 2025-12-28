class Pagos:
    def __init__(self,id,fecha_pago,monto):
        self.id = id
        self.fecha_pago = fecha_pago
        self.monto = monto 
    
    def to_dict(self):
        return {
                "pago_id": self.id,
                "fecha_pago": self.fecha_pago,
                "monto": self.monto
                }