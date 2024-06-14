import random
import string

def generate_random_password(length=12):
    # Definiowanie zbioru znaków, z których będzie składać się hasło: litery i cyfry
    characters = string.ascii_letters + string.digits
    
    # Generowanie losowego hasła
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Przykładowe użycie funkcji
password = generate_random_password(12)  # Generowanie hasła o długości 12 znaków
print(f"Wygenerowane hasło: {password}")