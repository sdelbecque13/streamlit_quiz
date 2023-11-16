# Création d'un quiz

import streamlit as st

st.title("Quiz de culture générale")

# Création d'un formulaire

with st.form("my_form"):

    reponse1 = st.text_input("Combien de fois la france a-t-elle remporté la Coupe du Monde de football ?")

    bouton = st.form_submit_button("Valider")

    if bouton:
        if reponse1.lower() == '2':
            st.write("Bonne réponse")
        else:
            st.write("Mauvaise réponse")