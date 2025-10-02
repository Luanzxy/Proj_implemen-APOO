import streamlit as st
from view.item_view import ItemView

def main():
    view = ItemView()
    view.render()

if __name__ == "__main__":
    main()