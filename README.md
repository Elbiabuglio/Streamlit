# 💰 Dashboard Financeiro Pessoal

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.47+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
[![App Online](https://img.shields.io/badge/App-Online-brightgreen.svg)](https://finance-control-esb.streamlit.app/)

**Uma aplicação web interativa para controle e análise de finanças pessoais**

🌐 **[Acesse a aplicação online](https://finance-control-esb.streamlit.app/)**

[🚀 Demonstração](#demonstração) • [📁 Estrutura](#estrutura-do-projeto) • [🛠️ Instalação](#instalação) • [📊 Funcionalidades](#funcionalidades)

</div>

---

## 📖 Sobre o Projeto

O **Dashboard Financeiro Pessoal** é uma aplicação web desenvolvida em **Streamlit** que permite analisar, visualizar e gerenciar suas finanças pessoais de forma intuitiva e profissional. Com integração à API do Banco Central para dados da SELIC e interface moderna, oferece uma visão completa da sua situação financeira.

### ✨ Principais Características

- 📊 **Análise de dados financeiros** com gráficos interativos
- 📅 **Calendário financeiro** interativo para visualização temporal
- 🎯 **Sistema de metas** com cálculos automáticos e projeções
- 🏦 **Análise por instituição bancária** com comparativos
- 📈 **Estatísticas avançadas** e tendências
- 🔄 **Integração com API SELIC** para cálculos de rendimento
- 🎨 **Interface moderna** com CSS e HTML modulares

---

## 🚀 Demonstração

### 🌐 Acesso Direto
**👉 [https://finance-control-esb.streamlit.app/](https://finance-control-esb.streamlit.app/)**

Teste todas as funcionalidades online sem precisar instalar nada!

### Tela Principal
![Dashboard Principal](https://via.placeholder.com/800x400?text=Dashboard+Financeiro)

### Funcionalidades em Ação
- **Calendário Interativo**: Navegue pelos meses e visualize informações financeiras
- **Upload de Dados**: Carregue seus arquivos CSV e veja análises instantâneas
- **Metas Financeiras**: Configure objetivos e acompanhe o progresso
- **Gráficos Dinâmicos**: Visualize tendências e padrões nos seus dados

---

## 📁 Estrutura do Projeto

```
📂 Streamlit/
├── 📄 main.py                          # Aplicação principal
├── 📄 requirements.txt                 # Dependências Python
├── 📄 README.md                        # Documentação
├── 📂 styles/                          # Estilos CSS separados
│   └── 📄 calendar_css.py             # CSS do calendário
├── 📂 templates/                       # Templates HTML
│   └── 📄 html_templates.py           # Templates reutilizáveis
└── 📄 Template Controle Financeiro.CSV # Arquivo de exemplo
```

### 🏗️ Arquitetura Modular

O projeto foi desenvolvido com **separação de responsabilidades**:

- **`main.py`**: Lógica de negócio e interface
- **`styles/`**: Estilos CSS organizados por componente
- **`templates/`**: Templates HTML reutilizáveis
- **Modularidade**: Fácil manutenção e personalização

---

## 🛠️ Instalação

> 💡 **Dica**: Você pode usar a aplicação diretamente online em [https://finance-control-esb.streamlit.app/](https://finance-control-esb.streamlit.app/) sem precisar instalar nada!

### Pré-requisitos

- **Python 3.8+** instalado


### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/Elbiabuglio/Streamlit.git
   cd Streamlit
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação**
   ```bash
   streamlit run main.py
   ```

4. **Acesse no navegador**
   ```
   http://localhost:8501
   ```

### 🐳 Usando Docker (Opcional)

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.address", "0.0.0.0"]
```

```bash
# Construir e executar
docker build -t dashboard-financeiro .
docker run -p 8501:8501 dashboard-financeiro
```

---

## 📊 Funcionalidades

### 1. 📅 **Calendário Financeiro Interativo**
- Navegação por mês/ano
- Visualização de dias úteis
- Interface responsiva e intuitiva
- CSS modular para fácil personalização

### 2. 📈 **Análise de Dados**
- **Upload de CSV**: Carregue seus dados financeiros
- **Visualização de Dados**: Tabelas formatadas e organizadas
- **Análise por Instituição**: Compare performance entre bancos
- **Estatísticas Gerais**: Métricas e indicadores financeiros

### 3. 🎯 **Sistema de Metas Financeiras**
- **Configuração de Metas**: Defina objetivos financeiros
- **Cálculos Automáticos**: Projeções com base na SELIC
- **Acompanhamento**: Visualize progresso e atingimento
- **Gráficos Interativos**: Evolução das metas ao longo do tempo

### 4. 🏦 **Integração com APIs**
- **API SELIC**: Dados atualizados do Banco Central
- **Cache Inteligente**: Otimização de performance
- **Tratamento de Erros**: Fallbacks para indisponibilidade

### 5. 📊 **Visualizações Avançadas**
- **Gráficos Interativos**: Plotly para visualizações dinâmicas
- **Tabelas Formatadas**: Configuração personalizada por coluna
- **Métricas em Tempo Real**: KPIs e indicadores principais
- **Tabs Organizadas**: Interface limpa e navegável

---

## 🔧 Configuração

### Formato do Arquivo CSV

Seu arquivo CSV deve conter as seguintes colunas:

```csv
Data,Instituição,Valor
01/01/2024,Banco do Brasil,1500.00
01/02/2024,Itaú,2300.50
01/03/2024,Nubank,800.75
```

### Configurações Avançadas

**Personalizar Estilos:**
```python
# styles/calendar_css.py
def get_calendar_css():
    return """
    <style>
    .calendar-container {
        /* Seus estilos personalizados */
    }
    </style>
    """
```

**Modificar Templates:**
```python
# templates/html_templates.py
def get_calendar_html_template():
    return """
    <div class="calendar-container">
        <!-- Seu HTML personalizado -->
    </div>
    """
```

---

## 📚 Uso Detalhado

### 1. **Primeiros Passos**
1. Execute a aplicação
2. Navegue pelo calendário para se familiarizar
3. Prepare seu arquivo CSV com dados financeiros
4. Faça upload e explore as análises

### 2. **Análise de Dados**
```python
# Exemplo de uso programático
import pandas as pd

# Seus dados
df = pd.read_csv("seus_dados.csv")
df_stats = calc_general_stats(df)
```

### 3. **Configuração de Metas**
1. Acesse a aba "Metas"
2. Configure custos fixos e salário
3. Defina data de início e objetivos
4. Acompanhe o progresso nos gráficos

---

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. **Fork** o projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. **Push** para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um **Pull Request**

### 💡 Ideias para Contribuição

- [ ] Novos tipos de gráficos
- [ ] Integração com APIs bancárias
- [ ] Exportação em diferentes formatos
- [ ] Temas personalizáveis
- [ ] Notificações e alertas
- [ ] Análise preditiva com ML

---

## 🐛 Problemas Conhecidos

- **Taxa SELIC**: Em caso de indisponibilidade da API, usa valor padrão
- **Formato de Data**: Suporta DD/MM/YYYY, YYYY-MM-DD e detecção automática
- **Navegadores**: Otimizado para Chrome, Firefox e Edge

### 🔧 Soluções

```python
# Tratamento de erros de data
try:
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y")
except:
    df["Data"] = pd.to_datetime(df["Data"], infer_datetime_format=True)
```

---

## 📝 Changelog

### v2.0.0 - Modularização
- ✅ Separação CSS e HTML
- ✅ Estrutura modular
- ✅ Templates reutilizáveis
- ✅ Melhoria na manutenibilidade

### v1.0.0 - Versão Inicial
- ✅ Dashboard básico
- ✅ Integração SELIC
- ✅ Sistema de metas
- ✅ Calendário interativo

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

- **Streamlit** pela excelente framework
- **Banco Central do Brasil** pela API da SELIC
- **Plotly** pelas visualizações interativas
- **Pandas** pelo processamento de dados

---

<div align="center">

### 🌟 Se este projeto te ajudou, considere dar uma ⭐!

**Desenvolvido com ❤️ para facilitar o controle das suas finanças**

</div>