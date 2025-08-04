"""
CSS extraído do main.py - Calendário
"""


def get_calendar_css():
    """Retorna o CSS moderno e elegante do calendário"""
    return """
    <style>
    .calendar-container {
        background: linear-gradient(135deg, #ffffff, #f8fafc);
        border: 2px solid #e2e8f0;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.1);
        margin: 1.5rem 0;
        max-width: 700px;
        margin: 1.5rem auto;
        transition: all 0.3s ease;
    }
    
    .calendar-container:hover {
        box-shadow: 0 25px 50px -10px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }
    
    .calendar-header {
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 700;
        font-size: 1.8rem;
        background: linear-gradient(135deg, #1e3a8a, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .weekday-header {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 4px;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #1e3a8a, #3b82f6);
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .weekday-name {
        text-align: center;
        font-weight: 600;
        color: white;
        font-size: 0.9rem;
        padding: 0.5rem;
        border-radius: 6px;
        background: rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .weekday-name:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: scale(1.05);
    }
    
    .calendar-grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 4px;
        border: 2px solid #e2e8f0;
        border-radius: 12px;
        padding: 1rem;
        background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    }
    
    .calendar-day {
        aspect-ratio: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 2px solid #e2e8f0;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
        background: white;
        font-weight: 600;
        min-height: 45px;
        color: #374151;
        position: relative;
        overflow: hidden;
    }
    
    .calendar-day::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.1), transparent);
        transition: left 0.5s ease;
    }
    
    .calendar-day:hover {
        background: linear-gradient(135deg, #dbeafe, #bfdbfe);
        border-color: #3b82f6;
        transform: scale(1.08);
        box-shadow: 0 8px 15px -3px rgba(59, 130, 246, 0.2);
        color: #1e3a8a;
    }
    
    .calendar-day:hover::before {
        left: 100%;
    }
    
    .calendar-day.selected {
        background: linear-gradient(135deg, #3b82f6, #1e3a8a);
        color: white;
        border-color: #1e3a8a;
        box-shadow: 0 10px 25px -5px rgba(59, 130, 246, 0.4);
        transform: scale(1.1);
    }
    
    .calendar-day.today {
        background: linear-gradient(135deg, #f59e0b, #d97706);
        color: white;
        border-color: #d97706;
        font-weight: 700;
        box-shadow: 0 10px 25px -5px rgba(245, 158, 11, 0.4);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 10px 25px -5px rgba(245, 158, 11, 0.4); }
        50% { box-shadow: 0 10px 25px -5px rgba(245, 158, 11, 0.6); }
        100% { box-shadow: 0 10px 25px -5px rgba(245, 158, 11, 0.4); }
    }
    
    .calendar-day.other-month {
        color: #9ca3af;
        background: #f9fafb;
        border-color: #f3f4f6;
        opacity: 0.6;
    }
    
    .calendar-day.other-month:hover {
        opacity: 0.8;
        background: #f3f4f6;
        transform: scale(1.02);
    }
    
    /* Responsividade */
    @media (max-width: 768px) {
        .calendar-container {
            padding: 1rem;
            margin: 1rem 0;
        }
        
        .calendar-header {
            font-size: 1.4rem;
            margin-bottom: 1rem;
        }
        
        .calendar-day {
            min-height: 35px;
            font-size: 0.9rem;
        }
        
        .weekday-name {
            font-size: 0.8rem;
            padding: 0.3rem;
        }
    }
    </style>
    """
