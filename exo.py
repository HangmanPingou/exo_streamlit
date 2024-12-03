import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()


def menu():
    with st.sidebar:
    # Création du menu qui va afficher les choix qui se trouvent dans la variable options
        st.write(f"Bonjour {st.session_state['username']} !\n  Bienvenue 👋")
        selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"],
            default_index= 0)
        authenticator.logout("Déconnexion")
    return selection

def album():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Sauteur")
        st.image("https://c0.lestechnophiles.com/www.madmoizelle.com/wp-content/uploads/2014/03/pourquoi-pingouins-etres-fascinants.jpg?webp=1&resize=640,361&key=c6b166cc")
    with col2:
        st.header("Crieur")
        st.image("https://b3200456.smushcdn.com/3200456/wp-content/uploads/2019/01/PB-Pingouin-detail-900x900px-100x100.jpg?lossy=0&strip=1&webp=1")
    with col3:
        st.header("Nageur")
        st.image("https://www.francebleu.fr/s3/cruiser-production/2022/11/1e7d9bd4-fd86-471c-ad58-675f4f7d78b8/1200x680_unnamed_1_0.webp")


if st.session_state["authentication_status"]:
    selection = menu()
    if selection == "Accueil":
        st.title("Bienvenue sur la page d'accueil !")
    elif selection == "Photos":
        st.title("Bienvenue sur mon album photo")
        album()


elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')