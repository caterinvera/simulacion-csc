import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Simulación Clínica", layout="wide")

st.title("🏥 Centro de Simulación Clínica")
st.subheader("Sistema de Reservas")

if 'reservas' not in st.session_state:
    st.session_state.reservas = []

with st.form("form_reserva"):
    docente = st.text_input("Nombre del Docente")
    asignatura = st.text_input("Asignatura")
    zona = st.selectbox("Zona de Simulación", ["0", "1", "2A", "2B", "2.5", "3"])
    fecha = st.date_input("Fecha", min_value=datetime.now())
    enviar = st.form_submit_button("Registrar Reserva")
    
    if enviar:
        st.session_state.reservas.append({"Docente": docente, "Zona": zona, "Fecha": fecha})
        st.success("¡Reserva registrada!")

if st.session_state.reservas:
    st.write("### Reservas Actuales")
    st.table(pd.DataFrame(st.session_state.reservas))
