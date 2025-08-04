"""
CSS extraído do main.py - Calendário
"""


def get_calendar_css():
    """Retorna o CSS do calendário que estava no main.py"""
    return """
    <style>
    .calendar-container {
        background: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 10px 0;
        max-width: 600px;
        margin: 0 auto;
    }
    .calendar-header {
        text-align: center;
        margin-bottom: 20px;
        font-weight: bold;
        font-size: 18px;
        color: #1976d2;
    }
    .weekday-header {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 2px;
        margin-bottom: 10px;
        background: #1976d2;
        border-radius: 8px;
        padding: 12px 8px;
    }
    .weekday-name {
        text-align: center;
        font-weight: bold;
        color: white;
        font-size: 14px;
        padding: 5px;
    }
    .calendar-grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 2px;
        border: 1px solid #e1e5e9;
        border-radius: 8px;
        padding: 8px;
        background: #f8f9fa;
    }
    .calendar-day {
        aspect-ratio: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid #e1e5e9;
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.2s;
        background: white;
        font-weight: 500;
        min-height: 40px;
    }
    .calendar-day:hover {
        background: #e3f2fd;
        border-color: #1976d2;
        transform: scale(1.05);
    }
    .calendar-day.selected {
        background: #1976d2;
        color: white;
        border-color: #1976d2;
    }
    .calendar-day.today {
        background: #ff9800;
        color: white;
        border-color: #f57c00;
        font-weight: bold;
    }
    .calendar-day.other-month {
        color: #bbb;
        background: #f5f5f5;
    }
    </style>
    """
