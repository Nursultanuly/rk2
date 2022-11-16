numbers = [1, 2, 3, 4, 5, 6, 7]
even_numbers_iterator = filter(lambda x: (x%2 == 0), numbers)
even_numbers = list(even_numbers_iterator)#Листқа айналдырады
print(even_numbers)