#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste de importação do Plotly
"""

try:
    import plotly.express as px
    import plotly.graph_objects as go
    print("✅ SUCCESS: Plotly importado com sucesso!")
    print(f"Versão do Plotly: {px.__version__}")
    PLOTLY_AVAILABLE = True
except ImportError as e:
    print(f"❌ ERROR: Erro ao importar Plotly: {e}")
    PLOTLY_AVAILABLE = False

print(f"PLOTLY_AVAILABLE = {PLOTLY_AVAILABLE}")
