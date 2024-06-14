def reverse_string(s):
    # Inicjalizacja pustego napisu dla wyniku
    reversed_s = ''
    
    # Iteracja przez napis od końca do początku
    for i in range(len(s) - 1, -1, -1):
        reversed_s += s[i]
    
    return reversed_s

# Przykładowe użycie funkcji
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(f"Odwrócony napis: {reversed_string}")