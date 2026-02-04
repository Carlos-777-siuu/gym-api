from modelos.usuarios import Usuario
from psycopg.rows import dict_row
class UsuarioRepositorio:
    def __init__(self, conexion_db):
        self.conexion = conexion_db

    def crear_usuario(self, usuario:Usuario) -> Usuario:
        cursor = self.conexion.cursor(row_factory=dict_row)
        sql_crear_usuario = "INSERT INTO usuarios(nombre,email,rol,contrasena) VALUES(%s,%s,%s,%s) RETURNING id"

        try:
            cursor.execute(sql_crear_usuario, (usuario.nombre, usuario.email, usuario.rol, usuario.contrasena))
            usuario.id = cursor.fetchone()["id"]
        except Exception as e: 
            print(f"No se puedo agregar al usuario dado el error: {e}")
            raise e
        finally:
            cursor.close()
        return usuario

    def buscar_usuario(self, email_usuario:str) -> Usuario:
        cursor = self.conexion.cursor(row_factory=dict_row)
        sql_buscar_usuario = "SELECT id, nombre, email, rol, contrasena FROM usuarios WHERE email = %s"

        try:
            cursor.execute(sql_buscar_usuario, (email_usuario,))
            usuario_info = cursor.fetchone()

            if usuario_info is None:
                return None

            user = Usuario.from_row(usuario_info)
        except Exception as e:
            raise e
        finally:
            cursor.close()

        return user

    def mostrar_todos_usuarios(self) ->list[Usuario]:
        cursor = self.conexion.cursor(row_factory=dict_row)
        sql_buscar_todos = "SELECT id, nombre, email, rol, contrasena FROM usuarios"

        try:
            cursor.execute(sql_buscar_todos)
            usuarios_encontrados = cursor.fetchall()
            
            if not usuarios_encontrados:
                return []

            lista_usuarios = [Usuario.from_row(u) for u in usuarios_encontrados]

        except Exception as e:
            print(f"No se pudo listar a los usuarios dado el error: {e}")
            raise e
        finally:
            cursor.close()

        return lista_usuarios

    def actualizar_usuario(self,id_usuario:int,ninfo_usuario: Usuario) -> None:
        cursor = self.conexion.cursor(row_factory=dict_row)
        sql_actualizar_usuario = "UPDATE usuarios SET nombre = %s, email = %s, rol = %s, contrasena=%s WHERE id = %s "

        try:
            cursor.execute(sql_actualizar_usuario, (ninfo_usuario.nombre, ninfo_usuario.email, ninfo_usuario.rol,ninfo_usuario.contrasena, id_usuario))
        except Exception as e:
            print(f"No se pudo actualizar al usuario dado el error: {e}")
            raise e
        finally:
            cursor.close()

    def eliminar_usuario(self, id_usuario: int) -> None:
        cursor = self.conexion.cursor(row_factory=dict_row)
        sql_eliminar_usuario = "DELETE FROM usuarios WHERE id = %s"

        try:
            cursor.execute(sql_eliminar_usuario, (id_usuario,))
        except Exception as e:
            print(f"No se pudo eliminar al usuario dado el erro: {e}")
        finally:
            cursor.close()

