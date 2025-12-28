from modelos.usuarios import Usuario
class UsuarioRepositorio:
    def __init__(self, conexion_db):
        self.conexion = conexion_db

    def crear_usuario(self, usuario:Usuario, contrasena:str) -> Usuario:
        cursor = self.conexion.cursor()
        sql_crear_usuario = "INSERT INTO usuarios(nombre,email,rol,contrasena) VALUES(%s,%s,%s,%s) RETURNING id"

        try:
            cursor.execute(sql_crear_usuario, (usuario.nombre, usuario.email, usuario.rol, contrasena))
            usuario.id = cursor.fetchone()[0]
        except Exception as e: 
            print(f"No se puedo agregar al usuario dado el error: {e}")
            raise e
        finally:
            cursor.close()
        return usuario

    def buscar_usuario(self, nombre_usuario:str) -> Usuario:
        cursor = self.conexion.cursor()
        sql_buscar_usuario = "SELECT id, nombre, email, rol FROM usuarios WHERE nombre = %s"

        try:
            cursor.execute(sql_buscar_usuario, (nombre_usuario,))
            usuario_info = cursor.fetchone()

            if usuario_info is None:
                return None

            user = Usuario(*usuario_info)
        except Exception as e:
            raise e
        finally:
            cursor.close()

        return user
    
    def obtener_constrasena(self, id_usuario:int) -> str:
        cursor = self.conexion.cursor()
        sql_obtener_contrasena = "SELECT contrasena FROM usuarios WHERE id = %s"
        
        try:
            cursor.execute(sql_obtener_contrasena, (id_usuario,))
            contrasena = cursor.fetchone()[0]
            if contrasena is None:
                return None
        except Exception as e:
            raise e
        finally:
            cursor.close()

        return contrasena


    def mostrar_todos_usuarios(self) ->list[Usuario]:
        cursor = self.conexion.cursor()
        sql_buscar_todos = "SELECT id, nombre, email, rol FROM usuarios"

        try:
            cursor.execute(sql_buscar_todos)
            usuarios_encontrados = cursor.fetchall()
            
            if usuarios_encontrados is None:
                return []

            lista_usuarios = [Usuario(id=u[0], nombre=u[1], email=u[2], rol=u[3]).to_dict() for u in usuarios_encontrados]

        except Exception as e:
            print(f"No se pudo listar a los usuarios dado el error: {e}")
            raise e
        finally:
            cursor.close()

        return lista_usuarios

    def actualizar_usuario(self,id_usuario:int,ninfo_usuario: Usuario) -> None:
        cursor = self.conexion.cursor()
        sql_actualizar_usuario = "UPDATE usuarios SET nombre = %s, email = %s, rol = %s WHERE id = %s "

        try:
            cursor.execute(sql_actualizar_usuario, (ninfo_usuario.nombre, ninfo_usuario.email, ninfo_usuario.rol, id_usuario))
        except Exception as e:
            print(f"No se pudo actualizar al usuario dado el error: {e}")
            raise e
        finally:
            cursor.close()

    def eliminar_usuario(self, id_usuario: int) -> None:
        cursor = self.conexion.cursor()
        sql_eliminar_usuario = "DELETE FROM usuarios WHERE id = %s"

        try:
            cursor.execute(sql_eliminar_usuario, (id_usuario,))
        except Exception as e:
            print(f"No se pudo eliminar al usuario dado el erro: {e}")
        finally:
            cursor.close()

