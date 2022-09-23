text = input('Введите текст: ')
shift = int(input('Введите число сдвига: '))
ans = ' '
for letter in text:
    if letter != ' ':
        ans += " ".join(chr(ord(letter) + shift))
    else:
        ans += " ".join(' ')

print(ans)
