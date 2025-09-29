import streamlit as st

dao = ItemDAO()
controller = ItemController(dao)

st.title("Cadastro de Itens")

with st.form("form_item"):
    descricao = st.text_input("Descrição")
    quantidade = st.number_input("Quantidade", min_value=1, step=1)
    submit = st.form_submit_button("Adicionar")

if submit:
    if descricao.strip() == "":
        st.error("Descrição não pode ser vazia")
    else:
        controller.criarItem(descricao, quantidade)
        st.success("Item adicionado com sucesso!")

st.subheader("Lista de Itens")

itens = controller.obterTodosOsItens()
for item in itens:
    st.write(f"ID: {item.id} | Descrição: {item.descricao} | Quantidade: {item.quantidade}")
