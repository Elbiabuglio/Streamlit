# 💰 Dashboard Financeiro Pessoal

## 🚀 Demonstração

🔗 **Aplicação Online**  
👉 [Acesse o Dashboard](https://finance-control-esb.streamlit.app/)

---

## 📖 Sobre o Projeto

O **Dashboard Financeiro Pessoal** é uma aplicação web desenvolvida em **Streamlit**, voltada para o controle e análise de finanças pessoais de forma intuitiva, interativa e profissional.

Totalmente otimizada para **Windows**, a aplicação inclui correções de compatibilidade (como erros envolvendo PyArrow e NumPy) e oferece uma experiência fluida e estável.

---

## ✨ Principais Funcionalidades

- 📊 **Análise financeira interativa** com gráficos Plotly
- 📅 **Calendário financeiro** com navegação avançada
- 🎯 **Sistema de metas** com integração da taxa SELIC
- 🏦 **Comparativo entre instituições financeiras**
- 📈 **Estatísticas e indicadores personalizados**
- 🔄 **Integração com API da SELIC (Banco Central)**
- 🎨 **Interface responsiva e moderna (HTML/CSS customizado)**
📌 Outros Pontos Relevantes a Melhorar
1. "Status do Projeto" duplicado
Você usa essa seção duas vezes (antes e depois da instalação). Pode consolidar em um único lugar.

2. Evitar excesso de emojis corrompidos (�)
Alguns pontos da estrutura estão com ícones mal renderizados (possivelmente 📄, 📁, etc.). Sugestão: revisar no GitHub direto e, se possível, usar emojis compatíveis com UTF-8.

3. Seção “Execução Rápida” e “Como Executar”
Essas duas seções se repetem com conteúdo similar. Você pode unificá-las para evitar redundância:

md
Copiar
Editar
## 🚀 Como Executar

### Opção 1: Execução Direta

```bash
git clone https://github.com/Elbiabuglio/Streamlit.git
cd Streamlit
pip install -r requirements.txt
streamlit run main.py
Opção 2: Docker
bash
Copiar
Editar
# Docker Compose
docker-compose up --build

# Docker tradicional
docker build -t dashboard-financeiro .
docker run -p 8501:8501 dashboard-financeiro
shell
Copiar
Editar

#### 4. **Título “Funcionalidades Principais” está duplicado**
Você já tem isso no início como “Principais Características”, e repete depois. Poderia organizar assim:

```md
## 📊 Funcionalidades em Destaque
🧼 Pequenas Melhorias de Redação
"Análise de dados financeiros com gráficos Plotly interativos" →
"Visualização interativa de dados com gráficos Plotly"

"Renderização HTML customizada sem dependências PyArrow" →
"Tabelas HTML customizadas, sem dependência do PyArrow"

"Sistema completo de configuração e cálculo de metas" →
"Defina metas financeiras personalizadas com projeções automatizadas"

✅ Finalização
O trecho final está ótimo. A sugestão aqui é só deixar a chamada para o “⭐” mais direta:

md
Copiar
Editar
<div align="center">

### ⭐ Se este projeto foi útil, considere deixar uma estrela!

**Desenvolvido com ❤️ para facilitar o controle das suas finanças pessoais**

---

[![GitHub stars](https://img.shields.io/github/stars/Elbiabuglio/Streamlit?style=social)](https://github.com/Elbiabuglio/Streamlit/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Elbiabuglio/Streamlit?style=social)](https://github.com/Elbiabuglio/Streamlit/network)

**🔄 Última atualização**: Agosto 2025 • **📊 Status**: Ativo e Funcional • **🛡️ Qualidade**: Estável

</div>
🚀 Quer que eu gere o README revisado completo?
Se quiser, posso montar a versão ajustada com todos os pontos acima já aplicados. Deseja?








Você disse:
poderia montar com as melhorias sugeridas


O ChatGPT disse:
Claro, Elbia! Abaixo está o seu README.md revisado com todas as melhorias aplicadas: clareza, estrutura, fluidez, correções de codificação, eliminação de redundâncias e um visual mais profissional.

md
Copiar
Editar
# 💰 Dashboard Financeiro Pessoal

## 🚀 Demonstração

🔗 **Aplicação Online**  
👉 [Acesse o Dashboard](https://finance-control-esb.streamlit.app/)

---

## 📖 Sobre o Projeto

O **Dashboard Financeiro Pessoal** é uma aplicação web desenvolvida com **Streamlit** para facilitar a análise e o controle das suas finanças pessoais, com uma interface moderna, recursos interativos e suporte completo a gráficos e metas financeiras.

O sistema está otimizado para **Windows**, com correções de compatibilidade para erros comuns com **PyArrow** e **NumPy**, garantindo uma experiência estável e fluida.

---

## ✨ Funcionalidades em Destaque

- 📊 Visualização interativa de dados com gráficos Plotly
- 📅 Calendário financeiro com seleção de datas e períodos úteis
- 🎯 Sistema de metas com projeções automáticas usando taxa SELIC
- 🏦 Análise comparativa entre instituições financeiras
- 📈 Estatísticas avançadas com médias móveis e KPIs
- 🔄 Integração com API oficial do Banco Central (SELIC)
- 🎨 Interface HTML responsiva com CSS customizado

---

## 📦 Status do Projeto

✅ **Totalmente funcional e estável**

- ✅ Erros PyArrow e NumPy resolvidos
- ✅ Compatível com Python 3.12+
- ✅ Estrutura de pastas limpa e organizada
- ✅ Interface intuitiva e responsiva

---

## 🖥️ Como Executar

### 💡 Opção 1: Execução Direta

```bash
# Clone o repositório
git clone https://github.com/Elbiabuglio/Streamlit.git
cd Streamlit

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
streamlit run main.py


🐳 Opção 2: Usando Docker
bash
Copiar
Editar
# Docker Compose (recomendado)
docker-compose up --build
# Acesse em: http://localhost:8501

# Docker 
docker build -t dashboard-financeiro .
docker run -p 8501:8501 dashboard-financeiro
📖 Guia completo de Docker: veja DOCKER.md

📋 Pré-requisitos
Python 3.12+

pip atualizado

Navegador moderno (Chrome, Firefox, Edge)

📚 Principais Dependências
txt
Copiar
Editar
streamlit>=1.47.0
pandas>=2.0.0
requests>=2.32.0
numpy>=1.24.0

🧱 Estrutura do Projeto
bash
Copiar
Editar
📂 Streamlit/
├── main.py                          # Aplicação principal
├── requirements.txt                 # Dependências
├── README.md                        # Documentação
├── Template Controle Financeiro.CSV # Arquivo de exemplo
├── styles/
│   ├── calendar_css.py             # CSS do calendário
│   ├── main_css.py                 # Estilo principal
│   └── main_css_fixed.py           # Estilo corrigido
├── templates/
│   └── html_templates.py           # Templates HTML reutilizáveis
└── __pycache__/                    # Cache Python
📊 Recursos Detalhados
📅 Calendário Financeiro Avançado
Seleção de mês e ano em português

Destaque para datas importantes

Cálculo automático de dias úteis

Interface visual com CSS customizado

🎯 Sistema de Metas Financeiras
python
Copiar
Editar
def main_metas(df_stats):
    """Sistema completo de configuração e cálculo de metas"""
Custos fixos, salário líquido e meta desejada

Projeções com taxa SELIC integrada

Acompanhamento do atingimento mensal/anual

Recalculo dinâmico ao alterar dados

🏦 Análise Multi-Instituições
Comparativo de desempenho entre bancos

Gráficos de participação e evolução

Tabelas pivotadas com dados organizados

KPIs financeiros por instituição

📈 Estatísticas Avançadas
python
Copiar
Editar
def calc_general_stats(df):
    """Cálculo de estatísticas e métricas financeiras"""
Médias móveis de 6, 12 e 24 meses

Diferenças absolutas e relativas mensais

Evolução de patrimônio e gastos ao longo do tempo

📁 Formato do Arquivo CSV
csv
Copiar
Editar
Data,Instituição,Valor
01/01/2024,Banco do Brasil,1500.00
01/02/2024,Itaú,2300.50
01/03/2024,Nubank,800.75
15/03/2024,XP Investimentos,5000.00
Requisitos:
Data: Formato DD/MM/AAAA (suporte automático para outros formatos)

Instituição: Nome da instituição financeira

Valor: Número decimal com . como separador

📚 Guia de Uso
🔹 Primeira execução
bash
Copiar
Editar
cd caminho/para/Streamlit
streamlit run main.py
🔹 Preparando seus dados
Exporte os dados em .csv

Confirme que as colunas seguem o formato padrão

Salve o arquivo em UTF-8

🔹 Analisando finanças
Faça o upload do CSV

Navegue pelas abas de análise

Configure metas

Visualize os resultados com gráficos interativos

🔹 Interpretação dos Resultados
Valor: Patrimônio total no período

Diferença Mensal: Comparação entre meses

Médias Móveis: Tendências suavizadas

Atingimento: Progresso em relação às metas

🤝 Contribuições
Contribuições são muito bem-vindas!
Este projeto está ativo e em constante melhoria.

Como contribuir:
Faça um fork

Crie uma branch com a sua feature (git checkout -b feature/minha-funcionalidade)

Commit suas mudanças (git commit -m 'Minha contribuição')

Push para o seu repositório (git push origin feature/minha-funcionalidade)

Abra um Pull Request 🤝

📄 Licença
Distribuído sob a licença MIT.
Veja o arquivo LICENSE para mais informações.

<div align="center">
🌟 Se este projeto te ajudou, considere dar uma estrela!
💰🚀 Desenvolvido com ❤️ para facilitar o controle das suas finanças pessoais 📊




🔄 Última atualização: Agosto 2025
📊 Status: Ativo e funcional
🛡️ Qualidade: Estável

</div> ```