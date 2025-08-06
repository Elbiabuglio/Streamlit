#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dashboard Financeiro Pessoal - Streamlit App

Features: Análise financeira, sistema de metas, calendário interativo, integração SELIC API
Autor: Elbia | v3.0.1 | Python 3.13 | Agosto 2025
Deploy: https://finance-control-esb.streamlit.app/
"""

import streamlit as st
import pandas as pd
import requests
import datetime
import calendar
from datetime import date, timedelta

# Imports com tratamento de erro para Streamlit Cloud
PLOTLY_AVAILABLE = False
try:
    import plotly.express as px
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except ImportError:
    pass  # Será tratado mais tarde na interface
except Exception:
    pass  # Será tratado mais tarde na interface

# =============================================================================
# CONSTANTES E CONFIGURAÇÕES GLOBAIS
# =============================================================================

# Meses e dias da semana em português
MESES_PT = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]
DIAS_SEMANA_ABREV = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]
DIAS_SEMANA_COMPLETOS = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

# Imports CSS/HTML com tratamento de erro
try:
    from styles.calendar_css import get_calendar_css
    from styles.main_css import get_main_css, get_custom_header
    CSS_AVAILABLE = True
except ImportError:
    CSS_AVAILABLE = False
except Exception:
    CSS_AVAILABLE = False

# Imports de templates com tratamento de erro
try:
    from templates.html_templates import get_calendar_html_template, get_weekday_html, get_calendar_day_html, get_footer_html
    TEMPLATES_AVAILABLE = True
except ImportError:
    TEMPLATES_AVAILABLE = False
except Exception:
    TEMPLATES_AVAILABLE = False

# =============================================================================
# FUNÇÕES UTILITÁRIAS CENTRALIZADAS
# =============================================================================
# Funções consolidadas para eliminar duplicações de código:
# - Formatação monetária/percentual padronizada
# - Seletores de data/calendário reutilizáveis  
# - Formatação de DataFrames consistente
# - Métricas e estilos CSS centralizados

def format_currency(value, symbol="R$", decimals=2):
    """Formatação monetária padronizada"""
    return f"{symbol} {value:.{decimals}f}" if pd.notnull(value) else "-"

def format_percentage(value, decimals=1):
    """Formatação percentual padronizada"""
    return f"{value:.{decimals}f}%" if pd.notnull(value) else "-"

def create_month_year_selector(key_prefix, default_month=None, default_year=None):
    """Cria seletores padronizados de mês/ano"""
    col_mes, col_ano = st.columns(2)
    
    if default_month is None:
        default_month = datetime.date.today().month
    if default_year is None:
        default_year = datetime.date.today().year

    with col_mes:
        mes_selecionado = st.selectbox(
            "Mês",
            options=list(range(1, 13)),
            format_func=lambda x: MESES_PT[x-1],
            index=default_month - 1,
            key=f"{key_prefix}_mes"
        )

    with col_ano:
        anos_disponiveis = list(range(default_year - 1, default_year + 3))
        ano_selecionado = st.selectbox(
            "Ano",
            options=anos_disponiveis,
            index=anos_disponiveis.index(default_year) if default_year in anos_disponiveis else 1,
            key=f"{key_prefix}_ano"
        )
    
    return mes_selecionado, ano_selecionado

def create_calendar_day_style(dia, data_atual, hoje, weekend_style=True):
    """Gera estilos CSS para dias do calendário"""
    if data_atual == hoje:
        # Dia atual - destaque especial
        return f"""
        <div style='
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
            padding: 8px;
            border-radius: 8px;
            font-weight: bold;
            margin: 2px;
        '>{dia}</div>
        """
    elif weekend_style and (data_atual.weekday() == 5 or data_atual.weekday() == 6):
        # Fins de semana
        return f"""
        <div style='
            background-color: #FFF5F5;
            color: #FF6B6B;
            text-align: center;
            padding: 8px;
            border-radius: 8px;
            margin: 2px;
            border: 1px solid #FFE5E5;
        '>{dia}</div>
        """
    else:
        # Dias normais
        return f"""
        <div style='
            background-color: #F8F9FA;
            text-align: center;
            padding: 8px;
            border-radius: 8px;
            margin: 2px;
            border: 1px solid #E9ECEF;
        '>{dia}</div>
        """

def create_mini_calendar_day_style(dia, data_atual, data_selecionada, datas_disponiveis):
    """Gera estilos CSS para mini calendários"""
    if data_atual in datas_disponiveis:
        if data_atual.day == data_selecionada:
            # Dia selecionado
            return f"""
            <div style='
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                text-align: center;
                padding: 4px;
                border-radius: 4px;
                font-size: 12px;
                font-weight: bold;
            '>{dia}</div>
            """
        else:
            # Dia com dados
            return f"""
            <div style='
                background-color: #E3F2FD;
                color: #1976D2;
                text-align: center;
                padding: 4px;
                border-radius: 4px;
                font-size: 12px;
                border: 1px solid #BBDEFB;
            '>{dia}</div>
            """
    else:
        # Dia sem dados
        return f"""
        <div style='
            background-color: #F5F5F5;
            color: #9E9E9E;
            text-align: center;
            padding: 4px;
            border-radius: 4px;
            font-size: 12px;
        '>{dia}</div>
        """


def render_html_table(df, container=None):
    """Renderiza tabela com st.dataframe"""
    if container:
        container.dataframe(df, use_container_width=True)
    else:
        st.dataframe(df, use_container_width=True)

def format_dataframe_for_display(df, currency_cols=None, percentage_cols=None):
    """Aplica formatação consistente em DataFrames"""
    df_display = df.copy()
    
    if currency_cols:
        for col in currency_cols:
            if col in df_display.columns:
                df_display[col] = df_display[col].apply(format_currency)
    
    if percentage_cols:
        for col in percentage_cols:
            if col in df_display.columns:
                df_display[col] = df_display[col].apply(format_percentage)
                
    return df_display

def create_info_metrics(data_dict, columns=4):
    """Cria métricas em colunas com formatação automática"""
    cols = st.columns(columns)
    for i, (label, value) in enumerate(data_dict.items()):
        with cols[i % columns]:
            if isinstance(value, (int, float)):
                # Formatação automática
                if value >= 1000000:
                    st.metric(label, f"R$ {value/1000000:.1f}M")
                elif value >= 1000:
                    st.metric(label, f"R$ {value/1000:.1f}K")
                else:
                    st.metric(label, format_currency(value))
            else:
                st.metric(label, str(value))

# Imports de templates com tratamento de erro
try:
    from templates.html_templates import get_calendar_html_template, get_weekday_html, get_calendar_day_html, get_footer_html
    TEMPLATES_AVAILABLE = True
except ImportError:
    TEMPLATES_AVAILABLE = False
except Exception:
    TEMPLATES_AVAILABLE = False


@st.cache_data(ttl="1day")
def get_selic():
    """Obtém dados SELIC do BCB com cache de 1 dia"""
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
    """Widget de calendário interativo com seleção de datas"""
    # Interface do calendário
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        # Usar função centralizada
        mes_selecionado, ano_selecionado = create_month_year_selector("calendario_widget")

    # Criar o calendário
    cal = calendar.monthcalendar(ano_selecionado, mes_selecionado)
    hoje = datetime.date.today()

    # Mostrar informações do calendário
    st.markdown(f"### 📅 {MESES_PT[mes_selecionado-1]} de {ano_selecionado}")

    # Cabeçalho dos dias da semana
    col_headers = st.columns(7)
    for i, dia_semana in enumerate(DIAS_SEMANA_ABREV):
        with col_headers[i]:
            if i == 0 or i == 6:  # Domingo ou Sábado
                st.markdown(
                    f"**<span style='color: #FF6B6B;'>{dia_semana}</span>**", unsafe_allow_html=True)
            else:
                st.markdown(f"**{dia_semana}**")

    # Exibir calendário em grid
    for semana in cal:
        cols_semana = st.columns(7)
        for i, dia in enumerate(semana):
            with cols_semana[i]:
                if dia == 0:
                    st.markdown("<div style='height: 40px;'></div>",
                                unsafe_allow_html=True)
                else:
                    data_atual = datetime.date(ano_selecionado, mes_selecionado, dia)
                    # Usar função centralizada
                    weekend_style = (i == 0 or i == 6)  # Fins de semana
                    html_day = create_calendar_day_style(dia, data_atual, hoje, weekend_style)
                    st.markdown(html_day, unsafe_allow_html=True)

    # Retornar data selecionada
    return datetime.date(ano_selecionado, mes_selecionado, 1)


def calc_general_stats(df):
    """Calcula estatísticas financeiras avançadas e métricas de performance"""
    # Ordenar e agrupar dados
    df_sorted = df.sort_values('Data')
    df_data = df_sorted.groupby(by="Data")["Valor"].sum().to_frame()
    df_data = df_data.sort_index()  # Ordem cronológica

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
    """Interface de configuração e cálculo de metas financeiras"""
    # Seção de configuração de metas
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

        # Extrair datas disponíveis do DataFrame
        datas_disponiveis = sorted(df_stats.index)
        
        # Usar função centralizada para seletores de mês/ano
        anos_unicos = sorted(list(set([d.year for d in datas_disponiveis])))
        col_ano_meta, col_mes_meta, col_dia_meta = st.columns(3)

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
                format_func=lambda x: MESES_PT[x-1],  # Usar constante centralizada
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
                    index=len(dias_disponiveis_mes) - 1,  # Último dia disponível
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
        col_cal = st.columns(7)
        for i, dia_sem in enumerate(DIAS_SEMANA_ABREV):  # Usar constante centralizada
            with col_cal[i]:
                if i == 0 or i == 6:  # Domingo ou Sábado
                    st.markdown(
                        f"**<span style='color: #FF6B6B; font-size: 12px;'>{dia_sem}</span>**", unsafe_allow_html=True)
                else:
                    st.markdown(
                        f"**<span style='font-size: 12px;'>{dia_sem}</span>**", unsafe_allow_html=True)

        # Dias do calendário usando função centralizada
        for semana in cal:
            col_sem = st.columns(7)
            for i, dia in enumerate(semana):
                with col_sem[i]:
                    if dia == 0:
                        st.markdown("")
                    else:
                        # Usar função centralizada para estilo do mini calendário
                        data_check = datetime.date(ano_meta_selecionado, mes_meta_selecionado, dia)
                        html_day = create_mini_calendar_day_style(
                            dia, data_check, dia_meta_selecionado, datas_disponiveis
                        )
                        st.markdown(html_day, unsafe_allow_html=True)

        st.markdown(
            f"**Patrimônio no Início da Meta:** {format_currency(valor_inicio)}")  # Usar função centralizada

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
            st.markdown(format_currency(mensal))  # Usar função centralizada

    with col2_pot:
        with st.container(border=True):
            st.markdown("**Potencial Arrecadação Anual**")
            st.markdown(format_currency(anual))  # Usar função centralizada

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
        # Configurando meses para exibição usando função centralizada
        meses_display = meses.copy()

        # Definir colunas de moeda e percentual
        currency_cols = ["Meta Mensal", "Valor"]
        percentage_cols = ["Atingimento (%)", "Atingimento Ano"]
        
        # Aplicar formatação usando função centralizada
        meses_display = format_dataframe_for_display(
            meses_display, 
            currency_cols=currency_cols, 
            percentage_cols=percentage_cols
        )

        # Formatando Atingimento Esperado (valor decimal) - caso especial
        meses_display["Atingimento Esperado"] = meses_display["Atingimento Esperado"].apply(
            lambda x: f"{x:.3f}" if pd.notnull(x) else "-"
        )

        render_html_table(meses_display)

    # Retornar os valores solicitados incluindo o DataFrame meses
    return data_inicio_meta, valor_inicio, meta_estimada, patrimonio_final, meses


# =============================================================================
# CONFIGURAÇÃO DA APLICAÇÃO
# =============================================================================

# Configuração da página
st.set_page_config(
    page_title="Finanças Pessoais",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =============================================================================
# CABEÇALHO E INTERFACE PRINCIPAL
# =============================================================================

# Cabeçalho principal
st.title("💰 Finanças Pessoais")
st.subheader("Seu painel de controle financeiro inteligente")

# Seção de boas-vindas
st.markdown("### ✨ Bem-vindo ao seu painel de controle financeiro!")

# Cards com funcionalidades
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

# =============================================================================
# CALENDÁRIO FINANCEIRO
# =============================================================================

# Expander para o calendário
with st.expander("📅 Calendário Financeiro", expanded=False):
    st.markdown("### 🗓️ Visualize datas importantes para suas finanças")

    # Widget de calendário
    data_calendario = create_calendar_widget()

    # Informações complementares
    col1, col2, col3 = st.columns(3)

    # Cards informativos
    with col1:
        mes_nome = MESES_PT[data_calendario.month - 1]  # Constante centralizada
        st.info(f"📅 **Mês selecionado:** {mes_nome}/{data_calendario.year}")

    with col2:
        dias_no_mes = calendar.monthrange(
            data_calendario.year, data_calendario.month)[1]
        st.info(f"📊 **Dias no mês:** {dias_no_mes} dias")

    with col3:
        dias_uteis = len([d for d in range(1, dias_no_mes + 1)
                         if datetime.date(data_calendario.year, data_calendario.month, d).weekday() < 5])
        st.info(f"💼 **Dias úteis:** {dias_uteis} dias")

# =============================================================================
# UPLOAD E PROCESSAMENTO DE DADOS
# =============================================================================

st.markdown("### 📂 Carregamento de Dados")

# Instruções para o usuário
st.info("💡 **Como usar:** Carregue seu arquivo CSV com dados financeiros para começar a análise. O arquivo deve conter as colunas: Data, Valor e Instituição.")

# Widget de upload
file_upload = st.file_uploader(
    "📥 Selecione seu arquivo CSV",
    type=["csv"],
    help="Carregue um arquivo CSV com suas informações financeiras"
)

# Processamento se arquivo foi carregado
if file_upload:

    # Leitura do CSV
    df = pd.read_csv(file_upload)

    # Tratamento de diferentes formatos de data
    # Tentativa 1: DD/MM/YYYY
    try:
        df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y").dt.date
    except:
        # Tentativa 2: YYYY-MM-DD
        try:
            df["Data"] = pd.to_datetime(df["Data"], format="%Y-%m-%d").dt.date
        except:
            # Tentativa 3: Detecção automática
            try:
                df["Data"] = pd.to_datetime(
                    df["Data"], infer_datetime_format=True).dt.date
            except Exception as e:
                # Erro: para execução
                st.error(f"Erro ao converter datas: {e}")
                st.stop()

    # Visualização dos dados brutos
    exp1 = st.expander("📊 Visualizar Dados", expanded=False)

    # Conversão e formatação
    df["Valor"] = df["Valor"].astype(float)

    # Formatação usando função centralizada
    df_display = format_dataframe_for_display(df, currency_cols=["Valor"])

    # Renderização da tabela
    exp1.markdown("### 💾 Dados Carregados")
    render_html_table(df_display, exp1)

    # Análise por instituição

    exp2 = st.expander("📊 Análise por Instituição", expanded=False)
    df_instituicao = df.pivot_table(
        index="Data", columns="Instituição", values="Valor")

    tab_data, tab_history, tb_share = exp2.tabs(
        ["📊 Dados por Instituição", "📜 Histórico de Evolução", "📈 Participação por Data"])

    with tab_data:
        st.markdown("### 🏦 Dados Organizados por Instituição")
        # Formatação usando função centralizada
        df_instituicao_display = format_dataframe_for_display(
            df_instituicao, currency_cols=df_instituicao.columns.tolist()
        )
        render_html_table(df_instituicao_display)

    with tab_history:
        st.markdown("### 📈 Evolução Temporal por Instituição")
        st.subheader("Evolução por Instituição")
        if not df_instituicao.empty:
            st.line_chart(df_instituicao)
        else:
            st.warning("Dados insuficientes para gráfico de evolução temporal.")

    with tb_share:
        st.markdown("### 📊 Participação por Data Selecionada")
        if not df_instituicao.empty:
            date = st.selectbox("📅 Selecione uma data",
                                options=sorted(df_instituicao.index),
                                key="data_participacao")
            st.subheader(f"Participação em {date}")
            data_serie = df_instituicao.loc[date].dropna()
            if not data_serie.empty:
                st.bar_chart(data_serie)
            else:
                st.warning(f"Dados indisponíveis para {date}.")
        else:
            st.warning("Dados insuficientes para análise por data.")

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
        # Formatação usando função centralizada
        valor_cols = [col for col in df_stats.columns if 'Valor' in col or ('Diferença' in col and 'Rel' not in col)]
        perc_cols = [col for col in df_stats.columns if 'Rel' in col]
        
        df_stats_display = format_dataframe_for_display(
            df_stats, 
            currency_cols=valor_cols,
            percentage_cols=perc_cols
        )
        render_html_table(df_stats_display)

    with tab_abs:
        abs_cols = [
            "Diferença Mensal Absoluta",
            "Média 6M Diferença Mensal Absoluta",
            "Média 12M Diferença Mensal Absoluta",
            "Média 24M Diferença Mensal Absoluta",
        ]
        st.subheader("Evolução Absoluta")
        # Verificar colunas disponíveis
        available_cols = [col for col in abs_cols if col in df_stats.columns]
        if available_cols and not df_stats[available_cols].dropna().empty:
            st.line_chart(df_stats[available_cols])
        else:
            st.warning("Dados insuficientes para gráfico de evolução absoluta.")

    with tab_rel:
        rel_cols = [
            "Diferença Mensal Rel",
            "Evolução 6M Relativa",
            "Evolução 12M Relativa",
            "Evolução 24M Relativa",
        ]
        st.subheader("Evolução Relativa (%)")
        # Verificar colunas disponíveis
        available_rel_cols = [
            col for col in rel_cols if col in df_stats.columns]
        if available_rel_cols and not df_stats[available_rel_cols].dropna().empty:
            st.line_chart(df_stats[available_rel_cols])
        else:
            st.warning("Dados insuficientes para gráfico de evolução relativa.")

    with st.expander("📊 Metas Financeiras", expanded=False):
        # Tabs para organizar seção de metas
        tab_main, tab_data_meta, tab_graph = st.tabs(
            ["📋 Configuração", "📊 Dados", "📈 Gráficos"])

        with tab_main:
            # Função principal de metas
            data_inicio_meta, valor_inicio, meta_estimada, patrimonio_final, meses = main_metas(
                df_stats)

        with tab_data_meta:
            st.markdown("### 📊 Dados das Metas")
            # Função centralizada para métricas
            if 'data_inicio_meta' in locals():
                metas_metrics = {
                    "Data Início": data_inicio_meta.strftime("%d/%m/%Y"),
                    "Valor Inicial": valor_inicio,
                    "Meta Estimada": meta_estimada,
                    "Patrimônio Final": patrimonio_final
                }
                
                create_info_metrics(metas_metrics, columns=4)

        with tab_graph:
            st.markdown("### 📈 Gráficos das Metas")
            # Gráficos relacionados às metas
            if 'meses' in locals() and not meses.empty:
                if "Atingimento Ano" in meses.columns:
                    st.subheader("Atingimento de Meta Anual (%)")
                    # Filtrar apenas valores não nulos para o gráfico
                    meses_chart = meses[["Atingimento Ano"]].dropna()
                    if not meses_chart.empty:
                        st.line_chart(meses_chart)
                    else:
                        st.info("Dados insuficientes para gráfico de metas.")
                else:
                    st.warning("Dados de atingimento indisponíveis.")
            else:
                st.info("Configure metas na aba 'Configuração' para ver gráficos.")

    # Informações do dataset

    with st.expander("ℹ️ Informações do Dataset"):
        st.markdown("### 📊 Resumo dos Dados Carregados")

        # Métricas principais usando função centralizada
        dataset_metrics = {
            "📝 Total de Registros": len(df),
            "📅 Períodos Analisados": len(df['Data'].unique()),
            "🏦 Instituições": len(df['Instituição'].unique())
        }
        
        create_info_metrics(dataset_metrics, columns=3)

        # Informações detalhadas
        col_period, col_inst = st.columns(2)

        # Período analisado
        with col_period:
            st.info(f"📈 **Período:** {min(df['Data']).strftime('%d/%m/%Y')} até {max(df['Data']).strftime('%d/%m/%Y')}")

        # Lista de instituições
        with col_inst:
            instituicoes_list = ', '.join(df['Instituição'].unique().tolist())
            st.info(f"🏢 **Instituições:** {instituicoes_list}")

# =============================================================================
# RODAPÉ
# =============================================================================

# Separador visual
st.markdown("---")

# Dicas de uso
st.markdown("📱 **Dica:** Use o calendário para visualizar informações específicas de cada mês!")

# Orientação sobre manutenção dos dados
st.markdown("💡 Para melhores resultados, mantenha seus dados financeiros sempre atualizados.")
