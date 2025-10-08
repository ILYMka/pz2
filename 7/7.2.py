words = input().split()
result = []
for word in words:
    if word:
        last_char = word[-1]
        new_word = ''.join('.' if i < len(word)-1 and ch == last_char else ch for i, ch in enumerate(word))
        result.append(new_word)
    else:
        result.append('')
print(' '.join(result))