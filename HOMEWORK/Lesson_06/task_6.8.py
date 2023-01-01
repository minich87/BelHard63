# Словарь: ключ - название стараны, значения - список городов,
# на вход поступает город, необходимо сказать из какой он страны.

def find_country(city):
    global countries
    for country, cities in countries.items():
        if city in cities:
            return country


countries = {
        'Belarus': ['Brest', 'Vitebsk', 'Gomel', 'Grodno', 'Minsk'],
        'Germany': ['Berlin', 'Bonn', 'Cologne', 'Drezden', 'Munich'],
        'France': ['Bordeuax', 'Nice', 'Lion', 'Marseilles', 'Paris'],
        'Great Britain': ['Edinburgh', 'London', 'Liverpool', 'Manchester', 'Newcastle'],
        'The USA': ['Boston', 'Chicago', 'Los Angeles', 'Miami', 'Washington']
        }

print(find_country('Paris'))
