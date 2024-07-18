# Dictionary of lists: Mapping cities to their temperature
cities = {
    "New York": [32, 25, 30, 28, 35],
    "Los Angeles": [75, 68, 72, 70, 80],
    "Chicago": [20, 18, 22, 25, 15],
}

# Calculate average temperature for each city
averages = {city: sum(temps) / len(temps) for city, temps in cities.items()}
print("Average temperatures:", averages)
