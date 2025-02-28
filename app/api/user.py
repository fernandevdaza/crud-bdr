from fastapi import APIRouter, Depends

from app.controllers.usuario_controller import crear_usuario, obtener_usuarios, actualizar_usuario, eliminar_usuario
from app.models.usuario import UsuarioCreate, UsuarioUpdate, UsuarioDelete

router = APIRouter()

@router.post("/create_user")
def create_user(user: UsuarioCreate):
    try:
        crear_usuario(user)
        return {"message": "Usuario creado exitosamente"}
    except Exception as e:
        return {"message": str(e)}

@router.get("/get_users")
def get_users():
    try:
        users = obtener_usuarios()
        return {"message": "Usuarios obtenidos exitosamente", "user": users}
    except Exception as e:
        return {"message": str(e)}

@router.put("/update_user")
def update_user(user: UsuarioUpdate):
    try:
        actualizar_usuario(user)
        return {"message": "Usuario actualizado exitosamente"}
    except Exception as e:
        return {"message": str(e)}

@router.delete("/delete_user")
def create_user(user: UsuarioDelete):
    try:
        eliminar_usuario(user)
        return {"message": "Usuario eliminado exitosamente"}
    except Exception as e:
        return {"message": str(e)}
