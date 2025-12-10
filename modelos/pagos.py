class Pagos:
    def __init__(self,fecha_pago,monto):
        self.fecha_pago = fecha_pago
        self.monto = monto 
    
    def to_dict(self):
        return {
                "fecha_pago": self.fecha_pago,
                "monto": self.monto
                }