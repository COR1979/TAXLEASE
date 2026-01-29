import streamlit as st

st.set_page_config(page_title="DERTOGEST - Optimización Fiscal", page_icon="📊")

st.title("📊 DERTOGEST, S.L.")
st.header("Calculadora de Optimización (Art. 39.7 LIS)")

perfil = st.radio("Perfil del Inversor:", ["Profesional/Empresario (IRPF)", "Sociedad (IS)"])
cuota = st.number_input("Cuota Íntegra estimada (€):", min_value=0, value=10000, step=1000)

# Lógica según tus informes estratégicos
# El Art. 39.1 LIS permite elevar el límite al 50% si la inversión es relevante [cite: 13, 14, 39, 81]
deduccion_max = cuota * 0.50 
inversion_optima = deduccion_max / 1.20 
ahorro_neto = deduccion_max - inversion_optima

st.divider()
c1, c2 = st.columns(2)
with c1:
    st.metric("Inversión Óptima", f"{inversion_optima:,.2f} €")
    st.caption("Aportación antes del 31 de diciembre.")
with c2:
    st.metric("Beneficio Neto (20%)", f"{ahorro_neto:,.2f} €")
    st.caption("Ganancia neta garantizada[cite: 12, 29, 74].")

st.success(f"Usted deja de pagar {deduccion_max:,.2f} € a Hacienda. Su cuota final se reduce a {cuota - deduccion_max:,.2f} €.")
st.info("Operación blindada con Informe Motivado y Seguro de Contingencia.")
