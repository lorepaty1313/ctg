import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="AUC Glucosa", layout="centered")

st.title("📈 Área Bajo la Curva (AUC) – Curva de Tolerancia a la Glucosa")
st.markdown("Ingresa pares de tiempo y glucosa para calcular el área bajo la curva (AUC). Puedes agregar o eliminar filas.")

# Valores iniciales
default_data = pd.DataFrame({
    "Tiempo (min)": [0, 30, 60, 90, 120],
    "Glucosa (mmol/L)": [5.2, 7.8, 8.5, 7.2, 5.9]
})

# Edición de datos en tabla
st.subheader("✍️ Ingreso de datos")
df = st.data_editor(
    default_data,
    num_rows="dynamic",
    use_container_width=True
)

# Verificación
if len(df) < 2:
    st.warning("Debes ingresar al menos dos puntos para calcular el AUC.")
else:
    # Ordenar por tiempo por si acaso
    df = df.sort_values(by="Tiempo (min)")

    # Calcular AUC
    auc = np.trapz(df["Glucosa (mmol/L)"], df["Tiempo (min)"])

    # Mostrar resultados
    st.subheader("📐 Resultado")
    st.success(f"Área Bajo la Curva (AUC): **{auc:.2f} mmol·min/L**")

    # Gráfica
    st.subheader("📈 Gráfica de la Curva")
    fig, ax = plt.subplots()
    ax.plot(df["Tiempo (min)"], df["Glucosa (mmol/L)"], marker='o', color="mediumvioletred")
    ax.fill_between(df["Tiempo (min)"], df["Glucosa (mmol/L)"], alpha=0.3, color="mediumvioletred")
    ax.set_xlabel("Tiempo (min)")
    ax.set_ylabel("Glucosa (mmol/L)")
    ax.set_title("Curva de Tolerancia a la Glucosa")
    st.pyplot(fig)
