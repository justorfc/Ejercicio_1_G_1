import streamlit as st
import pandas as pd

st.title('Ejemplo básico de Streamlit')

st.write('¡Hola, mundo!')

# Ejemplo de DataFrame

data = {
    'Columna 1': [1, 2, 3, 4],
    'Columna 2': ['A', 'B', 'C', 'D']
}
df = pd.DataFrame(data)

st.write('Este es un DataFrame de ejemplo:')
st.dataframe(df)
