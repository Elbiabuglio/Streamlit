"""
Templates HTML extraídos do main.py - Versão elegante
"""

def get_calendar_html_template():
    """Template HTML moderno do calendário"""
    return """
    <div class="calendar-container">
        <div class="calendar-header">
            📅 {mes_nome} {ano}
        </div>
        <div class="weekday-header">
            {dias_semana_html}
        </div>
        <div class="calendar-grid">
            {dias_calendario_html}
        </div>
    </div>
    """

def get_weekday_html():
    """Template para dias da semana"""
    return '<div class="weekday-name">{dia}</div>'

def get_calendar_day_html():
    """Template para dia do calendário"""
    return '<div class="{classes}">{dia}</div>'

def get_welcome_section():
    """Template para seção de boas-vindas elegante"""
    return """
    <div style="
        background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
        border: 2px solid #0ea5e9;
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 10px 25px -5px rgba(14, 165, 233, 0.2);
    ">
        <h3 style="
            color: #0c4a6e;
            margin: 0 0 1rem 0;
            font-size: 1.5rem;
            font-weight: 700;
        ">✨ Bem-vindo ao seu painel de controle financeiro!</h3>
        
        <div style="
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 1.5rem;
        ">
            <div style="
                background: white;
                border-radius: 12px;
                padding: 1rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                transition: all 0.3s ease;
            ">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">📈</div>
                <div style="color: #0c4a6e; font-weight: 600;">Monitorar receitas</div>
            </div>
            
            <div style="
                background: white;
                border-radius: 12px;
                padding: 1rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                transition: all 0.3s ease;
            ">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">📉</div>
                <div style="color: #0c4a6e; font-weight: 600;">Controlar despesas</div>
            </div>
            
            <div style="
                background: white;
                border-radius: 12px;
                padding: 1rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                transition: all 0.3s ease;
            ">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🏦</div>
                <div style="color: #0c4a6e; font-weight: 600;">Gerenciar investimentos</div>
            </div>
            
            <div style="
                background: white;
                border-radius: 12px;
                padding: 1rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                transition: all 0.3s ease;
            ">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">📅</div>
                <div style="color: #0c4a6e; font-weight: 600;">Visualizar datas importantes</div>
            </div>
        </div>
        
        <p style="
            color: #0369a1;
            margin: 1.5rem 0 0 0;
            font-size: 1.1rem;
            font-style: italic;
        ">Organize sua vida financeira de forma simples e eficiente.</p>
    </div>
    """

def get_info_card(title, content, icon="💡", color="#3b82f6"):
    """Template para cards informativos elegantes - versão simplificada"""
    return f"""
<div style="
    background: linear-gradient(135deg, #ffffff, #f8fafc);
    border: 2px solid {color}33;
    border-radius: 16px;
    padding: 1.5rem;
    margin: 1rem 0;
    box-shadow: 0 8px 15px -3px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
">
    <div style="display: flex; align-items: center; margin-bottom: 0.75rem;">
        <span style="font-size: 1.5rem; margin-right: 0.75rem;">{icon}</span>
        <h4 style="color: {color}; margin: 0; font-size: 1.2rem; font-weight: 600;">{title}</h4>
    </div>
    <div style="color: #374151; line-height: 1.6; font-size: 1rem;">{content}</div>
</div>
"""

def get_metric_card(value, label, icon="📊", trend=None):
    """Template para cards de métricas elegantes"""
    trend_html = ""
    if trend:
        trend_color = "#22c55e" if trend > 0 else "#ef4444" if trend < 0 else "#64748b"
        trend_icon = "↗️" if trend > 0 else "↘️" if trend < 0 else "➡️"
        trend_html = f"""
        <div style="
            display: flex;
            align-items: center;
            margin-top: 0.5rem;
            color: {trend_color};
            font-size: 0.9rem;
            font-weight: 500;
        ">
            <span style="margin-right: 0.25rem;">{trend_icon}</span>
            {abs(trend):.1f}%
        </div>
        """
    
    return f"""
    <div style="
        background: linear-gradient(135deg, #ffffff, #f8fafc);
        border: 2px solid #e2e8f0;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 8px 15px -3px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        margin: 0.5rem;
    ">
        <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
        <div style="
            color: #1e3a8a;
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
        ">{value}</div>
        <div style="
            color: #64748b;
            font-size: 0.9rem;
            font-weight: 500;
        ">{label}</div>
        {trend_html}
    </div>
    """

def get_footer_html():
    """HTML do rodapé elegante e moderno"""
    return """
<div style="
    background: linear-gradient(135deg, #f8fafc, #e2e8f0);
    border: 2px solid #e2e8f0;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin-top: 3rem;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
">
    <div style="
        color: #1e3a8a;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 1rem;
    ">
        📱 <strong>Dica Inteligente:</strong> Use o calendário para visualizar informações específicas de cada mês!
    </div>
    <div style="
        color: #64748b;
        font-size: 1rem;
        line-height: 1.6;
    ">
        💡 Para melhores resultados, mantenha seus dados financeiros sempre atualizados.<br>
        📊 Monitore suas metas regularmente para alcançar seus objetivos financeiros.
    </div>
    <div style="
        margin-top: 1rem;
        padding-top: 1rem;
        border-top: 1px solid #cbd5e1;
        color: #94a3b8;
        font-size: 0.9rem;
    ">
        🚀 Desenvolvido com Streamlit | 💼 Gestão Financeira Inteligente
    </div>
</div>
"""
