# Словарь: ключ - название стараны, значения - список городов,
# на вход поступает город, необходимо сказать из какой он страны.

city = input('Enter city: ').title()

country = {
        'Belarus': ['Brest', 'Vitebsk', 'Gomel', 'Grodno', 'Minsk'],
        'Germany': ['Berlin', 'Bonn', 'Cologne', 'Drezden', 'Munich'],
        'France': ['Bordeuax', 'Nice', 'Lion', 'Marseilles', 'Paris'],
        'Great Britain': ['Edinburgh', 'London', 'Liverpool', 'Manchester', 'Newcastle'],
        'The USA': ['Boston', 'Chicago', 'Los Angeles', 'Miami', 'Washington']
        }

for key, val in country.items():
    for el in val:
        if el == city:
            print(key)
