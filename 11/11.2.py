with open('text18-19.txt') as f:
    text = f.read()

print(text)
print('Букв:', sum(c.isalpha() for c in text))

with open('new_text.txt', 'w') as f:
    f.write(text.lower())