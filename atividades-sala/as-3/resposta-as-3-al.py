goiaba1 = int(input("Digite o peso da primeira goiaba (em g): "))
goiaba2 = int(input("Digite o peso da segunda goiaba (em g): "))
goiaba3 = int(input("Digite o peso da terceira goiaba (em g): "))

media = (goiaba1 + goiaba2 + goiaba3) / 3

print("Media: {} g".format(media))

if media >= 300:
    print("Lote premium")
else:
    print("Lote comum")
