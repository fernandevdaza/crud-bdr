from app.db import conectar_db
from app.models.usuario import Usuario, UsuarioCreate, UsuarioUpdate, UsuarioDelete


def crear_usuario(usuario: UsuarioCreate):
    conexion = conectar_db()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO Usuarios (nombre_usuario, clave_usuario) VALUES (%s, %s)"
            cursor.execute(sql, (usuario.nombre_usuario, usuario.clave_usuario))
        conexion.commit()
        return {"mensaje": "Usuario creado exitosamente"}
    finally:
        conexion.close()

def obtener_usuarios():
    conexion = conectar_db()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM Usuarios")
            usuarios = cursor.fetchall()
        return usuarios
    finally:
        conexion.close()

def actualizar_usuario(usuario: UsuarioUpdate):
    conexion = conectar_db()
    try:
        with conexion.cursor() as cursor:
            sql = "UPDATE Usuarios SET nombre_usuario=%s, clave_usuario=%s WHERE id_usuario=%s"
            cursor.execute(sql, (usuario.nombre_usuario, usuario.clave_usuario, usuario.id_usuario))
        conexion.commit()
        return {"mensaje": "Usuario actualizado correctamente"}
    finally:
        conexion.close()

def eliminar_usuario(user: UsuarioDelete):
    conexion = conectar_db()
    try:
        with conexion.cursor() as cursor:
            sql = "DELETE FROM Usuarios WHERE id_usuario=%s"
            cursor.execute(sql, (user.id_usuario,))
        conexion.commit()
        return {"mensaje": "Usuario eliminado correctamente"}
    finally:
        conexion.close()