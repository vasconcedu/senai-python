import streamlit as st
import datetime as dt
import json


########################################
# Ler e escrever estado da aplicação
########################################

# Ler arquivo de categorias de gastos (TXT)
def ler_categorias_gastos():
    with open("categorias_gastos.txt", "r") as arquivo_categorias:
        categorias_gastos = arquivo_categorias.read().splitlines()
        arquivo_categorias.close()
        return categorias_gastos

# Instancia uma data (utilizada pela funcao ler_gastos)
#   Isso eh necessario porque datetimes nao serializam, e 
#   consequentemente precisam ser serailizados como string e 
#   posteriormente reinstanciados 
def instanciar_data(string_data):
    return dt.datetime.strptime(string_data, "%Y-%m-%d").date()

# Ler arquivo de gastos cadastrados (JSON)
def ler_gastos():
    with open("gastos.json", "r") as arquivo_gastos:
        gastos = json.load(arquivo_gastos)
        for gasto in gastos:
            gasto["data"] = instanciar_data(gasto["data"])
        arquivo_gastos.close()
        return gastos

# Escrever arquivo de gastos cadastrados (JSON)
def escrever_gastos(gastos):
    arquivo_gastos = open("gastos.json", "w")
    arquivo_gastos.write(json.dumps(gastos, default=str))
    arquivo_gastos.close()


########################################
# Paginas da aplicacao
########################################

# Pagina de cadastro de novo gasto (item de menu "Cadastrar")
def novo_gasto():
    nome = ""
    valor = ""
    data = ""
    categoria = ""
    tipo = ""
    cadastrar = False 

    with st.container():
        st.header("Cadastrar")

        nome = st.text_input("Nome")

        # Organiza os campos de entrada do cadastro em duas colunas 
        cols = st.columns(2)
        valor = cols[0].number_input("Valor", min_value=0.0)
        data = cols[1].date_input("Data", format="DD/MM/YYYY", max_value = "today")

        cols = st.columns(2)
        categoria = cols[0].selectbox("Categoria", ler_categorias_gastos())
        tipo = cols[1].radio("Tipo", ["Variavel", "Fixo"])

        # Botao "Cadastrar"
        cadastrar = st.button("Cadastrar")
    
    # Testa se o usuario preencheu todos os campos necessarios do cadastro
    #   Se sim, efetua o cadastro do novo gasto
    #   Senao, avisa o usuario que tem um erro no preenchimento 
    if cadastrar:
        if (nome == ""):
            st.error("🚨 Gasto não cadastrado: preencha o nome do gasto")
        elif (valor == 0.0):
            st.error("🚨 Gasto não cadastrado: preencha o valor do gasto")
        else:
            gastos = ler_gastos()
            gastos.append({
                "nome": nome,
                "valor": valor,
                "data": data,
                "categoria": categoria,
                "tipo": tipo
            })
            escrever_gastos(gastos)
            st.success("✅ Gasto cadastrado com sucesso")

# Pagina de listagem de gastos cadastrados 
def listar():
    with st.container():
        st.header("Listar")

        gastos = ler_gastos()

        # Se nao tiver nenhum gasto cadastrado, nao listar nada e 
        #   avisar somente "Sem gastos a listar"
        if (len(gastos) == 0):
            st.write("Sem gastos a listar")

        # Para cada gasto, criar um expander com as informacoes dele 
        for gasto in gastos:
            with st.expander("{}: {}".format(gasto["data"].strftime("%d/%m/%y"), gasto["nome"])):
                cols = st.columns(3)
                with cols[0]:
                    st.write("Valor: {}".format(gasto["valor"]))
                with cols[1]:
                    st.write("Categoria: {}".format(gasto["categoria"]))
                with cols[2]:
                    st.write("Tipo: {}".format(gasto["tipo"]))

# Relatorio de gastos por data, com base em datas de inicio e fim
#   Esta funcao eh usada pela pagina de relatorio (funcao relatorio)
def datas(data_inicio, data_fim):
    total_data = {}

    data = data_inicio
    while data <= data_fim:
        total_data[data.strftime("%d/%m/%y")] = 0.0
        data += dt.timedelta(days=1)
    
    gastos = ler_gastos()
    for gasto in gastos:
        if gasto["data"] >= data_inicio and gasto["data"] <= data_fim:
            total_data[gasto["data"].strftime("%d/%m/%y")] += gasto["valor"]

    return total_data

# Relatorio de gastos por categoria, com base em datas de inicio e fim
#   Esta funcao eh usada pela pagina de relatorio (funcao relatorio)
def categorias(data_inicio, data_fim):
    total_categoria = {}

    for categoria_gasto in ler_categorias_gastos():
        total_categoria[categoria_gasto] = 0.0

    gastos = ler_gastos()
    for gasto in gastos:
        if gasto["data"] >= data_inicio and gasto["data"] <= data_fim:
            total_categoria[gasto["categoria"]] += gasto["valor"]

    return total_categoria

# Relatorio de gasto total, com base em datas de inicio e fim
#   Esta funcao eh usada pela pagina de relatorio (funcao relatorio)
def total(data_inicio, data_fim):
    total = 0.0

    gastos = ler_gastos()
    for gasto in gastos:
        if gasto["data"] >= data_inicio and gasto["data"] <= data_fim:
            total = total + gasto["valor"]

    return total

# Pagina de relatorio 
def relatorio():
    data_inicio = ""
    data_fim = ""
    gerar = False 

    with st.container():
        st.header("Relatório")

        # Selecao de datas de inicio e fim do relatorio 
        cols = st.columns(2)
        data_inicio = cols[0].date_input("Início", format="DD/MM/YYYY", max_value="today")
        data_fim = cols[1].date_input("Fim", format="DD/MM/YYYY", max_value="today")

        # Botao "Gerar"
        gerar = st.button("Gerar")

        # Testar se as datas fornecidas fazem sentido: a data de 
        #   inicio nao pode ser maior do que data de fim! 
        #   Se isso acontecer, avisar o usuario e nao gerar o relatorio
        #   Senao, gerar o relatorio normalmente 
        if (gerar == True):
            if (data_inicio > data_fim):
                st.error("🚨 Relatório não pode ser gerado: data de início posterior à data de fim")
            else:
                # Informacoes do periodo do relatorio (datas de inicio e fim)
                st.subheader("Período")
                st.write("Início: {}".format(data_inicio.strftime("%d/%m/%Y")))
                st.write("Fim: {}".format(data_fim.strftime("%d/%m/%Y")))

                # Gasto total do periodo 
                st.subheader("Total")
                st.write("{}".format(total(data_inicio, data_fim)))

                # Grafico de gasto por categoria no periodo 
                st.subheader("Categoria")
                total_categorias = categorias(data_inicio, data_fim)
                st.bar_chart(total_categorias)

                # Grafico de gasto por data no periodo 
                st.subheader("Data")
                total_datas = datas(data_inicio, data_fim)
                st.bar_chart(total_datas)

                # Reiniciar o estado do botao 
                gerar = False 


########################################
# Programa principal 
########################################

def main():
    # Menu lateral 
    st.sidebar.title("Gastos")
    opcao = st.sidebar.radio("Navegação", ["Cadastrar", "Listar", "Relatório"])

    # Mostrar pagina correspondente a opcao selecionada no menu lateral 
    if opcao == "Cadastrar":
        novo_gasto()
    elif opcao == "Listar":
        listar()
    elif opcao == "Relatório":
        relatorio()
    else: 
        novo_gasto()

# Chamada do programa principal 
main()
