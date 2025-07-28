import streamlit as st  

import pandas as pd

st.set_page_config(page_title="Finanças", page_icon=":moneybag:", layout="wide")

st.markdown("""
# 💰 Finanças Pessoais

Bem-vindo ao seu painel de controle financeiro!  
Aqui você pode:

- 📈 Monitorar receitas
- 📉 Controlar despesas
- 🏦 Gerenciar investimentos

Organize sua vida financeira de forma simples e eficiente.
""")

file_upload = st.file_uploader("📥 Carregar arquivo CSV", type=["csv"])
if file_upload:
    
    df = pd.read_csv(file_upload)
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y").dt.date
    
    exp1 = st.expander("📊 Visualizar Dados")
    df["Valor"] = df["Valor"].astype(float)
    columns_fmt = {"Valor": st.column_config.NumberColumn ("Valor", format="R$ %f")}
    exp1.dataframe(df, hide_index=True, column_config=columns_fmt)

    exp2 =st.expander("📊 Análise por Instituição")
    df_instituicao = df.pivot_table(index="Data", columns="Instituição", values="Valor")
    
    tab_data,tab_history, tb_share = exp2.tabs(["📊 Dados", "📜 Histórico", "📈 Participação"])
    
    with tab_data:
        st.dataframe(df_instituicao)

    with tab_history:
        st.line_chart(df_instituicao, use_container_width=True)

    with tb_share:
        date = st.selectbox("📅 Selecione uma data", options=df_instituicao.index)
        st.bar_chart(df_instituicao.loc[date])