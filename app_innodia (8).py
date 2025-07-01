import streamlit as st
import pandas as pd

# 🎨 Paleta de Cores Profissional
AZUL_PRIMARIO = "#2643E8"
AZUL_ESCURO = "#0A1033"
DOURADO = "#D4AF37"
BRANCO = "#FFFFFF"
CINZA_CLARO = "#F5F7FA"

# Configuração da página
st.set_page_config(page_title="Innódia - Sistema Empresarial", layout="wide")

# Estilo personalizado com alto contraste e visual limpo
st.markdown(f"""
    <style>
        body, .stApp {{
            background-color: {CINZA_CLARO};
            color: {AZUL_ESCURO};
            font-family: 'Segoe UI', sans-serif;
        }}
        .stButton>button {{
            background-color: {AZUL_PRIMARIO};
            color: white;
            border-radius: 6px;
            padding: 8px 18px;
            font-weight: 600;
            font-size: 15px;
            border: none;
        }}
        .stButton>button:hover {{
            background-color: {DOURADO};
            color: {AZUL_ESCURO};
        }}
        h1, h2, h3 {{
            color: {AZUL_ESCURO};
            font-weight: 700;
        }}
        .card {{
            background-color: {BRANCO};
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            text-align: center;
        }}
    </style>
""", unsafe_allow_html=True)

# Menu lateral
menu = st.sidebar.radio("Navegação", ["Início", "Clientes"])
st.sidebar.markdown("---")
st.sidebar.markdown("Sistema Innódia © 2025")

# Início
if menu == "Início":
    st.title("Painel Administrativo - Innódia")
    st.markdown("Sistema de gestão empresarial com automação, clareza e eficiência.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='card'><h3>Clientes</h3><p style='font-size:24px;color:{AZUL_PRIMARIO};'>12</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='card'><h3>Estoque</h3><p style='font-size:24px;color:{AZUL_PRIMARIO};'>37</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='card'><h3>Faturamento</h3><p style='font-size:24px;color:{AZUL_PRIMARIO};'>R$ 4.820</p></div>", unsafe_allow_html=True)

# Clientes
elif menu == "Clientes":
    st.title("Cadastro de Clientes")

    if "clientes" not in st.session_state:
        st.session_state.clientes = []

    with st.form("form_cliente"):
        st.subheader("Adicionar Novo Cliente")
        col1, col2, col3 = st.columns(3)
        with col1:
            nome = st.text_input("Nome completo")
        with col2:
            email = st.text_input("E-mail")
        with col3:
            telefone = st.text_input("Telefone")
        enviar = st.form_submit_button("Cadastrar Cliente")

        if enviar:
            if nome and email and telefone:
                st.session_state.clientes.append({
                    "Nome": nome,
                    "E-mail": email,
                    "Telefone": telefone
                })
                st.success(f"Cliente {nome} cadastrado com sucesso.")
            else:
                st.warning("Preencha todos os campos obrigatórios.")

    st.markdown("---")
    st.subheader("Clientes Cadastrados")

    if st.session_state.clientes:
        df = pd.DataFrame(st.session_state.clientes)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Nenhum cliente cadastrado ainda.")