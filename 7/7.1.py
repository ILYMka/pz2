s = input().strip()
if s.count('.') == 1 and s.replace('.', '').isdigit():
    print(2)
elif s.isdigit() or (s[0] == '-' and s[1:].isdigit()):
    print(1)
else:
    print(0)