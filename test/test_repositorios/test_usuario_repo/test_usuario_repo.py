import pytest
from repositorio.usuarios_repositorio import UsuarioRepositorio
from modelos.usuarios import Usuario

class TestUsuarioRepositorio:

    def test_crear_usuario(self, db_conn):
        repo = UsuarioRepositorio(db_conn)

        usuario = Usuario(
            id=None,
            nombre="Carlos",
            email="carlos@test.com",
            rol="admin",
            hash_contrasena = "1234"
        )

        usuario_creado = repo.crear_usuario(usuario)

        assert usuario_creado.id is not None

        cursor = db_conn.cursor()
        cursor.execute(
            "SELECT nombre, email, rol FROM usuarios WHERE id=%s",
            (usuario_creado.id,)
        )

        fila = cursor.fetchone()
        assert fila == ("Carlos", "carlos@test.com", "admin")


    def test_buscar_usuario_existente(self, db_conn):
        repo = UsuarioRepositorio(db_conn)

        usuario = Usuario(None, "Ana", "ana@test.com", "user", "abc123")
        repo.crear_usuario(usuario)

        usuario_encontrado = repo.buscar_usuario("ana@test.com")

        assert usuario_encontrado is not None
        assert usuario_encontrado.nombre == "Ana"
        assert usuario_encontrado.email == "ana@test.com"
        assert usuario_encontrado.rol == "user"


    def test_buscar_usuario_inexistente(self, db_conn):
        repo = UsuarioRepositorio(db_conn)

        resultado = repo.buscar_usuario("no-existe")
        assert resultado is None


    def test_mostrar_todos_usuarios(self, db_conn):
        repo = UsuarioRepositorio(db_conn)

        repo.crear_usuario(
            Usuario(None, "U1", "u1@test.com", "user", "1")
        )
        repo.crear_usuario(
            Usuario(None, "U2", "u2@test.com", "admin", "2")
        )

        usuarios = repo.mostrar_todos_usuarios()

        assert len(usuarios) == 2
        nombres = {u.nombre for u in usuarios}
        assert nombres == {"U1", "U2"}


    def test_actualizar_usuario(self, db_conn):
        repo = UsuarioRepositorio(db_conn)

        usuario = Usuario(None, "Luis", "luis@test.com", "user", "admin123")
        repo.crear_usuario(usuario)

        nuevo_usuario = Usuario(
            id=None,
            nombre="Luis Mod",
            email="luis_mod@test.com",
            rol="admin",
            hash_contrasena=usuario.contrasena
        )

        repo.actualizar_usuario(usuario.id, nuevo_usuario)

        cursor = db_conn.cursor()
        cursor.execute(
            "SELECT nombre, email, rol FROM usuarios WHERE id=%s",
            (usuario.id,)
        )

        assert cursor.fetchone() == (
            "Luis Mod", "luis_mod@test.com", "admin"
        )


    def test_eliminar_usuario(self, db_conn):
        repo = UsuarioRepositorio(db_conn)

        usuario = Usuario(None, "Delete", "delete@test.com", "user", "pass")
        repo.crear_usuario(usuario)

        repo.eliminar_usuario(usuario.id)

        cursor = db_conn.cursor()
        cursor.execute(
            "SELECT id FROM usuarios WHERE id=%s",
            (usuario.id,)
        )

        assert cursor.fetchone() is None


