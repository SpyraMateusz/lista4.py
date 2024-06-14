import os

def list_files_and_sizes(directory='.'):
    try:
        # Pobieranie listy plików i katalogów w podanym katalogu
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():  # Sprawdzanie czy entry jest plikiem
                    # Pobieranie rozmiaru pliku
                    size = entry.stat().st_size
                    # Wyświetlanie nazwy pliku i jego rozmiaru w bajtach
                    print(f'Nazwa pliku: {entry.name}, Rozmiar: {size} bajtów')
    except Exception as e:
        print(f'Wystąpił błąd: {e}')

# Wywołanie funkcji
list_files_and_sizes()