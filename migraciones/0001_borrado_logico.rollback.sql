ALTER TABLE usuarios DROP COLUMN activo;
ALTER TABLE clientes DROP COLUMN activo;
ALTER TABLE membresias DROP COLUMN activo;

ALTER TABLE pagos DROP CONSTRAINT fk_cliente;
ALTER TABLE pagos DROP CONSTRAINT fk_membresia;
ALTER TABLE pagos DROP CONSTRAINT fk_pago_usuario;

ALTER TABLE pagos ADD CONSTRAINT fk_cliente 
    FOREIGN KEY(cliente_id) REFERENCES clientes(id) ON DELETE SET NULL;
ALTER TABLE pagos ADD CONSTRAINT fk_membresia 
    FOREIGN KEY(membresia_id) REFERENCES membresias(id) ON DELETE SET NULL;
ALTER TABLE pagos ADD CONSTRAINT fk_pago_usuario 
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id) ON DELETE SET NULL;

ALTER TABLE clientes DROP CONSTRAINT fk_cliente_usuario;
ALTER TABLE clientes ADD CONSTRAINT fk_cliente_usuario 
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id) ON DELETE SET NULL;