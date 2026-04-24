--Modificamos constraints y anadimos columas de activo para aplicar borrado logico en pro de tener datos consistentes
--depends: 0000_creacion_esquema_inicial
ALTER TABLE clientes DROP CONSTRAINT fk_cliente_usuario;

ALTER TABLE clientes ADD CONSTRAINT fk_cliente_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id) 
ON DELETE RESTRICT; 

ALTER TABLE pagos DROP CONSTRAINT fk_cliente;
ALTER TABLE pagos DROP CONSTRAINT fk_membresia;
ALTER TABLE pagos DROP CONSTRAINT fk_pago_usuario;

ALTER TABLE pagos ADD CONSTRAINT fk_cliente FOREIGN KEY(cliente_id) REFERENCES clientes(id) 
ON DELETE RESTRICT;
ALTER TABLE pagos ADD CONSTRAINT fk_membresia FOREIGN KEY(membresia_id) REFERENCES membresias(id)
ON DELETE RESTRICT;
ALTER TABLE pagos ADD CONSTRAINT fk_pago_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
ON DELETE RESTRICT;


ALTER TABLE usuarios ADD COLUMN activo BOOLEAN NOT NULL DEFAULT TRUE;
ALTER TABLE clientes ADD COLUMN activo BOOLEAN NOT NULL DEFAULT TRUE;
ALTER TABLE membresias ADD COLUMN activo BOOLEAN NOT NULL DEFAULT TRUE;