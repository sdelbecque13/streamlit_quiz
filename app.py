import streamlit as st

st.set_page_config(
    page_title="Quiz",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("La meilleure application de Quiz")

# Input de texte
user_input = st.text_input("Entrez votre prénom")

# Affichage du texte
st.write("Bienvenue ", user_input)

# Bouton
bouton = st.button("Cliquez ici")

if bouton:
    st.write(user_input, ", venez jouer à notre quiz de culture générale")