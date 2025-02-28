import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Gestión de Usuarios")

st.header("Crear Usuario")
nombre = st.text_input("Nombre de usuario")
clave = st.text_input("Clave de usuario", type="password")
if st.button("Crear"):
    response = requests.post(f"{API_URL}/user/create_user", json={"nombre_usuario": nombre, "clave_usuario": clave})
    st.write(response.json())

st.header("Lista de Usuarios")
if st.button("Obtener Usuarios"):
    response = requests.get(f"{API_URL}/user/get_users")
    st.write(response.json())

st.header("Actualizar Usuario")
id_usuario = st.number_input("ID del usuario", min_value=1)
nuevo_nombre = st.text_input("Nuevo Nombre")
nueva_clave = st.text_input("Nueva Clave", type="password")
if st.button("Actualizar"):
    response = requests.put(f"{API_URL}/user/update_user", json={"id_usuario": id_usuario, "nombre_usuario": nuevo_nombre, "clave_usuario": nueva_clave})
    st.write(response.json())

st.header("Eliminar Usuario")
id_eliminar = st.number_input("ID del usuario a eliminar", min_value=1)
if st.button("Eliminar"):
    response = requests.delete(f"{API_URL}/user/delete_user", json={"id_usuario": id_eliminar})
    st.write(response.json())