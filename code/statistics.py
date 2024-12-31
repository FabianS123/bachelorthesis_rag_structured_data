import statistics
import math
import pandas as pd



# Median for Chunk_size, the questions that cannot contain chunks have been omitted
new_numbers = [
    3, 12, 22, 17, 8, 1, 23, 4, 28, 1, 1, 29, 28, 37, 5, 20, 7, 82, 17, 23, 4, 61,
    3, 4, 7, 4, 23, 5, 27, 17, 1, 2, 5, 6, 20, 11, 6, 6, 8, 8
]

# Calculate the median for the new data
new_median_value = statistics.median(new_numbers)
new_median_value


# mean, median, variance, and standard deviation for the given question categories
# given values for each category
categories = {
    "Existenzfragen": [100, 100, 100, 100, 100, 75],
    "Überblicksfragen": [100, 100],
    "Detailfragen": [100, 100, 100, 100, 100, 100, 100, 75, 33],
    "Interpretationsfragen": [100, 100, 100, 63, 63, 25, 75, 0, 13],
    "Synonymfragen": [25, 50, 67, 0, 43, 0],
    "Toleranzfragen": [0, 20, 38, 50, 100, 100, 40, 0]
}

# functions to calculate mean, median, variance, and standard deviation
def calculate_statistics(values):
    # mean
    mean = sum(values) / len(values)
    # median
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        median = sorted_values[mid]
    # Variance (n-1 for sample variance)
    variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    # Standardabweichung
    std_dev = math.sqrt(variance)
    return mean, median, variance, std_dev

# calculation of statistics for each category
statistics_results = {
    category: calculate_statistics(values) for category, values in categories.items()
}

# Darstellung der Ergebnisse als DataFrame
df_statistics = pd.DataFrame.from_dict(
    statistics_results,
    orient='index',
    columns=['Mittelwert (%)', 'Median (%)', 'Varianz (%)', 'Standardabweichung (%)']
)

print(df_statistics)




# values for additional question categories
categories_additional = {
    "Geschlossene Fragen": [100] * 9 + [75, 50, 40, 0, 0, 0, 25, 67],
    "Offene Fragen": [100] * 10 + [63, 63, 25, 75, 75, 0, 0, 13, 33, 20, 38, 50, 43]
}


# functions to calculate mean, median, variance, and standard deviation
def calculate_statistics_types(values):
    # mean
    mean = sum(values) / len(values)
    # median
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        median = sorted_values[mid]
    # Variance (n-1 for sample variance)
    variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    # Standardabweichung
    std_dev = math.sqrt(variance)
    return mean, median, variance, std_dev

# calculation of statistics for each category
statistics_additional_results = {
    category: calculate_statistics(values) for category, values in categories_additional.items()
}

# visualization of the results as a DataFrame
df_additional_statistics = pd.DataFrame.from_dict(
    statistics_additional_results,
    orient='index',
    columns=['Mittelwert (%)', 'Median (%)', 'Varianz (%)', 'Standardabweichung (%)']
)
print(df_additional_statistics)