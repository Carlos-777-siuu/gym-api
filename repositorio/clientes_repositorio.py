from modelos.clientes import Cliente

class ClientesRepositorio: 
    def __init__(self, conexion_db):
        self.conexion = conexion_db

    def registrar_cliente(self, cliente: Cliente, usuario_id) -> Cliente:
        cursor = self.conexion.cursor()
        sql_registrar_cliente = "INSERT INTO clientes(nombre, email, telefono, fecha_alta, fecha_vencimiento, usuario_id) VALUES (%s,%s,%s,%s,%s,%s) RETURNING id" 

        try:
            cursor.execute(sql_registrar_cliente, (cliente.nombre, cliente.email, cliente.telefono, cliente.fecha_alta, cliente.fecha_vencimiento, usuario_id))
            cliente.id = cursor.fetchone()[0]
        except Exception as e:
            raise e
        finally:
            cursor.close()

        return cliente
    
    def consultar_cliente(self, nombre_cliente:str) -> Cliente | None:
        cursor = self.conexion.cursor()
        sql_consultar_cliente = "SELECT id, nombre, email, telefono, fecha_alta, fecha_vencimiento FROM clientes WHERE nombre = %s"

        try:
            cursor.execute(sql_consultar_cliente, (nombre_cliente,))
            cliente_info = cursor.fetchone()
            if cliente_info is None:
                return None
            
            cliente: Cliente = Cliente(*cliente_info)
        except Exception as e:
            raise e
        finally:
            cursor.close()

        return cliente
    
    def consultar_todos_clientes(self) -> list[Cliente]:
        cursor = self.conexion.cursor()
        sql_consultar_todos_clientes = "SELECT id, nombre, email, telefono, fecha_alta, fecha_vencimiento FROM clientes"

        try:
            cursor.execute(sql_consultar_todos_clientes)
            clientes_info = cursor.fetchall()

            if clientes_info == None:
                return []
            
            clientes_lista = [Cliente(*cliente) for cliente in clientes_info]
        except Exception as e:
            raise e
        finally:
            cursor.close()

        return clientes_lista
    
    def actualizar_cliente(self, id_cliente: int, new_cliente_info:Cliente) -> None: 
        cursor = self.conexion.cursor()
        sql_actualizar_cliente = "UPDATE clientes SET "
    
    def historial_pagos_cliente(self, id_cliente: int) -> list[dict]:
        cursor = self.conexion.cursor()
        sql_hist_pagos_cliente = "SELECT pagos.fecha_pago, pagos.monto, membresias.nombre, membresias.duracion_dias, membresias.precio" \
        "FROM pagos INNER JOIN membresias ON pagos.membresia_id = membresias.id WHERE pagos.cliente_id = %s"

        try: 
            cursor.execute(sql_hist_pagos_cliente, (id_cliente,))
            historial_cliente = cursor.fetchall()

            if historial_cliente == None:
                return []


            lista_pagos = [ {"fecha pago": pagos[0], 
                             "Monto": pagos[1], 
                             "Membresia": pagos[2],
                             "Duracion": pagos[3],
                             "Precio": pagos[4]} for pagos in historial_cliente]

        except Exception as e:
            raise e
        finally:
            cursor.close()
        
        return lista_pagos
    
    


