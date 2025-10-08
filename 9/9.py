avto = {
    'Toyota': ['Camry', 'Corolla', 'RAV4'],
    'BMW': ['X5', 'X3', 'X1'],
    'Audi': ['A4', 'A6', 'Q7']
}

print([avto[brand][1] for brand in avto])

for brand in avto:
    for model in avto[brand]:
        print(model)