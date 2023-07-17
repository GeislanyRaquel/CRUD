import streamlit as st

import page.insert as insert
import page.select as select
import page.delete as delete
import controller.cliente as cliente

#criando a barra lateral do menu
st.sidebar.title('Menu')
selectbox = st.sidebar.selectbox('Ação', ['Inserir', 'Consultar', 'Excluir'])

if selectbox == 'Inserir':
    insert.inserir()

if selectbox == 'Consultar':
    select.consultar()

if selectbox == 'Excluir':
    delete.Excluir()


