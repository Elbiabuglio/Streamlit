"""
Templates HTML extraídos do main.py
"""

def get_calendar_html_template():
    """Template HTML do calendário que estava no main.py"""
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

def get_footer_html():
    """HTML do rodapé que estava no main.py"""
    return """
<div style='text-align: center; color: #666; padding: 20px;'>
    📱 <strong>Dica:</strong> Use o calendário para visualizar informações específicas de cada mês!<br>
    💡 Para melhores resultados, mantenha seus dados financeiros sempre atualizados.
</div>
"""
