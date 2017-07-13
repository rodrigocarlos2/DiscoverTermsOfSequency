
sequency = input('Write the complet sequency: ')

sequency = str(sequency)

lenght = len(sequency)

term = input('Write the secret term: ')

term = int(term)

position = term % lenght

print(sequency[position-1])
