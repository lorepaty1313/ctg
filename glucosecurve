import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="AUC Glucosa", layout="centered")

st.title("📈 Área Bajo la Curva (AUC) – Curva de Tolerancia a la Glucosa")

st.markdown("Ingresa los niveles de glucosa (mmol/L) en los diferentes tiempos medidos.")

# Tiempos comunes para la prueba
tiempos = [0, 30, 60, 90, 120]
glucosa = []

st.header("1. Ingresa tus datos")

# Inputs
for t in tiempos:
    val = st.number_input(
        f"Glucosa a los {t} minutos (mmol/L)",
        min_value=0.0,
        step=0.1,
        format="%.1f",
        key=f"glucosa_{t}"
    )
    glucosa.append(val)

# Crear dataframe
df = pd.DataFrame({
    "Tiempo (min)": tiempos,
    "Glucosa (mmol/L)": glucosa
})

# Mostrar tabla
st.subheader("📊 Datos ingresados")
st.dataframe(df)

# Calcular AUC
auc = np.trapz(df["Glucosa (mmol/L)"], df["Tiempo (min)"])

# Mostrar resultado
st.subheader("📐 Resultado")
st.success(f"Área Bajo la Curva (AUC): **{auc:.2f} mmol·min/L**")

# Gráfica
st.subheader("📈 Gráfica de la Curva de Glucosa")
fig, ax = plt.subplots()
ax.plot(df["Tiempo (min)"], df["Glucosa (mmol/L)"], marker='o', color="mediumvioletred")
ax.fill_between(df["Tiempo (min)"], df["Glucosa (mmol/L)"], alpha=0.3, color="mediumvioletred")
ax.set_xlabel("Tiempo (min)")
ax.set_ylabel("Glucosa (mmol/L)")
ax.set_title("Curva de Tolerancia a la Glucosa")
st.pyplot(fig)
