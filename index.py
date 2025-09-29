import streamlit as st
from templates.controller import ItemController

class IndexUI:
    def main():
        ItemController.main()

IndexUI.main()