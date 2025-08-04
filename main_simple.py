import streamlit as st
import pandas as pd
import requests
import datetime
import calendar
from datetime import date, timedelta

# Configuração da página
st.set_page_config(
    page_title="Finanças Pessoais",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Cabeçalho simples
st.title("💰 Finanças Pessoais")
st.subheader("Seu painel de controle financeiro inteligente")

# Seção de boas-vindas
st.markdown("### ✨ Bem-vindo ao seu painel de controle financeiro!")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.info("📈 **Monitorar receitas**")
with col2:
    st.info("📉 **Controlar despesas**")
with col3:
    st.info("🏦 **Gerenciar investimentos**")
with col4:
    st.info("📅 **Visualizar datas importantes**")

st.markdown("*Organize sua vida financeira de forma simples e eficiente.*")
st.markdown("---")

# Upload de arquivo
st.markdown("### 📂 Carregamento de Dados")
st.info("💡 **Como usar:** Carregue seu arquivo CSV com dados financeiros para começar a análise.")

file_upload = st.file_uploader(
    "📥 Selecione seu arquivo CSV",
    type=["csv"],
    help="Carregue um arquivo CSV com suas informações financeiras"
)

if file_upload:
    try:
        df = pd.read_csv(file_upload)

        # Tentar diferentes formatos de data
        try:
            df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y").dt.date
        except:
            try:
                df["Data"] = pd.to_datetime(
                    df["Data"], format="%Y-%m-%d").dt.date
            except:
                try:
                    df["Data"] = pd.to_datetime(
                        df["Data"], infer_datetime_format=True).dt.date
                except Exception as e:
                    st.error(f"Erro ao converter datas: {e}")
                    st.stop()

        # Mostrar dados básicos
        st.success("✅ Arquivo carregado com sucesso!")
        st.dataframe(df.head())

        # Informações básicas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📝 Total de Registros", len(df))
        with col2:
            st.metric("📅 Períodos", len(df['Data'].unique()))
        with col3:
            st.metric("🏦 Instituições", len(df['Instituição'].unique()))

    except Exception as e:
        st.error(f"Erro ao processar arquivo: {e}")

# Rodapé
st.markdown("---")
st.info("📱 **Dica:** Use esta aplicação para controlar suas finanças de forma eficiente!")
