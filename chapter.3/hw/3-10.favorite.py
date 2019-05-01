country = ['taiwan', 'japan', 'usa', 'turkey', 'egypt']
print(country)

country[0] = 'ice land'
print(country)

country.append('france')
print(country)

del country[3]
print(country)

popped_country = country.pop()
print(country)
print(popped_country)

born_in = country.pop(0)
print(country)
print(born_in)

country.remove('usa')
print(country)

country.append('spain')
country.append('cambodia')
country.append('roman')
print(country)

country.sort()
print(country)

country.sort(reverse=True)
print(country)

cars = ['yamaha', 'toyota', 'kawasaki', 'aprillia', 'ducati', 'bmw', 'suzuki']
print(cars)

print(sorted(cars))

print(cars)

cars.reverse()
print(cars)

print(len(cars))
