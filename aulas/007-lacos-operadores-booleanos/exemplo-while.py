# Esse programa solicita uma entrada do usuario e
#   continua a solicitar entradas ate o usuario digitar "sair"

while(True):
    # Solicitar uma entrada do usuario
    entrada = input("Digite algo (ou 'sair' para sair): ")
    
    # Verificar se a entrada eh "sair"
    if entrada.lower() == "sair":
        print("OK, tchau!")
        break  # Sair do laco while
    
    # Mostrar a entrada do usuario
    print("{}? Huummm, muito interessante...".format(entrada))
