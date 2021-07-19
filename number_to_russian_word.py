import re

with open("russian.txt", "r") as f:
    words = list(map(lambda x: x[:-1], f.readlines()))

# Digit-Letter Code
DLC = {
        '0' : '[нм]',
        '1' : '[гж]',
        '2' : '[дт]',
        '3' : '[кх]',
        '4' : '[чщ]',
        '5' : '[пб]',
        '6' : '[шл]',
        '7' : '[сз]',
        '8' : '[вф]',
        '9' : '[рц]',
        }

# Separators
sep = "[аеёийоуьыъэюя]*"

while True:
    print("Input number: ", end='')

    number = list(map(lambda x: DLC[x], input()))
    regex = sep + f"{sep}".join(number) + sep

    for word in words:
        x = re.fullmatch(regex, word)
        if x: print(x.group())

    print()
