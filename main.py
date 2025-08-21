print('PyCharm')
import streamlit as st

# Título
st.title("Verificador de Idade")

# Campo de entrada para idade
idade = st.number_input("Digite sua idade:", min_value=0, max_value=150, step=1)

# Botão para verificar
if st.button("Verificar"):
    if idade >= 18:
        st.success("Você é maior de idade!")
    else:
        st.warning("Você é menor de idade.")



