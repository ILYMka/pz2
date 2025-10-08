with open('file1.txt', 'w') as f:
    f.write('5 -3 10 -2 8')

with open('file1.txt') as f:
    data = list(map(int, f.read().split()))

n = data[-1]
result = [x * n for x in data[:-1]]

with open('result.txt', 'w') as f:
    f.write(f"Исходные данные: {data}\n")
    f.write(f"Количество элементов: {len(data)}\n")
    f.write(f"Сумма элементов: {sum(data)}\n")
    f.write(f"Элементы до n-1 умножены на элемент n: {result}\n")