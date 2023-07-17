import streamlit as st

import controller.cliente as cliente
import services.database as db


def Excluir():
    st.title('Deletar dados')

    with st.form(key='delete'):
        nome = st.text_input(label='Inserir o nome:')
        buttom_submit = st.form_submit_button('Deletar')

    if buttom_submit:
        cliente.excluir(nome)
        st.success('Aluno excluido com sucesso')
    