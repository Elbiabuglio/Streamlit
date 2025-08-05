# 💰 Dashboard Financeiro Pessoal

<div align="cente## 🚀 Demonstração

### 🌐 **Aplicação Online**
**👉 [https://finance-control-esb.streamlit.app/](https://finance-control-esb.streamlit.app/)**


## 📖 Sobre o Projeto

O **Dashboard Financeiro Pessoal** é uma aplicação web robusta desenvolvida em **Streamlit** que permite analisar, visualizar e gerenciar suas finanças pessoais de forma intuitiva e profissional. Totalmente otimizada para **Windows** com correções de compatibilidade PyArrow/NumPy, oferece uma experiência estável e completa.

### ✨ Principais Características

- 📊 **Análise de dados financeiros** com gráficos Plotly interativos
- 📅 **Calendário financeiro** interativo para visualização temporal
- 🎯 **Sistema de metas** com cálculos automáticos e projeções SELIC
- 🏦 **Análise por instituição bancária** com comparativos detalhados
- 📈 **Estatísticas avançadas** e análise de tendências
- 🔄 **Integração robusta com API SELIC** do Banco Central
- 🛡️ **Renderização HTML customizada** sem dependências PyArrow
- 🎨 **Interface moderna** responsiva e intuitiva

---

## 🚀 Demonstração

### � **Status do Projeto: Totalmente Funcional** ✅

A aplicação foi **completamente otimizada** e está livre de erros de compatibilidade:
- ✅ **Erro PyArrow DLL**: Resolvido com renderização HTML customizada
- ✅ **Erro NumPy multiarray**: Resolvido com gráficos Plotly
- ✅ **KeyError DataFrame**: Corrigido com referências de colunas adequadas
- ✅ **Estrutura limpa**: Arquivos redundantes removidos

### 🖥️ Como Executar

```bash
# Clone o repositório
git clone https://github.com/Elbiabuglio/Streamlit.git
cd Streamlit

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
streamlit run main.py
```

### Funcionalidades Principais
- **📊 Tabelas**: Renderização HTML sem dependência PyArrow
- **📈 Gráficos**: Plotly interativo substituindo st.line_chart/st.bar_chart
- **📅 Calendário**: Interface visual intuitiva para seleção de datas
- **🎯 Metas**: Cálculos precisos com integração SELIC
- **🏦 Multi-instituições**: Análise comparativa detalhada

---

## 📁 Estrutura do Projeto

```
📂 Streamlit/
├── 📄 main.py                          # ⭐ Aplicação principal (830 linhas)
├── 📄 requirements.txt                 # 📦 Dependências otimizadas
├── 📄 README.md                        # 📚 Documentação completa
├── � Template Controle Financeiro.CSV # 📊 Arquivo exemplo
├── �📂 styles/                          # 🎨 Estilos modulares
│   ├── 📄 calendar_css.py             # 📅 CSS do calendário
│   ├── � main_css.py                 # 🎨 CSS principal
│   └── 📄 main_css_fixed.py           # 🔧 CSS corrigido
├── �📂 templates/                       # 🏗️ Templates HTML
│   └── 📄 html_templates.py           # 📝 Templates reutilizáveis
└── � __pycache__/                     # 🔄 Cache Python
```



## 🛠️ Instalação

### ⚡ **Execução Rápida**

```bash
# 1. Clone o repositório
git clone https://github.com/Elbiabuglio/Streamlit.git
cd Streamlit

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute a aplicação
streamlit run main.py

# 4. Acesse no navegador
# http://localhost:8501
```

### 📋 Pré-requisitos

- **Python 3.12+** (recomendado para melhor compatibilidade)
- **pip** atualizado
- **Navegador moderno** (Chrome, Firefox, Edge)

### 📦 Dependências Principais

```txt
streamlit>=1.47.0    # Framework web principal
pandas>=2.0.0        # Análise de dados
requests>=2.32.0     # API calls (SELIC)
numpy>=1.24.0        # Computação numérica

```

### 🔧 Instalação em Ambiente Virtual (Recomendado)

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
streamlit run main.py
```

### 🐳 **Docker (Opcional)**

Para quem prefere containerização ou deploy em produção:

```bash
# Opção A: Docker Compose (Mais simples)
docker-compose up --build
# Acesse: http://localhost:8501

# Opção B: Docker tradicional
docker build -t dashboard-financeiro .
docker run -p 8501:8501 dashboard-financeiro
```

📖 **Guia completo**: Veja [DOCKER.md](DOCKER.md) para instruções detalhadas.

### ⚡ **Comparação: Execução Direta vs Docker**

| Método | Prós | Contras | Recomendado para |
|--------|------|---------|------------------|
| **Execução Direta** | 🚀 Mais rápido<br>🔧 Debug fácil<br>📦 Menos recursos | 🐍 Dependências Python<br>🏠 Só ambiente local | Uso pessoal, desenvolvimento |
| **Docker** | 🌐 Deploy fácil<br>🛡️ Isolamento<br>📊 Portabilidade | 📈 Mais recursos<br>🔧 Setup inicial | Produção, compartilhamento |

---

## 📊 Funcionalidades

### 🎯 **Principais Recursos**


#### 3. 📅 **Calendário Financeiro Avançado**
- **Navegação intuitiva**: Seletores de mês/ano em português
- **Visualização temporal**: Destaque para datas importantes
- **Dias úteis**: Cálculo automático de períodos de trabalho
- **Interface visual**: Design moderno com CSS customizado

#### 4. 🎯 **Sistema de Metas Completo**
```python
def main_metas(df_stats):
    """Sistema completo de configuração e cálculo de metas"""
```
- **📋 Configuração flexível**: Custos fixos, salários, objetivos
- **📊 Integração SELIC**: Cálculos automáticos com taxa oficial
- **📈 Projeções precisas**: Análise de atingimento mensal e anual
- **🔄 Atualização dinâmica**: Recálculo automático ao alterar parâmetros

#### 5. 🏦 **Análise Multi-instituições**
- **Comparação de performance**: Evolução por banco/corretora
- **Gráficos comparativos**: Visualização de participação e crescimento
- **Tabelas pivotadas**: Organização temporal dos dados
- **Métricas de performance**: KPIs por instituição

#### 6. 📈 **Estatísticas Avançadas**
```python
def calc_general_stats(df):
    """Cálculo de estatísticas e métricas financeiras"""
```
- **Médias móveis**: 6M, 12M, 24M para análise de tendências
- **Diferenças absolutas e relativas**: Crescimento mensal detalhado
- **Evolução temporal**: Análise de variações periódicas
- **Indicadores de performance**: Métricas customizadas


## 🔧 Configuração e Uso

### 📊 **Formato do Arquivo CSV**

Seu arquivo deve seguir esta estrutura **exata**:

```csv
Data,Instituição,Valor
01/01/2024,Banco do Brasil,1500.00
01/02/2024,Itaú,2300.50
01/03/2024,Nubank,800.75
15/03/2024,XP Investimentos,5000.00
```

**📋 Especificações:**
- **Data**: Formato DD/MM/YYYY (suporte automático para outros formatos)
- **Instituição**: Nome da instituição financeira (texto livre)
- **Valor**: Valor numérico com ponto como separador decimal

### 🎯 **Configuração de Metas**

1. **📊 Carregue seus dados** via upload CSV
2. **📅 Selecione data de início** da meta
3. **💰 Configure parâmetros**:
   - Custos fixos mensais
   - Salário bruto e líquido
   - Meta financeira desejada
4. **📈 Acompanhe o progresso** em tempo real


### 📚 **Guia de Uso Passo a Passo**

#### 1. **Primeira Execução**
```bash
# Terminal/CMD
cd caminho/para/Streamlit
streamlit run main.py
```

#### 2. **Preparação dos Dados**
- Exporte dados bancários em CSV
- Verifique formato das colunas
- Salve com codificação UTF-8

#### 3. **Análise Financeira**
- Faça upload do arquivo
- Explore as abas de análise
- Configure metas personalizadas
- Visualize gráficos interativos

#### 4. **Interpretação dos Resultados**
- **Valor**: Patrimônio total na data
- **Diferença Mensal**: Variação entre períodos
- **Médias Móveis**: Tendências suavizadas
- **Atingimento**: Percentual de progresso das metas

---

## 🤝 Contribuição

Contribuições são **muito bem-vindas**! Este projeto está ativo e em constante melhoria.

### 🚀 **Como Contribuir**

1. **🍴 Fork** o projeto
2. **🌟 Crie uma branch** para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. **💡 Commit** suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. **🚀 Push** para a branch (`git push origin feature/nova-funcionalidade`)
5. **📥 Abra um Pull Request**


## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 👨‍💻 Autor

**Elbia**
- GitHub: [@Elbiabuglio](https://github.com/Elbiabuglio)





<div align="center">

### 🌟 **Se este projeto te ajudou, considere dar uma ⭐!**

**💰🚀 Desenvolvido com ❤️ para facilitar o controle das suas finanças 📊📈**

---

[![GitHub stars](https://img.shields.io/github/stars/Elbiabuglio/Streamlit?style=social)](https://github.com/Elbiabuglio/Streamlit/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Elbiabuglio/Streamlit?style=social)](https://github.com/Elbiabuglio/Streamlit/network)

**🔄 Última atualização**: Agosto 2025 • **📊 Status**: Ativo e Funcional • **🛡️ Qualidade**: Estável

</div>
