from datetime import datetime

def days_until_end_of_year():
    # Pobieranie  daty
    today = datetime.today()
    
    # Ustalenie daty ostatniego dnia roku
    end_of_year = datetime(year=today.year, month=12, day=31)
    
    # Obliczanie różnicy między końcem roku a dzisiejszą datą
    remaining_days = (end_of_year - today).days
    
    return remaining_days

# Wywołanie funkcji i wyświetlenie wyniku
days_left = days_until_end_of_year()
print(f"Liczba dni pozostałych do końca roku: {days_left}")