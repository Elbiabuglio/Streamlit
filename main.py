import streamlit as st
import pandas as pd
import requests
import datetime
import calendar
from datetime import date, timedelta

# Imports com tratamento de erro para Streamlit Cloud
try:
    import plotly.express as px
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError:
    st.error("⚠️ Plotly não disponível. Instale com: pip install plotly")
    PLOTLY_AVAILABLE = False

# Imports CSS/HTML temporariamente removidos para debug
# from styles.calendar_css import get_calendar_css
# from styles.main_css import get_main_css, get_custom_header


def render_html_table(df, container=None):
    """
    Renderiza uma tabela HTML sem dependência do PyArrow
    """
    html_table = "<div style='overflow-x: auto;'><table style='width: 100%; border-collapse: collapse; font-family: Arial, sans-serif;'>"
    html_table += "<thead><tr style='background-color: #f0f2f6; border-bottom: 2px solid #ddd;'>"

    # Cabeçalhos
    for col in df.columns:
        html_table += f"<th style='padding: 12px; text-align: left; font-weight: bold;'>{col}</th>"
    html_table += "</tr></thead><tbody>"

    # Dados
    for idx, row in df.iterrows():
        html_table += "<tr style='border-bottom: 1px solid #eee;'>"
        for col in df.columns:
            value = row[col] if pd.notnull(row[col]) else "-"
            html_table += f"<td style='padding: 10px; text-align: left;'>{value}</td>"
        html_table += "</tr>"

    html_table += "</tbody></table></div>"

    if container:
        container.markdown(html_table, unsafe_allow_html=True)
    else:
        st.markdown(html_table, unsafe_allow_html=True)


def render_line_chart(df, title="Gráfico de Linhas", container=None):
    """
    Renderiza um gráfico de linhas usando Plotly (sem dependência do PyArrow)
    """
    if not PLOTLY_AVAILABLE:
        error_msg = "⚠️ Plotly não disponível para renderizar gráficos"
        if container:
            container.error(error_msg)
        else:
            st.error(error_msg)
        return
    
    try:
        fig = px.line(df, title=title)
        fig.update_layout(
            showlegend=True,
            height=400,
            xaxis_title="Data",
            yaxis_title="Valor",
            font=dict(size=12)
        )
        if container:
            container.plotly_chart(fig, use_container_width=True)
        else:
            st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        error_msg = f"⚠️ Erro ao renderizar gráfico de linhas: {e}"
        if container:
            container.error(error_msg)
        else:
            st.error(error_msg)


def render_bar_chart(data, title="Gráfico de Barras", container=None):
    """
    Renderiza um gráfico de barras usando Plotly (sem dependência do PyArrow)
    """
    if not PLOTLY_AVAILABLE:
        error_msg = "⚠️ Plotly não disponível para renderizar gráficos"
        if container:
            container.error(error_msg)
        else:
            st.error(error_msg)
        return
    
    try:
        if isinstance(data, pd.Series):
            fig = px.bar(x=data.index, y=data.values, title=title)
        else:
            fig = px.bar(data, title=title)

        fig.update_layout(
            showlegend=True,
            height=400,
            xaxis_title="Categoria",
            yaxis_title="Valor",
            font=dict(size=12)
        )
        if container:
            container.plotly_chart(fig, use_container_width=True)
        else:
            st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        error_msg = f"⚠️ Erro ao renderizar gráfico de barras: {e}"
        if container:
            container.error(error_msg)
        else:
            st.error(error_msg)

# from templates.html_templates import get_calendar_html_template, get_weekday_html, get_calendar_day_html, get_footer_html


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

    # Interface do calendário (CSS temporariamente removido)
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
                key="mes_calendario_widget"
            )

        with col_ano:
            ano_atual = datetime.date.today().year
            # Anos: 2024, 2025, 2026, 2027
            anos_disponiveis = list(range(ano_atual - 1, ano_atual + 3))
            ano_selecionado = st.selectbox(
                "Ano",
                options=anos_disponiveis,
                index=anos_disponiveis.index(
                    ano_atual) if ano_atual in anos_disponiveis else 1,
                key="ano_calendario_widget"
            )

    # Criar o calendário
    cal = calendar.monthcalendar(ano_selecionado, mes_selecionado)
    hoje = datetime.date.today()

    # Nomes dos dias da semana
    dias_semana_abrev = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]

    # Gerar calendário simples (removido HTML templates temporariamente)
    # Templates removidos para debug
    # weekday_template = get_weekday_html()
    # day_template = get_calendar_day_html()

    # Código de geração HTML do calendário removido temporariamente para debug
    # for semana in cal:
    #     for dia in semana:
    #         if dia == 0:
    #             dias_calendario_html += day_template.format(
    #                 classes="calendar-day other-month", dia="")
    #         else:
    #             data_atual = date(ano_selecionado, mes_selecionado, dia)
    #             classes = "calendar-day"
    #
    #             if data_atual == hoje:
    #                 classes += " today"
    #
    #             dias_calendario_html += day_template.format(
    #                 classes=classes, dia=dia)

    # Mostrar informações do calendário de forma elegante
    st.markdown(f"### 📅 {meses[mes_selecionado-1]} de {ano_selecionado}")

    # Criar uma visualização mais elegante do calendário
    dias_semana_completos = ["Domingo", "Segunda",
                             "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
    dias_semana_abrev = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]

    # Cabeçalho dos dias da semana com cores
    col_headers = st.columns(7)
    for i, dia_semana in enumerate(dias_semana_abrev):
        with col_headers[i]:
            if i == 0 or i == 6:  # Domingo ou Sábado
                st.markdown(
                    f"**<span style='color: #FF6B6B;'>{dia_semana}</span>**", unsafe_allow_html=True)
            else:
                st.markdown(f"**{dia_semana}**")

    # Exibir o calendário em grid
    for semana in cal:
        cols_semana = st.columns(7)
        for i, dia in enumerate(semana):
            with cols_semana[i]:
                if dia == 0:
                    st.markdown("<div style='height: 40px;'></div>",
                                unsafe_allow_html=True)
                else:
                    data_atual = datetime.date(
                        ano_selecionado, mes_selecionado, dia)

                    # Destacar o dia de hoje
                    if data_atual == hoje:
                        st.markdown(f"""
                        <div style='
                            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            color: white;
                            text-align: center;
                            padding: 8px;
                            border-radius: 8px;
                            font-weight: bold;
                            margin: 2px;
                        '>{dia}</div>
                        """, unsafe_allow_html=True)
                    # Destacar fins de semana
                    elif i == 0 or i == 6:  # Domingo ou Sábado
                        st.markdown(f"""
                        <div style='
                            background-color: #FFF5F5;
                            color: #FF6B6B;
                            text-align: center;
                            padding: 8px;
                            border-radius: 8px;
                            margin: 2px;
                            border: 1px solid #FFE5E5;
                        '>{dia}</div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style='
                            background-color: #F8F9FA;
                            text-align: center;
                            padding: 8px;
                            border-radius: 8px;
                            margin: 2px;
                            border: 1px solid #E9ECEF;
                        '>{dia}</div>
                        """, unsafe_allow_html=True)

    # Retornar a data selecionada (para integração com o resto do código)
    return datetime.date(ano_selecionado, mes_selecionado, 1)


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

        # Usar selectboxes personalizados em português para melhor controle
        datas_disponiveis = sorted(df_stats.index)

        # Extrair anos e meses únicos das datas disponíveis
        anos_unicos = sorted(list(set([d.year for d in datas_disponiveis])))

        col_ano_meta, col_mes_meta, col_dia_meta = st.columns(3)

        meses_pt_meta = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]

        with col_ano_meta:
            ano_meta_selecionado = st.selectbox(
                "Ano da Meta",
                options=anos_unicos,
                index=0,
                key="ano_meta_inicio"
            )

        # Filtrar meses disponíveis para o ano selecionado
        meses_disponiveis_ano = sorted(list(
            set([d.month for d in datas_disponiveis if d.year == ano_meta_selecionado])))

        with col_mes_meta:
            mes_meta_selecionado = st.selectbox(
                "Mês da Meta",
                options=meses_disponiveis_ano,
                format_func=lambda x: meses_pt_meta[x-1],
                index=0,
                key="mes_meta_inicio"
            )

        # Filtrar dias disponíveis para o ano/mês selecionado
        dias_disponiveis_mes = sorted(list(
            set([d.day for d in datas_disponiveis if d.year == ano_meta_selecionado and d.month == mes_meta_selecionado])))

        with col_dia_meta:
            if dias_disponiveis_mes:
                dia_meta_selecionado = st.selectbox(
                    "Dia da Meta",
                    options=dias_disponiveis_mes,
                    index=len(dias_disponiveis_mes) -
                    1,  # Último dia disponível
                    # Chave única
                    key=f"dia_meta_inicio_{ano_meta_selecionado}_{mes_meta_selecionado}"
                )
            else:
                st.warning("Nenhum dia disponível")
                dia_meta_selecionado = 1

        # Construir a data selecionada
        try:
            data_inicio_meta = datetime.date(
                ano_meta_selecionado, mes_meta_selecionado, dia_meta_selecionado)

            # Verificar se a data existe nos dados
            if data_inicio_meta in datas_disponiveis:
                valor_inicio = df_stats.loc[data_inicio_meta, "Valor"]
            else:
                # Encontrar a data mais próxima
                datas_do_mes = [d for d in datas_disponiveis if d.year ==
                                ano_meta_selecionado and d.month == mes_meta_selecionado]
                if datas_do_mes:
                    data_inicio_meta = max(datas_do_mes)  # Última data do mês
                    valor_inicio = df_stats.loc[data_inicio_meta, "Valor"]
                else:
                    # Fallback para primeira data disponível
                    data_inicio_meta = datas_disponiveis[0]
                    valor_inicio = df_stats.loc[data_inicio_meta, "Valor"]
        except ValueError:
            # Data inválida, usar primeira data disponível
            data_inicio_meta = datas_disponiveis[0]
            valor_inicio = df_stats.loc[data_inicio_meta, "Valor"]

        # Exibir mini calendário visual para referência
        st.markdown("**📅 Calendário de Referência:**")

        # Criar um calendário visual simples para o mês selecionado
        cal = calendar.monthcalendar(
            ano_meta_selecionado, mes_meta_selecionado)

        # Cabeçalho dos dias
        dias_semana = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]
        col_cal = st.columns(7)
        for i, dia_sem in enumerate(dias_semana):
            with col_cal[i]:
                if i == 0 or i == 6:  # Domingo ou Sábado
                    st.markdown(
                        f"**<span style='color: #FF6B6B; font-size: 12px;'>{dia_sem}</span>**", unsafe_allow_html=True)
                else:
                    st.markdown(
                        f"**<span style='font-size: 12px;'>{dia_sem}</span>**", unsafe_allow_html=True)

        # Dias do calendário
        for semana in cal:
            col_sem = st.columns(7)
            for i, dia in enumerate(semana):
                with col_sem[i]:
                    if dia == 0:
                        st.markdown("")
                    else:
                        # Verificar se este dia tem dados disponíveis
                        data_check = datetime.date(ano_meta_selecionado,
                                                   mes_meta_selecionado, dia)

                        if data_check in datas_disponiveis:
                            if dia == dia_meta_selecionado:
                                # Dia selecionado
                                st.markdown(f"""
                                <div style='
                                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                                    color: white;
                                    text-align: center;
                                    padding: 4px;
                                    border-radius: 4px;
                                    font-size: 12px;
                                    font-weight: bold;
                                '>{dia}</div>
                                """, unsafe_allow_html=True)
                            else:
                                # Dia com dados disponíveis
                                st.markdown(f"""
                                <div style='
                                    background-color: #E3F2FD;
                                    color: #1976D2;
                                    text-align: center;
                                    padding: 4px;
                                    border-radius: 4px;
                                    font-size: 12px;
                                    border: 1px solid #BBDEFB;
                                '>{dia}</div>
                                """, unsafe_allow_html=True)
                        else:
                            # Dia sem dados
                            st.markdown(f"""
                            <div style='
                                background-color: #F5F5F5;
                                color: #9E9E9E;
                                text-align: center;
                                padding: 4px;
                                border-radius: 4px;
                                font-size: 12px;
                            '>{dia}</div>
                            """, unsafe_allow_html=True)

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

        # Formatando meses para exibição
        meses_display = meses.copy()

        # Formatando colunas de valor (que realmente existem)
        meses_display["Meta Mensal"] = meses_display["Meta Mensal"].apply(
            lambda x: f"R$ {x:.2f}" if pd.notnull(x) else "-"
        )
        meses_display["Valor"] = meses_display["Valor"].apply(
            lambda x: f"R$ {x:.2f}" if pd.notnull(x) else "-"
        )

        # Formatando colunas percentuais
        meses_display["Atingimento (%)"] = meses_display["Atingimento (%)"].apply(
            lambda x: f"{x:.1f}%" if pd.notnull(x) else "-"
        )
        meses_display["Atingimento Ano"] = meses_display["Atingimento Ano"].apply(
            lambda x: f"{x:.1f}%" if pd.notnull(x) else "-"
        )

        # Formatando Atingimento Esperado (valor decimal)
        meses_display["Atingimento Esperado"] = meses_display["Atingimento Esperado"].apply(
            lambda x: f"{x:.3f}" if pd.notnull(x) else "-"
        )

        render_html_table(meses_display)

    # Retornar os valores solicitados incluindo o DataFrame meses
    return data_inicio_meta, valor_inicio, meta_estimada, patrimonio_final, meses


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

# Seção de boas-vindas usando componentes nativos do Streamlit
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
st.markdown("---")  # Widget de calendário melhorado
with st.expander("📅 Calendário Financeiro", expanded=False):
    st.markdown("### 🗓️ Visualize datas importantes para suas finanças")
    data_calendario = create_calendar_widget()

    # Informações adicionais sobre a data selecionada
    col1, col2, col3 = st.columns(3)

    # Lista de meses em português para exibição
    meses_pt = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

    with col1:
        mes_nome = meses_pt[data_calendario.month - 1]
        st.info(f"📅 **Mês selecionado:** {mes_nome}/{data_calendario.year}")

    with col2:
        dias_no_mes = calendar.monthrange(
            data_calendario.year, data_calendario.month)[1]
        st.info(f"📊 **Dias no mês:** {dias_no_mes} dias")

    with col3:
        dias_uteis = len([d for d in range(1, dias_no_mes + 1)
                         if datetime.date(data_calendario.year, data_calendario.month, d).weekday() < 5])
        st.info(f"💼 **Dias úteis:** {dias_uteis} dias")

# Upload de arquivo com design elegante
st.markdown("### 📂 Carregamento de Dados")
st.info("💡 **Como usar:** Carregue seu arquivo CSV com dados financeiros para começar a análise. O arquivo deve conter as colunas: Data, Valor e Instituição.")

file_upload = st.file_uploader(
    "📥 Selecione seu arquivo CSV",
    type=["csv"],
    help="Carregue um arquivo CSV com suas informações financeiras"
)
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

    exp1 = st.expander("📊 Visualizar Dados", expanded=False)
    df["Valor"] = df["Valor"].astype(float)

    # Formatando a coluna Valor para exibição
    df_display = df.copy()
    df_display["Valor"] = df_display["Valor"].apply(lambda x: f"R$ {x:.2f}")

    exp1.markdown("### 💾 Dados Carregados")
    render_html_table(df_display, exp1)

    exp2 = st.expander("📊 Análise por Instituição", expanded=False)
    df_instituicao = df.pivot_table(
        index="Data", columns="Instituição", values="Valor")

    tab_data, tab_history, tb_share = exp2.tabs(
        ["📊 Dados por Instituição", "📜 Histórico de Evolução", "📈 Participação por Data"])

    with tab_data:
        st.markdown("### 🏦 Dados Organizados por Instituição")
        # Formatando valores para exibição em tabela
        df_instituicao_display = df_instituicao.copy()
        for col in df_instituicao_display.columns:
            df_instituicao_display[col] = df_instituicao_display[col].apply(
                lambda x: f"R$ {x:.2f}" if pd.notnull(x) else "-"
            )
        render_html_table(df_instituicao_display)

    with tab_history:
        st.markdown("### 📈 Evolução Temporal por Instituição")
        render_line_chart(df_instituicao, "Evolução por Instituição")

    with tb_share:
        st.markdown("### 📊 Participação por Data Selecionada")
        date = st.selectbox("📅 Selecione uma data",
                            options=sorted(df_instituicao.index),
                            key="data_participacao")
        render_bar_chart(df_instituicao.loc[date], f"Participação em {date}")

    exp3 = st.expander("📊 Estatísticas Gerais", expanded=False)

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
        # Formatando df_stats para exibição
        df_stats_display = df_stats.copy()
        # Formatando colunas de valor (R$)
        valor_cols = [
            col for col in df_stats_display.columns if 'Valor' in col or 'Diferença' in col]
        for col in valor_cols:
            if 'Rel' not in col:  # Se não for relativo (percentual)
                df_stats_display[col] = df_stats_display[col].apply(
                    lambda x: f"R$ {x:.2f}" if pd.notnull(x) else "-"
                )
        # Formatando colunas percentuais
        perc_cols = [col for col in df_stats_display.columns if 'Rel' in col]
        for col in perc_cols:
            df_stats_display[col] = df_stats_display[col].apply(
                lambda x: f"{x:.2%}" if pd.notnull(x) else "-"
            )
        render_html_table(df_stats_display)

    with tab_abs:
        abs_cols = [
            "Diferença Mensal Absoluta",
            "Média 6M Diferença Mensal Absoluta",
            "Média 12M Diferença Mensal Absoluta",
            "Média 24M Diferença Mensal Absoluta",
        ]
        render_line_chart(df_stats[abs_cols], "Evolução Absoluta")

    with tab_rel:
        rel_cols = [
            "Diferença Mensal Rel",
            "Evolução 6M Relativa",
            "Evolução 12M Relativa",
            "Evolução 24M Relativa",
        ]
        render_line_chart(df_stats[rel_cols], "Evolução Relativa (%)")

    with st.expander("📊 Metas Financeiras", expanded=False):
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
                render_line_chart(
                    meses[["Atingimento Ano"]], "Atingimento de Meta Anual (%)")

        # Informações do dataset
    with st.expander("ℹ️ Informações do Dataset"):
        st.markdown("### 📊 Resumo dos Dados Carregados")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📝 Total de Registros", f"{len(df):,}")
        with col2:
            st.metric("📅 Períodos Analisados", len(df['Data'].unique()))
        with col3:
            st.metric("🏦 Instituições", len(df['Instituição'].unique()))

        # Informações detalhadas
        col_period, col_inst = st.columns(2)
        with col_period:
            st.info(
                f"📈 **Período Analisado:** De {min(df['Data']).strftime('%d/%m/%Y')} até {max(df['Data']).strftime('%d/%m/%Y')}")

        with col_inst:
            instituicoes_list = ', '.join(df['Instituição'].unique().tolist())
            st.info(f"🏢 **Instituições:** {instituicoes_list}")

# Rodapé simples
st.markdown("---")
st.markdown(
    "📱 **Dica:** Use o calendário para visualizar informações específicas de cada mês!")
st.markdown(
    "💡 Para melhores resultados, mantenha seus dados financeiros sempre atualizados.")
