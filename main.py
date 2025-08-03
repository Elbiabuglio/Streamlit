import streamlit as st
import pandas as pd
import requests
import datetime
import calendar
from datetime import date, timedelta


@st.cache_data(ttl="1day")
def get_selic():
    url = "https://www.bcb.gov.br/api/servico/sitebcb/historicotaxasjuros"
    response = requests.get(url)
    if response.status_code == 200:
        df = pd.DataFrame(response.json()["conteudo"])
        df["DataInicioVigencia"] = pd.to_datetime(
            df["DataInicioVigencia"]).dt.date
        df["DataFimVigencia"] = pd.to_datetime(df["DataFimVigencia"]).dt.date
        df["DataFimVigencia"] = df["DataFimVigencia"].fillna(
            datetime.date.today())
        return df


def create_calendar_widget():
    """Cria um widget de calendário mais intuitivo"""

    # CSS personalizado para o calendário
    st.markdown("""
    <style>
    .calendar-container {
        background: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 10px 0;
        max-width: 600px;
        margin: 0 auto;
    }
    .calendar-header {
        text-align: center;
        margin-bottom: 20px;
        font-weight: bold;
        font-size: 18px;
        color: #1976d2;
    }
    .weekday-header {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 2px;
        margin-bottom: 10px;
        background: #1976d2;
        border-radius: 8px;
        padding: 12px 8px;
    }
    .weekday-name {
        text-align: center;
        font-weight: bold;
        color: white;
        font-size: 14px;
        padding: 5px;
    }
    .calendar-grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 2px;
        border: 1px solid #e1e5e9;
        border-radius: 8px;
        padding: 8px;
        background: #f8f9fa;
    }
    .calendar-day {
        aspect-ratio: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid #e1e5e9;
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.2s;
        background: white;
        font-weight: 500;
        min-height: 40px;
    }
    .calendar-day:hover {
        background: #e3f2fd;
        border-color: #1976d2;
        transform: scale(1.05);
    }
    .calendar-day.selected {
        background: #1976d2;
        color: white;
        border-color: #1976d2;
    }
    .calendar-day.today {
        background: #ff9800;
        color: white;
        border-color: #f57c00;
        font-weight: bold;
    }
    .calendar-day.other-month {
        color: #bbb;
        background: #f5f5f5;
    }
    </style>
    """, unsafe_allow_html=True)

    # Interface do calendário
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        # Seleção de mês e ano
        col_mes, col_ano = st.columns(2)

        meses = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]

        with col_mes:
            mes_selecionado = st.selectbox(
                "Mês",
                options=list(range(1, 13)),
                format_func=lambda x: meses[x-1],
                index=datetime.date.today().month - 1,  # Mês atual como padrão
                key="mes_calendario"
            )

        with col_ano:
            ano_selecionado = st.selectbox(
                "Ano",
                options=list(range(2020, 2030)),
                index=list(range(2020, 2030)).index(
                    datetime.date.today().year),  # Ano atual como padrão
                key="ano_calendario"
            )

    # Criar o calendário HTML
    cal = calendar.monthcalendar(ano_selecionado, mes_selecionado)
    hoje = datetime.date.today()

    # Nomes dos dias da semana
    dias_semana = ["Domingo", "Segunda", "Terça",
                   "Quarta", "Quinta", "Sexta", "Sábado"]
    dias_semana_abrev = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]

    calendar_html = f"""
    <div class="calendar-container">
        <div class="calendar-header">
            📅 {meses[mes_selecionado-1]} {ano_selecionado}
        </div>
        <div class="weekday-header">
    """

    # Adicionar cabeçalhos dos dias da semana
    for dia_abrev in dias_semana_abrev:
        calendar_html += f'<div class="weekday-name">{dia_abrev}</div>'

    calendar_html += """
        </div>
        <div class="calendar-grid">
    """

    # Adicionar os dias do calendário
    for semana in cal:
        for dia in semana:
            if dia == 0:
                calendar_html += '<div class="calendar-day other-month"></div>'
            else:
                data_atual = date(ano_selecionado, mes_selecionado, dia)
                classes = "calendar-day"

                if data_atual == hoje:
                    classes += " today"

                calendar_html += f'<div class="{classes}">{dia}</div>'

    calendar_html += """
        </div>
    </div>
    """

    st.markdown(calendar_html, unsafe_allow_html=True)

    # Retornar a data selecionada (para integração com o resto do código)
    return date(ano_selecionado, mes_selecionado, 1)


def calc_general_stats(df):
    # Ordenar por data antes de fazer os cálculos
    df_sorted = df.sort_values('Data')
    df_data = df_sorted.groupby(by="Data")["Valor"].sum().to_frame()
    df_data = df_data.sort_index()  # Garantir ordem cronológica

    df_data["lag_1"] = df_data["Valor"].shift(1)
    df_data["Diferença Mensal Absoluta"] = df_data["Valor"] - df_data["lag_1"]
    df_data["Média 6M Diferença Mensal Absoluta"] = df_data["Diferença Mensal Absoluta"].rolling(
        window=6, min_periods=1).mean()
    df_data["Média 12M Diferença Mensal Absoluta"] = df_data["Diferença Mensal Absoluta"].rolling(
        window=12, min_periods=1).mean()
    df_data["Média 24M Diferença Mensal Absoluta"] = df_data["Diferença Mensal Absoluta"].rolling(
        window=24, min_periods=1).mean()

    df_data["Diferença Mensal Rel"] = df_data["Valor"] / df_data["lag_1"] - 1

    df_data["Evolução 6M Diferença Mensal"] = df_data["Diferença Mensal Absoluta"].rolling(
        window=6, min_periods=1).apply(lambda x: x.iloc[-1] - x.iloc[0] if len(x) > 1 else 0)
    df_data["Evolução 12M Diferença Mensal"] = df_data["Diferença Mensal Absoluta"].rolling(
        window=12, min_periods=1).apply(lambda x: x.iloc[-1] - x.iloc[0] if len(x) > 1 else 0)
    df_data["Evolução 24M Diferença Mensal"] = df_data["Diferença Mensal Absoluta"].rolling(
        window=24, min_periods=1).apply(lambda x: x.iloc[-1] - x.iloc[0] if len(x) > 1 else 0)

    df_data["Evolução 6M Relativa"] = df_data["Diferença Mensal Rel"].rolling(
        window=6, min_periods=1).apply(lambda x: x.iloc[-1] / x.iloc[0] - 1 if len(x) > 1 and x.iloc[0] != 0 else 0)
    df_data["Evolução 12M Relativa"] = df_data["Diferença Mensal Rel"].rolling(
        window=12, min_periods=1).apply(lambda x: x.iloc[-1] / x.iloc[0] - 1 if len(x) > 1 and x.iloc[0] != 0 else 0)
    df_data["Evolução 24M Relativa"] = df_data["Diferença Mensal Rel"].rolling(
        window=24, min_periods=1).apply(lambda x: x.iloc[-1] / x.iloc[0] - 1 if len(x) > 1 and x.iloc[0] != 0 else 0)

    df_data = df_data.drop("lag_1", axis=1)
    return df_data


def main_metas(df_stats):
    """Função principal para configuração e cálculo de metas financeiras"""
    # Seção de configuração de metas com melhor organização
    st.markdown("### 🎯 Configuração de Metas Financeiras")

    # Container para os campos de entrada
    with st.container(border=True):
        st.markdown("#### 💰 Metas")
        col1, col2 = st.columns(2)

        with col1:
            custos_fixos = st.number_input(
                "Custos Fixos (R$)", min_value=0., format="%.2f", key="custos_fixos")

        with col2:
            salario_bruto = st.number_input(
                "Salário Bruto (R$)", min_value=0., format="%.2f", key="salario_bruto")

        salario_liquido = st.number_input(
            "Salário Líquido (R$)", min_value=0., format="%.2f", key="salario_liquido")

    # Container para dados de início da meta
    with st.container(border=True):
        st.markdown("#### 📅 Dados de Início da Meta")

        # Usar date_input com tratamento inteligente de datas
        datas_disponiveis = sorted(df_stats.index)

        data_inicio_meta = st.date_input(
            "Data de Início da Meta",
            value=datas_disponiveis[0],  # Primeira data disponível como padrão
            min_value=datas_disponiveis[0],  # Primeira data como mínima
            max_value=datas_disponiveis[-1],  # Última data como máxima
            help="Selecione uma data para definir o início da sua meta financeira"
        )

        # Encontrar a data mais próxima disponível
        if data_inicio_meta in datas_disponiveis:
            valor_inicio = df_stats.loc[data_inicio_meta, "Valor"]
        else:
            # Encontrar a data mais próxima (anterior ou igual)
            datas_anteriores = [
                d for d in datas_disponiveis if d <= data_inicio_meta]
            if datas_anteriores:
                data_proxima = max(datas_anteriores)
            else:
                data_proxima = min(datas_disponiveis)

            valor_inicio = df_stats.loc[data_proxima, "Valor"]
            st.info(
                f"📅 Usando dados de {data_proxima.strftime('%d/%m/%Y')} (data mais próxima disponível)")

        st.markdown(
            f"**Patrimônio no Início da Meta:** R$ {valor_inicio:,.2f}")

    # Container para configuração da SELIC
    with st.container(border=True):
        # Tratamento de erro para API da SELIC
        try:
            selic_gov = get_selic()
            filter_selic_date = (selic_gov["DataInicioVigencia"] <= data_inicio_meta) & (
                selic_gov["DataFimVigencia"] >= data_inicio_meta)
            selic_filtered = selic_gov.loc[filter_selic_date]

            if not selic_filtered.empty:
                selic_default = selic_filtered["MetaSelic"].iloc[0]
            else:
                selic_default = 10.75  # Valor padrão se não encontrar
        except:
            selic_default = 10.75  # Valor padrão em caso de erro

        selic = st.number_input("Selic (%)", min_value=0.,
                                value=selic_default, format="%.2f")
        selic_ano = selic / 100
        selic_mes = (selic_ano + 1) ** (1/12) - 1

    # Cálculos de rendimento
    rendimento_ano = valor_inicio * selic_ano
    rendimento_mes = valor_inicio * selic_mes
    mensal = salario_liquido - custos_fixos + valor_inicio * selic_mes
    anual = 12 * (salario_liquido - custos_fixos) + rendimento_ano

    # Container para potenciais de arrecadação
    st.markdown("#### 📈 Potencial de Arrecadação")
    col1_pot, col2_pot = st.columns(2)

    with col1_pot:
        with st.container(border=True):
            st.markdown("**Potencial Arrecadação Mensal**")
            st.markdown(f"R$ {mensal:.2f}")

    with col2_pot:
        with st.container(border=True):
            st.markdown("**Potencial Arrecadação Anual**")
            st.markdown(f"R$ {anual:.2f}")

    # Container para configuração de metas
    with st.container(border=True):
        st.markdown("#### 🎯 Configuração de Metas")
        col1_meta, col2_meta = st.columns(2)

        with col1_meta:
            meta_estimada = st.number_input(
                "Meta Estimada (R$)", min_value=0., format="%.2f", key="meta_estimada")

        with col2_meta:
            patrimonio_final = st.number_input(
                "Patrimônio Estimado pós Meta (R$)",
                min_value=0.,
                value=meta_estimada + valor_inicio if meta_estimada > 0 else valor_inicio,
                format="%.2f",
                help="Patrimônio total esperado após atingir a meta",
                key="patrimonio_final"
            )

    # Cálculo da tabela de metas
    meses = pd.DataFrame({
        "Data Referencia": [
            data_inicio_meta + pd.DateOffset(months=i) for i in range(1, 13)],
        "Meta Mensal": [valor_inicio + round(meta_estimada/12, 2) * i for i in range(1, 13)]})
    meses["Data Referencia"] = meses["Data Referencia"].dt.strftime(
        "%Y-%m")

    df_patrimonio = df_stats.reset_index()[["Valor"]].copy()
    df_patrimonio["Data Referencia"] = pd.to_datetime(
        df_stats.index).strftime("%Y-%m")
    meses = meses.merge(df_patrimonio, how="left", on="Data Referencia")

    # Calcular Atingimento Esperado após o merge
    meses["Atingimento Esperado"] = meses["Meta Mensal"] / meta_estimada

    meses = meses[["Data Referencia", "Meta Mensal",
                   "Atingimento Esperado", "Valor"]]
    meses["Atingimento (%)"] = (
        meses["Valor"] / meses["Meta Mensal"] * 100).round(1)

    meses["Atingimento Ano"] = (
        meses["Valor"] / patrimonio_final * 100).round(1)

    # Definir Data Referencia como índice
    meses.set_index("Data Referencia", inplace=True)

    # Container para a tabela de resultados
    st.markdown("#### 📊 Acompanhamento de Metas")
    with st.container(border=True):
        # Configurar formatação das colunas
        meses_config = {
            "Meta Mensal": st.column_config.NumberColumn("Meta Mensal", format="R$ %.2f"),
            "Atingimento Esperado": st.column_config.NumberColumn("Atingimento Esperado", format="%.3f"),
            "Valor": st.column_config.NumberColumn("Valor", format="R$ %.2f"),
            "Atingimento (%)": st.column_config.NumberColumn("Atingimento (%)", format="%.1f%%"),
            "Atingimento Ano": st.column_config.NumberColumn("Atingimento Ano", format="%.1f%%")
        }

        st.dataframe(meses, column_config=meses_config,
                     use_container_width=True)

    # Retornar os valores solicitados incluindo o DataFrame meses
    return data_inicio_meta, valor_inicio, meta_estimada, patrimonio_final, meses


# Configuração da página
st.set_page_config(page_title="Finanças",
                   page_icon=":moneybag:", layout="wide")

st.markdown("""
# 💰 Finanças Pessoais

Bem-vindo ao seu painel de controle financeiro!  
Aqui você pode:

- 📈 Monitorar receitas
- 📉 Controlar despesas
- 🏦 Gerenciar investimentos
- 📅 Visualizar datas importantes

Organize sua vida financeira de forma simples e eficiente.
""")

# Widget de calendário melhorado
with st.expander("📅 Calendário Financeiro", expanded=False):
    st.markdown("### Visualize datas importantes para suas finanças")
    data_calendario = create_calendar_widget()

    # Informações adicionais sobre a data selecionada
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"📅 **Mês selecionado:** {data_calendario.strftime('%B/%Y')}")
    with col2:
        dias_no_mes = calendar.monthrange(
            data_calendario.year, data_calendario.month)[1]
        st.info(f"📊 **Dias no mês:** {dias_no_mes}")
    with col3:
        dias_uteis = len([d for d in range(1, dias_no_mes + 1)
                         if date(data_calendario.year, data_calendario.month, d).weekday() < 5])
        st.info(f"💼 **Dias úteis:** {dias_uteis}")

# Upload de arquivo
file_upload = st.file_uploader("📥 Carregar arquivo CSV", type=["csv"])
if file_upload:

    df = pd.read_csv(file_upload)

    # Tentar diferentes formatos de data
    try:
        df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y").dt.date
    except:
        try:
            df["Data"] = pd.to_datetime(df["Data"], format="%Y-%m-%d").dt.date
        except:
            try:
                df["Data"] = pd.to_datetime(
                    df["Data"], infer_datetime_format=True).dt.date
            except Exception as e:
                st.error(f"Erro ao converter datas: {e}")
                st.stop()

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
                            options=sorted(df_instituicao.index))
        st.bar_chart(df_instituicao.loc[date])

    exp3 = st.expander("📊 Estatísticas Gerais")

    df_stats = calc_general_stats(df)

    columns_config = {
        "Valor": st.column_config.NumberColumn("Valor", format="R$ %.2f"),
        "Diferença Mensal Absoluta": st.column_config.NumberColumn("Diferença Mensal Absoluta", format="R$ %.2f"),
        "Média 6M Diferença Mensal Absoluta": st.column_config.NumberColumn("Média 6M Diferença Mensal Absoluta", format="R$ %.2f"),
        "Média 12M Diferença Mensal Absoluta": st.column_config.NumberColumn("Média 12M Diferença Mensal Absoluta", format="R$ %.2f"),
        "Média 24M Diferença Mensal Absoluta": st.column_config.NumberColumn("Média 24M Diferença Mensal Absoluta", format="R$ %.2f"),
        "Evolução 6M Diferença Mensal": st.column_config.NumberColumn("Evolução 6M Diferença Mensal", format="R$ %.2f"),
        "Evolução 12M Diferença Mensal": st.column_config.NumberColumn("Evolução 12M Diferença Mensal", format="R$ %.2f"),
        "Evolução 24M Diferença Mensal": st.column_config.NumberColumn("Evolução 24M Diferença Mensal", format="R$ %.2f"),
        "Diferença Mensal Rel": st.column_config.NumberColumn("Diferença Mensal Rel", format="%.2%"),
        "Evolução 6M Relativa": st.column_config.NumberColumn("Evolução 6M Relativa", format="%.2%"),
        "Evolução 12M Relativa": st.column_config.NumberColumn("Evolução 12M Relativa", format="%.2%"),
        "Evolução 24M Relativa": st.column_config.NumberColumn("Evolução 24M Relativa", format="%.2%"),
    }

    tab_stats, tab_abs, tab_rel = exp3.tabs(
        ["📊 Dados", "📈 Histórico de Evolução", "📉 Crescimento Relativo"])

    with tab_stats:
        st.dataframe(df_stats, column_config=columns_config)

    with tab_abs:
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
        # Estrutura de tabs para organizar a seção de metas
        tab_main, tab_data_meta, tab_graph = st.tabs(
            ["📋 Configuração", "📊 Dados", "📈 Gráficos"])

        with tab_main:
            # Chamada da função de metas que retorna os valores solicitados
            data_inicio_meta, valor_inicio, meta_estimada, patrimonio_final, meses = main_metas(
                df_stats)

        with tab_data_meta:
            st.markdown("### 📊 Dados das Metas")
            # Aqui você pode adicionar análises dos dados das metas
            if 'data_inicio_meta' in locals():
                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric("Data Início",
                              data_inicio_meta.strftime("%d/%m/%Y"))

                with col2:
                    st.metric("Valor Inicial", f"R$ {valor_inicio:,.2f}")

                with col3:
                    st.metric("Meta Estimada", f"R$ {meta_estimada:,.2f}")

                with col4:
                    st.metric("Patrimônio Final",
                              f"R$ {patrimonio_final:,.2f}")

        with tab_graph:
            st.markdown("### 📈 Gráficos das Metas")
            # Aqui você pode adicionar gráficos relacionados às metas
            if 'data_inicio_meta' in locals():
                st.line_chart(meses["Atingimento Ano"])

        # Informações do dataset
    with st.expander("ℹ️ Informações do Dataset"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total de Registros", len(df))
        with col2:
            st.metric("Períodos", len(df['Data'].unique()))
        with col3:
            st.metric("Instituições", len(df['Instituição'].unique()))

        st.write(
            f"**Período analisado**: {min(df['Data']).strftime('%d/%m/%Y')} até {max(df['Data']).strftime('%d/%m/%Y')}")
        st.write(
            f"**Instituições**: {', '.join(df['Instituição'].unique().tolist())}")

# Rodapé com informações adicionais
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    📱 <strong>Dica:</strong> Use o calendário para visualizar informações específicas de cada mês!<br>
    💡 Para melhores resultados, mantenha seus dados financeiros sempre atualizados.
</div>
""", unsafe_allow_html=True)
