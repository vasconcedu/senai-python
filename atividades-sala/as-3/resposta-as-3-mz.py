ovo1 = float(input("Digite o diametro do primeiro ovo (em cm): "))
ovo2 = float(input("Digite o diametro do segundo ovo (em cm): "))
ovo3 = float(input("Digite o diametro do terceiro ovo (em cm): "))

media = (ovo1 + ovo2 + ovo3) / 3

print("Media: {} cm".format(media))

if media > 3:
    print("Tipo extra grande")
else:
    print("Tipo medio")
