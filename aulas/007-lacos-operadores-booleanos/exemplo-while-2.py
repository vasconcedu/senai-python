# Esse programa faz a mesma coisa usando o laco while,
#   mas com uma variavel de controle

sair = False

while not sair:
    # Solicitar uma entrada do usuario
    entrada = input("Digite algo (ou 'sair' para sair): ")
    
    # Verificar se a entrada eh "sair"
    if entrada.lower() == "sair":
        print("OK, tchau!")
        sair = True  # Sair do laco while
    
    if not sair:
        # Mostrar a entrada do usuario
        print("{}? Huummm, muito interessante...".format(entrada))
