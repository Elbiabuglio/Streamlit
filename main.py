import streamlit as st

import pandas as pd


def calc_general_stats(df):
    df_data = df.groupby(by="Data")["Valor"].sum().to_frame()
    df_data["lag_1"] = df_data["Valor"].shift(1)
    df_data["Diferença Mensal Absoluta"] = df_data["Valor"] - df_data["lag_1"]
    df_data["Média 6M Diferença Mensal Absoluta"] = df_data["Diferença Mensal Absoluta"].rolling(
        window=6).mean()
    df_data["Média 12M Diferença Mensal Absoluta"] = df_data["Diferença Mensal Absoluta"].rolling(
        window=12).mean()
    df_data["Média 24M Diferença Mensal Absoluta"] = df_data["Diferença Mensal Absoluta"].rolling(
        window=24).mean()

    df_data["Diferença Mensal Rel"] = df_data["Valor"] / df_data["lag_1"] - 1

    df_data["Evolução 6M Diferença Mensal"] = df_data["Diferença Mensal Absoluta"].rolling(
        window=6).apply(lambda x: x[-1] - x[0])
    df_data["Evolução 12M Diferença Mensal"] = df_data["Diferença Mensal Absoluta"].rolling(
        window=12).apply(lambda x: x[-1] - x[0])
    df_data["Evolução 24M Diferença Mensal"] = df_data["Diferença Mensal Absoluta"].rolling(
        window=24).apply(lambda x: x[-1] - x[0])

    df_data["Evolução 6M Relativa"] = df_data["Diferença Mensal Rel"].rolling(
        window=6).apply(lambda x: x[-1] / x[0])-1
    df_data["Evolução 12M Relativa"] = df_data["Diferença Mensal Rel"].rolling(
        window=12).apply(lambda x: x[-1] / x[0])-1
    df_data["Evolução 24M Relativa"] = df_data["Diferença Mensal Rel"].rolling(
        window=24).apply(lambda x: x[-1] / x[0])-1

    df_data = df_data.drop("lag_1", axis=1)
    return df_data


st.set_page_config(page_title="Finanças",
                   page_icon=":moneybag:", layout="wide")

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
    columns_fmt = {"Valor": st.column_config.NumberColumn(
        "Valor", format="R$ %.2f")}
    exp1.dataframe(df, hide_index=True, column_config=columns_fmt)

    exp2 = st.expander("📊 Análise por Instituição")
    df_instituicao = df.pivot_table(
        index="Data", columns="Instituição", values="Valor")

    tab_data, tab_history, tb_share = exp2.tabs(
        ["📊 Dados", "📜 Histórico", "📈 Participação"])

    with tab_data:
        st.dataframe(df_instituicao)

    with tab_history:
        st.line_chart(df_instituicao, use_container_width=True)

    with tb_share:
        date = st.selectbox("📅 Selecione uma data",
                            options=df_instituicao.index)
        st.bar_chart(df_instituicao.loc[date])

    exp3 = st.expander("📊 Estatísticas Gerais")

    df_stats = calc_general_stats(df)

    columns_config = {

        "Diferença Mensal Absoluta": st.column_config.NumberColumn("Diferença Mensal Absoluta", format="R$ %.2f"),
        "Média 6M Diferença Mensal Absoluta": st.column_config.NumberColumn("Média 6M Diferença Mensal Absoluta", format="R$ %.2f"),
        "Média 12M Diferença Mensal Absoluta": st.column_config.NumberColumn("Média 12M Diferença Mensal Absoluta", format="R$ %.2f"),
        "Média 24M Diferença Mensal Absoluta": st.column_config.NumberColumn("Média 24M Diferença Mensal Absoluta", format="R$ %.2f"),
        "Evolução 6M Total": st.column_config.NumberColumn("Evolução 6M Total", format="R$ %.2f"),
        "Evolução 12M Total": st.column_config.NumberColumn("Evolução 12M Total", format="R$ %.2f"),
        "Evolução 24M Total": st.column_config.NumberColumn("Evolução 24M Total", format="R$ %.2f"),
        "Diferença Mensal Rel": st.column_config.NumberColumn("Diferença Mensal Rel", format="percent"),
        "Evolução 6M Relativa": st.column_config.NumberColumn("Evolução 6M Relativa", format="percent"),
        "Evolução 12M Relativa": st.column_config.NumberColumn("Evolução 12M Relativa", format="percent"),
        "Evolução 24M Relativa": st.column_config.NumberColumn("Evolução 24M Relativa", format="percent"),

    }

    tab_stats, tab_abs, tab_rel = exp3.tabs(
        ["📊 Dados", "📈 Histórico de Evolução", "📉 Crescimento Relativo"])

    with tab_stats:
        st.dataframe(df_stats, hide_index=True, column_config=columns_config)

    with tab_abs:
        abs_cols = [
            "Diferença Mensal Absoluta",
            "Média 6M Diferença Mensal Absoluta",
            "Média 12M Diferença Mensal Absoluta",
            "Média 24M Diferença Mensal Absoluta",
        ]
        st.line_chart(df_stats[abs_cols])
    abs_cols = [
        "Diferença Mensal Absoluta",
        "Média 6M Diferença Mensal Absoluta",
        "Média 12M Diferença Mensal Absoluta",
        "Média 24M Diferença Mensal Absoluta",
    ]
    st.line_chart(df_stats[abs_cols])

    with tab_rel:
        rel_cols = [
            "Diferença Mensal Rel",
            "Evolução 6M Relativa",
            "Evolução 12M Relativa",
            "Evolução 24M Relativa",
        ]
        st.line_chart(data=df_stats[rel_cols])

    with st.expander("📊 Metas"):

        col1, col2 = st.columns(2)

        data_inicio_meta = st.date_input(
            "📅 Data de Início da Meta", max_value=df["Data"].max())

        filter_data = df_stats.index <= data_inicio_meta
        data_filtrada = df_stats[filter_data].iloc[-1]

        custos_fixos = col1.number_input(
            "Custos Fixos (R$)", min_value=0., format="%.2f")

        salario_bruto = col2.number_input(
            "Salário Bruto (R$)", min_value=0., format="%.2f")
        salario_liquido = col2.number_input(
            "Salário Líquido (R$)", min_value=0., format="%.2f")

        valor_inicio = df_stats.loc[data_inicio_meta, "Valor"]
        col1.markdown(f"**Valor no Início da Meta**: R$ {valor_inicio:.2f}")

        col1_pot, _, col2_pot = st.columns(3)
        mensal = salario_liquido - custos_fixos
        anual = mensal * 12
        
        
        with col1_pot.container(border=True):
            st.markdown("**Potencial Arrecadação**")
        col1_pot.markdown(
            f"''**Potencial Arrecadação Mês**:\n\n R$ {mensal:.2f}"'')

        with col2_pot.container(border=True):
            st.markdown(
                f"''**Potencial Arrecadação Ano**:\n\n R$ {anual:.2f}"'')
        
        with st.container(border=True):
            col1_meta, col2_meta = st.columns(2)
            with col1_meta:
                meta_estimada = st.number_input("Meta Estimada (R$)", min_value=0., format="%.2f")

            with col2_meta.container(border=True):
                patrimonio_final = meta_estimada + valor_inicio
                st.markdown(f"Patrimonio Estimado pos Meta (R$): {patrimonio_final:.2f}")
            