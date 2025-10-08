import re

with open('pazzl.html', 'r', encoding='utf-8') as file:
    content = file.read()

pattern = r'<img[^>]+>'
images = re.findall(pattern, content)

print(f'Количество HTML-кодов изображений: {len(images)}')