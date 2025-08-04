# 💰 Dashboard Financeiro Pessoal

<div align="center">

![Python](h```
📂 Streamlit/
├── 📄 main.py                          # ⭐ Aplicação principal (830 linhas)
├── 📄 requirements.txt                 # 📦 Dependências otimizadas
├── 📄 README.md                        # 📚 Documentação completa
├── 📄 DOCKER.md                        # 🐳 Guia Docker detalhado
├── 📄 Dockerfile                       # 🐳 Configuração Docker
├── 📄 docker-compose.yml               # 🐳 Orquestração de containers
├── 📄 .dockerignore                    # 🐳 Exclusões para build Docker
├── 📄 Template Controle Financeiro.CSV # 📊 Arquivo exemplo
├── 📂 styles/                          # 🎨 Estilos modulares
│   ├── 📄 calendar_css.py             # 📅 CSS do calendário
│   ├── 📄 main_css.py                 # 🎨 CSS principal
│   └── 📄 main_css_fixed.py           # 🔧 CSS corrigido
├── 📂 templates/                       # 🏗️ Templates HTML
│   └── 📄 html_templates.py           # 📝 Templates reutilizáveis
└── 📂 __pycache__/                     # 🔄 Cache Python
```elds.io/badge/Python-3.12+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.47+-red.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)

**Uma aplicação web interativa robusta para controle e análise de finanças pessoais**

**✅ Sem erros de compatibilidade PyArrow/NumPy** • **🔧 Totalmente funcional** • **🎨 Interface moderna**

[🚀 Demonstração](#demonstração) • [📁 Estrutura](#estrutura-do-projeto) • [🛠️ Instalação](#instalação) • [📊 Funcionalidades](#funcionalidades)

</div>

---

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

### 🏗️ Arquitetura Otimizada

**Principais Melhorias de Estabilidade:**

- **🛡️ `render_html_table()`**: Substituição completa do st.dataframe() para eliminar erros PyArrow
- **📊 `render_line_chart()` e `render_bar_chart()`**: Gráficos Plotly substituindo funcionalidades nativas
- **🔧 Tratamento de erros robusto**: Fallbacks para APIs indisponíveis
- **📂 Estrutura limpa**: Apenas arquivos necessários (main_simple.py removido)

### 🎯 Funcionalidades Core

| Função | Localização | Descrição |
|--------|------------|-----------|
| `render_html_table()` | main.py:17 | Tabelas HTML sem PyArrow |
| `render_line_chart()` | main.py:36 | Gráficos de linha Plotly |
| `render_bar_chart()` | main.py:55 | Gráficos de barra Plotly |
| `main_metas()` | main.py:288 | Sistema completo de metas |
| `calc_general_stats()` | main.py:256 | Estatísticas financeiras |

---

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
plotly>=5.0.0        # Gráficos interativos (substitui PyArrow)
requests>=2.32.0     # API calls (SELIC)
numpy>=1.24.0        # Computação numérica
pyarrow==15.0.2      # Backup (não usado ativamente)
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

#### 1. � **Renderização de Tabelas Otimizada**
```python
def render_html_table(df, container=None):
    """Renderiza tabelas HTML sem dependência PyArrow"""
```
- ✅ **Sem erros DLL**: Eliminação completa de dependências PyArrow problemáticas
- 🎨 **Estilização customizada**: CSS incorporado para aparência profissional
- 📱 **Responsivo**: Adaptação automática para diferentes tamanhos de tela
- ⚡ **Performance**: Renderização mais rápida que componentes nativos

#### 2. 📈 **Gráficos Interativos Plotly**
```python
def render_line_chart(df, title, container=None):
def render_bar_chart(data, title, container=None):
```
- 🔧 **Substituição robusta**: Plotly no lugar de st.line_chart/st.bar_chart
- 🎯 **Interatividade completa**: Zoom, hover, filtros dinâmicos
- 🛡️ **Tratamento de erros**: Fallbacks e mensagens informativas
- 📊 **Múltiplos tipos**: Linhas, barras, séries temporais

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

### 🔧 **Funcionalidades Técnicas**

#### ✅ **Correções de Compatibilidade**
| Problema Original | Solução Implementada | Status |
|------------------|---------------------|---------|
| `PyArrow DLL load failed` | `render_html_table()` | ✅ Resolvido |
| `numpy.core.multiarray` | Gráficos Plotly | ✅ Resolvido |
| `KeyError: 'Valor Acumulado'` | Correção de colunas | ✅ Resolvido |
| Arquivos duplicados | Limpeza estrutural | ✅ Resolvido |

#### 🛡️ **Tratamento de Erros Robusto**
```python
try:
    # Operação principal
    resultado = operacao_principal()
except Exception as e:
    # Fallback e logging
    st.error(f"⚠️ Erro: {e}")
    resultado = valor_padrao
```

#### 🔄 **Integração API SELIC**
- **Cache inteligente**: TTL de 1 dia para otimização
- **Fallback robusto**: Valores padrão em caso de indisponibilidade
- **Tratamento de datas**: Compatibilidade com diferentes formatos
- **Validação de dados**: Verificação de integridade dos dados recebidos

---

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

### 🛠️ **Personalização Avançada**

#### Modificar Estilos de Tabela:
```python
def render_html_table(df, container=None):
    # Personalizar CSS aqui
    html_table = "<div style='overflow-x: auto;'>"
    # Seus estilos customizados
```

#### Configurar Gráficos:
```python
def render_line_chart(df, title="Seu Título", container=None):
    fig = px.line(df, title=title)
    fig.update_layout(
        height=400,  # Altura personalizada
        # Suas configurações
    )
```

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

### 💡 **Ideias para Contribuição**

#### 🔧 **Melhorias Técnicas**
- [ ] **Testes automatizados**: Implementar suite de testes com pytest
- [ ] **Docker**: Container otimizado para deploy fácil
- [ ] **CI/CD**: GitHub Actions para automação
- [ ] **Logging**: Sistema de logs mais robusto

#### 📊 **Novas Funcionalidades**
- [ ] **Importação bancária**: Integração com APIs de bancos (Open Banking)
- [ ] **Machine Learning**: Previsões de gastos e receitas
- [ ] **Alertas inteligentes**: Notificações personalizadas
- [ ] **Categorização automática**: ML para classificar transações
- [ ] **Comparação com índices**: IPCA, CDI, IBOVESPA
- [ ] **Relatórios PDF**: Exportação automática de relatórios

#### 🎨 **Interface e UX**
- [ ] **Dark mode**: Tema escuro alternativo
- [ ] **Responsividade mobile**: Otimização para smartphones
- [ ] **Widgets customizáveis**: Dashboard personalizável
- [ ] **Internacionalização**: Suporte a múltiplos idiomas
- [ ] **Acessibilidade**: Melhorias para screen readers

#### 🔗 **Integrações**
- [ ] **Google Sheets**: Sincronização automática
- [ ] **WhatsApp**: Alertas via bot
- [ ] **Telegram**: Notificações personalizadas
- [ ] **Email**: Relatórios automáticos por email

### 🐛 **Reportar Bugs**

Encontrou um problema? **Abra uma issue** com:
- **📋 Descrição detalhada** do problema
- **🔄 Passos para reproduzir** o erro
- **💻 Ambiente**: SO, versão Python, dependências
- **📸 Screenshots** se aplicável

### 🏆 **Reconhecimento**

Contribuidores serão reconhecidos no README e na aplicação!

### 📞 **Contato para Colaboração**

- **📧 Email**: [seu-email@exemplo.com]
- **💬 GitHub Discussions**: Para discussões técnicas
- **🐛 Issues**: Para bugs e melhorias

---

## 🐛 Solução de Problemas

### ✅ **Problemas Resolvidos**

| Erro Original | Causa | Solução Implementada | Status |
|---------------|-------|---------------------|---------|
| `ImportError: DLL load failed while importing lib` | PyArrow incompatibilidade Windows | `render_html_table()` | ✅ **Resolvido** |
| `numpy.core.multiarray falhou ao importar` | Conflito NumPy/PyArrow charts | Gráficos Plotly | ✅ **Resolvido** |
| `KeyError: 'Valor Acumulado'` | Referência coluna inexistente | Correção referencias DataFrame | ✅ **Resolvido** |
| Arquivos duplicados (`main_simple.py`) | Estrutura desorganizada | Limpeza estrutural | ✅ **Resolvido** |

### 🔧 **Diagnóstico e Correções**

#### **Erro de Importação PyArrow:**
```python
# ❌ Problema original
st.dataframe(df)  # Causava: DLL load failed

# ✅ Solução implementada
render_html_table(df)  # HTML puro, sem PyArrow
```

#### **Erro de Gráficos NumPy:**
```python
# ❌ Problema original
st.line_chart(df)  # Causava: multiarray falhou

# ✅ Solução implementada
render_line_chart(df)  # Plotly interativo
```

#### **Erro de Colunas DataFrame:**
```python
# ❌ Problema original
df["Valor Acumulado"]  # Coluna inexistente

# ✅ Solução implementada
df["Valor"]  # Coluna existente validada
```

### � **Problemas Conhecidos e Workarounds**

#### **API SELIC Indisponível:**
```python
try:
    selic_data = get_selic()
except:
    selic_default = 10.75  # Fallback automático
    st.warning("🔄 Usando taxa SELIC padrão")
```

#### **Formatos de Data Diversos:**
```python
# Tentativa múltipla de conversão
try:
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y")
except:
    try:
        df["Data"] = pd.to_datetime(df["Data"], format="%Y-%m-%d")
    except:
        df["Data"] = pd.to_datetime(df["Data"], infer_datetime_format=True)
```

### 🔍 **Verificação de Integridade**

#### **Checklist de Funcionamento:**
- [ ] ✅ Aplicação inicia sem erros
- [ ] ✅ Upload de CSV funcional
- [ ] ✅ Tabelas são renderizadas corretamente
- [ ] ✅ Gráficos aparecem sem erros
- [ ] ✅ Calendário é interativo
- [ ] ✅ Metas são calculadas corretamente
- [ ] ✅ API SELIC responde ou usa fallback

#### **Comandos de Teste:**
```bash
# Verificar dependências
pip list | grep -E "(streamlit|pandas|plotly)"

# Testar importações
python -c "import streamlit, pandas, plotly; print('✅ Importações OK')"

# Executar aplicação
streamlit run main.py
```

---

## 📝 Changelog

### 🔄 **v3.0.0 - Versão Estável (Atual)**
- ✅ **Correção PyArrow**: Implementação `render_html_table()` eliminando erros DLL
- ✅ **Correção NumPy**: Substituição por gráficos Plotly interativos
- ✅ **Correção KeyError**: Ajuste de referências de colunas DataFrame
- ✅ **Limpeza estrutural**: Remoção de arquivos redundantes
- ✅ **Documentação completa**: README atualizado com detalhes técnicos
- ✅ **Tratamento de erros robusto**: Fallbacks para todas as operações críticas

### 📊 **v2.0.0 - Modularização**
- ✅ Separação CSS e HTML em módulos
- ✅ Estrutura modular para manutenibilidade
- ✅ Templates HTML reutilizáveis
- ✅ Melhoria na organização do código

### 🚀 **v1.0.0 - Versão Inicial**
- ✅ Dashboard básico funcional
- ✅ Integração com API SELIC
- ✅ Sistema de metas financeiras
- ✅ Calendário interativo
- ❌ Problemas de compatibilidade PyArrow/NumPy (resolvidos em v3.0.0)

### 🔧 **Estatísticas de Desenvolvimento**
- **Total de linhas**: 830+ linhas em main.py
- **Funções principais**: 6 funções core implementadas
- **Correções de bugs**: 4 problemas críticos resolvidos
- **Compatibilidade**: 100% funcional em ambiente Windows
- **Dependências**: 6 bibliotecas principais otimizadas

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 👨‍💻 Autor

**Elbia**
- GitHub: [@Elbiabuglio](https://github.com/Elbiabuglio)
- LinkedIn: [Seu LinkedIn](https://linkedin.com/in/seu-perfil)

---

## 🙏 Agradecimentos

### 🛠️ **Tecnologias e Bibliotecas**
- **🎨 [Streamlit](https://streamlit.io/)**: Framework web Python incrível
- **📊 [Plotly](https://plotly.com/)**: Gráficos interativos de alta qualidade
- **🐼 [Pandas](https://pandas.pydata.org/)**: Manipulação de dados poderosa
- **🏦 [Banco Central do Brasil](https://www.bcb.gov.br/)**: API SELIC gratuita e confiável
- **🔢 [NumPy](https://numpy.org/)**: Computação científica fundamental
- **🌐 [Requests](https://docs.python-requests.org/)**: HTTP library elegante

### 👥 **Comunidade**
- **Stack Overflow**: Soluções para desafios técnicos
- **GitHub Community**: Inspiração e melhores práticas
- **Streamlit Community**: Suporte e documentação excelente
- **Python Brasil**: Comunidade Python brasileira acolhedora

### 🔧 **Ferramentas de Desenvolvimento**
- **VS Code**: Editor de código principal
- **Git**: Controle de versões
- **Windows Terminal**: Interface de linha de comando
- **Python**: Linguagem de programação base

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para detalhes completos.

**Resumo da Licença MIT:**
- ✅ **Uso comercial** permitido
- ✅ **Modificação** permitida
- ✅ **Distribuição** permitida
- ✅ **Uso privado** permitido
- ❗ **Sem garantia** ou responsabilidade do autor

---

## 👨‍💻 Autor

**Elbia**
- 🐙 **GitHub**: [@Elbiabuglio](https://github.com/Elbiabuglio)
- 💼 **LinkedIn**: [Conectar no LinkedIn](https://linkedin.com/in/seu-perfil)
- 📧 **Email**: [Contato direto](mailto:seu-email@exemplo.com)
- 🌐 **Website**: [Site pessoal](https://seu-site.com)

### 📊 **Estatísticas do Projeto**
- **⭐ Stars**: Se ajudou, considere dar uma estrela!
- **🍴 Forks**: Contribuições são bem-vindas
- **🐛 Issues**: Problemas são oportunidades de melhoria
- **👥 Contributors**: Reconhecimento para todos os colaboradores

---

<div align="center">

### 🌟 **Se este projeto te ajudou, considere dar uma ⭐!**

**💰🚀 Desenvolvido com ❤️ para facilitar o controle das suas finanças 📊📈**

---

[![GitHub stars](https://img.shields.io/github/stars/Elbiabuglio/Streamlit?style=social)](https://github.com/Elbiabuglio/Streamlit/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Elbiabuglio/Streamlit?style=social)](https://github.com/Elbiabuglio/Streamlit/network)

**🔄 Última atualização**: Agosto 2025 • **📊 Status**: Ativo e Funcional • **🛡️ Qualidade**: Estável

</div>