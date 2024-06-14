def calculate_mean_and_median(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty")
    
    # Obliczanie średniej
    mean = sum(numbers) / len(numbers)
    
    # Obliczanie mediany
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2
    
    if n % 2 == 0:
        # Jeśli liczba elementów jest parzysta, mediana to średnia z dwóch środkowych elementów
        median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        # Jeśli liczba elementów jest nieparzysta, mediana to środkowy element
        median = sorted_numbers[middle]
    
    return mean, median

# Przykładowe użycie funkcji
numbers = [1, 2, 3, 4, 5, 6, 7]
mean, median = calculate_mean_and_median(numbers)
print(f"Średnia: {mean}, Mediana: {median}")