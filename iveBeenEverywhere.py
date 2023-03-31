cases = int(input())

for i in range(cases):
    visits = int(input())
    cities = []
    for i in range(visits):
        city = input()
        if city not in cities:
            cities.append(city)
    print(len(cities))
