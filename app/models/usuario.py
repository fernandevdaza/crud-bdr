from pydantic import BaseModel

class Usuario(BaseModel):
    id_usuario: int
    nombre_usuario: str
    clave_usuario: str

class UsuarioCreate(BaseModel):
    nombre_usuario: str
    clave_usuario: str

class UsuarioUpdate(BaseModel):
    id_usuario: int
    nombre_usuario: str
    clave_usuario: str

class UsuarioDelete(BaseModel):
    id_usuario: int