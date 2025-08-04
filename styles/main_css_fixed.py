"""
CSS principal para estilização moderna e elegante da aplicação
"""


def get_main_css():
    """Retorna o CSS principal para tornar a aplicação mais elegante - versão simplificada"""
    return """
    <style>
    /* Reset e configurações gerais */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Melhor estilo para containers */
    .element-container div[data-testid="stVerticalBlock"] > div[style*="border"] {
        background: linear-gradient(135deg, #ffffff, #f8fafc);
        border: 2px solid #e2e8f0;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .element-container div[data-testid="stVerticalBlock"] > div[style*="border"]:hover {
        box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.15);
        transform: translateY(-3px);
    }
    
    /* Melhor estilo para dataframes */
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border: 1px solid #e2e8f0;
    }
    
    .stDataFrame thead th {
        background: linear-gradient(135deg, #1e3a8a, #3b82f6);
        color: white;
        font-weight: 600;
        padding: 1rem;
        border: none;
    }
    
    .stDataFrame tbody tr:nth-child(even) {
        background: #f8fafc;
    }
    
    .stDataFrame tbody tr:hover {
        background: #e2e8f0;
        transition: background-color 0.2s ease;
    }
    
    /* Estilo para gráficos */
    .stPlotlyChart, .stLineChart, .stBarChart {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border: 1px solid #e2e8f0;
    }
    
    /* Melhor estilo para selectbox e inputs */
    .stSelectbox > div > div {
        background: white;
        border: 2px solid #e2e8f0;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #3b82f6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
    }
    
    .stNumberInput > div > div > input {
        background: white;
        border: 2px solid #e2e8f0;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
    }
    
    .stDateInput > div > div > div > input {
        background: white;
        border: 2px solid #e2e8f0;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .stDateInput > div > div > div > input:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
    }
    
    /* Tabs modernas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: #f1f5f9;
        padding: 4px;
        border-radius: 12px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 8px;
        color: #64748b;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: white;
        color: #1e3a8a;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Melhor estilo para file uploader */
    .stFileUploader > div {
        background: linear-gradient(135deg, #ffffff, #f8fafc);
        border: 2px dashed #3b82f6;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stFileUploader > div:hover {
        background: linear-gradient(135deg, #f8fafc, #e2e8f0);
        border-color: #1e3a8a;
        transform: translateY(-2px);
    }
    
    /* Info boxes mais elegantes */
    .stInfo {
        background: linear-gradient(135deg, #dbeafe, #bfdbfe);
        border: 1px solid #3b82f6;
        border-radius: 12px;
        padding: 1rem;
        color: #1e3a8a;
    }
    
    .stSuccess {
        background: linear-gradient(135deg, #dcfce7, #bbf7d0);
        border: 1px solid #22c55e;
        border-radius: 12px;
        padding: 1rem;
        color: #166534;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #fef3c7, #fde68a);
        border: 1px solid #f59e0b;
        border-radius: 12px;
        padding: 1rem;
        color: #92400e;
    }
    
    .stError {
        background: linear-gradient(135deg, #fee2e2, #fecaca);
        border: 1px solid #ef4444;
        border-radius: 12px;
        padding: 1rem;
        color: #991b1b;
    }
    
    /* Scrollbar personalizada */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f5f9;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #cbd5e1, #94a3b8);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #94a3b8, #64748b);
    }
    
    /* Remove padding padrão */
    .main .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
    </style>
    """


def get_custom_header():
    """Retorna HTML para um cabeçalho customizado elegante"""
    return """
    <div style="
        background: linear-gradient(135deg, #1e3a8a, #3b82f6, #6366f1);
        padding: 2rem;
        border-radius: 20px;
        margin: -2rem -1rem 2rem -1rem;
        text-align: center;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.2);
    ">
        <h1 style="
            color: white;
            margin: 0;
            font-size: 2.5rem;
            font-weight: 700;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
        ">💰 Finanças Pessoais</h1>
        <p style="
            color: #e2e8f0;
            margin: 0.5rem 0 0 0;
            font-size: 1.1rem;
            font-weight: 400;
        ">Seu painel de controle financeiro inteligente</p>
    </div>
    """
