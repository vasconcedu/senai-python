# Exemplo de uso do laco for 
# Esse programa mostra na tela os numeros de 1 a 10
# Especificamente, se o numero for 5 ou 7, ele mostra uma mensagem especial 
for numero in range(1, 11):
    # Mostrar na tela o numero atual 
    print("numero: {}".format(numero))
    
    # Ver se o numero eh 5
    if numero == 5 or numero == 7:
        # Mostrar uma mensagem especial 
        print("Ouviram do Ipiranga as margens placidas")
