import streamlit as st
import pandas as pd
from controller.item_controller import ItemController

class ItemView:
    def __init__(self):
        self.controller = ItemController()

    def render(self):
        st.title("Cadastro de Itens")

        # --- Adicionar Item ---
        st.subheader("Adicionar novo item")
        with st.form("form_item"):
            descricao = st.text_input("Descrição")
            quantidade = st.number_input("Quantidade", min_value=1, step=1)
            submit = st.form_submit_button("Cadastrar")

            if submit:
                if descricao.strip():
                    self.controller.criarItem(descricao, quantidade)
                    st.success(f"Item '{descricao}' cadastrado com sucesso!")
                else:
                    st.warning("⚠️ A descrição não pode estar vazia.")

        # --- Listar Itens ---
        st.subheader("📋 Itens cadastrados")
        itens = self.controller.obterTodosOsItens()

        if itens:
            data = [{"ID": item.id, "Descrição": item.descricao, "Quantidade": item.quantidade} for item in itens]
            df = pd.DataFrame(data)
            st.dataframe(df.set_index("ID"))  # tira os números extras da esquerda
            st.info(f"Total de itens cadastrados: {len(itens)}")
        else:
            st.info("Nenhum item cadastrado ainda.")

        # --- Remover Item ---
        st.subheader("Remover item")
        id_remover = st.number_input("Digite o ID do item para remover", min_value=1, step=1)
        if st.button("Remover"):
            if self.controller.removerItem(id_remover):
                st.success(f"Item com ID {id_remover} removido com sucesso!")
            else:
                st.error(f"Nenhum item com ID {id_remover} encontrado.")