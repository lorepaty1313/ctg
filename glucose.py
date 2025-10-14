import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="AUC Glucosa (mg/dL)", layout="centered")

st.title("📈 Área Bajo la Curva (AUC) – Curva de Tolerancia a la Glucosa")
st.markdown("""
Ingresa pares de **tiempo (minutos)** y **glucosa (mg/dL)** para calcular el Área Bajo la Curva (**AUC**) con el método del trapecio.
""")

# Datos por defecto (valores en mg/dL)
default_data = pd.DataFrame({
    "Tiempo (min)": [0, 30, 60, 90, 120],
    "Glucosa (mg/dL)": [90, 140, 165, 130, 100]
})

# Entrada editable
st.subheader("✍️ Ingreso de datos")
df = st.data_editor(
    default_data,
    num_rows="dynamic",
    use_container_width=True
)

# Validación
if len(df) < 2:
    st.warning("Debes ingresar al menos dos puntos para calcular el AUC.")
else:
    # Ordenar por tiempo
    df = df.sort_values(by="Tiempo (min)")

    # Calcular AUC
    auc = np.trapz(df["Glucosa (mg/dL)"], df["Tiempo (min)"])

    # Interpretación automática basada en rangos estimados para 5 puntos
    if auc < 12000:
        interp = "⚠️ Glucosa baja. Posible hipoglucemia (consulta médica)."
        color = "orange"
    elif auc < 18000:
        interp = "✅ Respuesta normal a la glucosa."
        color = "green"
    elif auc < 22000:
        interp = "🟡 Intolerancia a la glucosa. Observar con atención."
        color = "gold"
    else:
        interp = "🔴 Posible diabetes o hiperglucemia sostenida."
        color = "red"

    # Resultado
    st.subheader("📐 Resultado")
    st.success(f"Área Bajo la Curva (AUC): **{auc:.2f} mg·min/dL**")
    st.markdown(f"**Interpretación:** <span style='color:{color}'>{interp}</span>", unsafe_allow_html=True)

    # Gráfica
    st.subheader("📈 Gráfica de la Curva de Glucosa")
    fig, ax = plt.subplots()
    ax.plot(df["Tiempo (min)"], df["Glucosa (mg/dL)"], marker='o', color="mediumvioletred")
    ax.fill_between(df["Tiempo (min)"], df["Glucosa (mg/dL)"], alpha=0.3, color="mediumvioletred")
    ax.set_xlabel("Tiempo (min)")
    ax.set_ylabel("Glucosa (mg/dL)")
    ax.set_title("Curva de Tolerancia a la Glucosa")
    st.pyplot(fig)
