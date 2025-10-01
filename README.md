# Ejemplo básico de Streamlit

## Definiciones

**Streamlit:** Framework de Python para crear aplicaciones web interactivas de manera sencilla y rápida, especialmente orientado a ciencia de datos y machine learning.

**pandas:** Biblioteca de Python para manipulación y análisis de datos, que proporciona estructuras de datos flexibles y eficientes.

---

Este proyecto contiene una aplicación sencilla desarrollada con Streamlit y pandas.

## Requisitos

- Python 3.12+
- Streamlit
- pandas

Puedes instalar las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

## Ejecución

Para iniciar la aplicación, activa el entorno virtual y ejecuta:

```bash
streamlit run app.py
```

## Descripción de la app

La aplicación muestra un título, un mensaje de bienvenida y un DataFrame de ejemplo usando pandas.

```python
import streamlit as st
import pandas as pd

st.title('Ejemplo básico de Streamlit')
st.write('¡Hola, mundo!')

data = {
    'Columna 1': [1, 2, 3, 4],
    'Columna 2': ['A', 'B', 'C', 'D']
}
df = pd.DataFrame(data)
st.write('Este es un DataFrame de ejemplo:')
st.dataframe(df)
```

## Autor

justorfc
