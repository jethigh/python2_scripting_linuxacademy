# Otawrcie pliku w trybie append
with open('tmp.txt', 'a') as tmp:
    text = raw_input('Podaj tekst, ktory zostanie dodany do pliku.')
    tmp.write(text + "\n")

# Wydukowanie calej zawartosci pliku
with open('tmp.txt') as tmp:
    print(tmp.read())

# Wydrukowani linia po lini (przecinek po print sprawia ze nie jest dodawana nowa linia przez print)
with open('tmp.txt', 'r') as tmp:
    for line in tmp:
        print(line),
    