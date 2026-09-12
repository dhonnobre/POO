import mysql.connector
from modelos import Aluno, Plano, Instrutor
from crud  import GerenciadorAluno, GerenciadorPlano, GerenciadorInstrutor

conexao = mysql.connector.connect( #Criando a conexão com o banco de dados
    host='localhost',
    user='root',
    password='Mned2003@',
    database='bdacademia',
)
#Gerenciadores
ger_aluno = GerenciadorAluno(conexao)
ger_plano = GerenciadorPlano(conexao)
ger_instrutor = GerenciadorInstrutor(conexao)
#Menu principal
while True:
    print("-" * 30)
    print("Menu principal")
    print("-" * 30)
    print("Escolha uma opção em que voçê quer gerenciar")
    print("""
    1- Alunos
    2- Instrutores
    3- Planos
    0- Sair            
    """)
    print("-" * 30)
    opcao = input()
    match opcao:
        case "1": #Gerenciador de Alunos
            while True:
                print("-" * 30)
                print("Escolha uma opção!")
                print("""
                1- Adicionar
                2- Listar
                3- Remover
                4- Altualizar
                5- Contratar Personal    
                0- Sair            
                """)
                op = input()
                match op:
                    case "1": #Adicionando aluno
                        nome = input("Digite o nome do aluno que deseja adicionar!").strip() #Strip nesse caso foi utlizado para retirar espaços em branco
                        if not nome: #validação para 'nome' pois não pode ser vazio
                            print("Erro: nome não pode ser vazio!")
                            continue
                        cpf = input("Digite o CPF do aluno!").strip()
                        if not cpf.isdigit() or len(cpf) != 11: #isdigit() é utlizado para garantir que esta passando somente numeros e len(cpf) para contar quantos numeros tem no CPF
                            print("Erro: CPF inválido Digite 11 números sem pontos ou traços.")
                            continue
                        email = input("Digite o E-mail do aluno!").strip()
                        if "@" not in email or "." not in email: #Validação de E-mail, onde não poderá criar um E-mail sem '@' e '.' e obviamente não pode ser vazio
                            print("Erro: E-mail invalido!")
                            continue
                        telefone = input("Digite o Telefone do aluno!").strip()
                        if not telefone.isdigit() or len(telefone) not in [10, 11]: #validação testando se tudo são numeros e se o tamanho é 10 ou 11
                            print("Erro: telefone invalido, Digite 10 ou 11 números.")
                            continue
                        print("Escolha um plano:")
                        ger_plano.listando() #Como um novo aluno precisa escolher um plano, coloquei para listar todos os planos e escolher um plano
                        id_plano = input("Digite o id do plano que você quer!").strip()
                        if not id_plano.isdigit():
                            print("Erro: ID inválido!")
                            continue
                        id_plano = int(id_plano) #transfomando o id_plano em um INT
                        aluno = Aluno(nome, cpf, email, telefone, id_plano) #Encapsulando o nome, cpf, email, telefone, id_plano dentro da classe Aluno de modelos.py
                        ger_aluno.adicionando(aluno) #Enviando aluno para a função de adicionar alunos
                        print("Aluno adicionado!")
                    case "2": #Listando alunos
                        ger_aluno.listando() 
                    case "3": #Excluir aluno
                        if not ger_aluno.verificando(): #verifica se á algum aluno cadastrado
                            print("Nenhum aluno cadastrado!")
                            continue
                        name = input("Digite o nome do aluno que você deseja excluir!")
                        if not ger_aluno.buscando(name): #Busca no banco de dados se esse aluno existe no banco de dados
                            print(f"Aluno '{name}' não encontrado!")
                            continue
                        ger_aluno.limpando(name) #Função para Excluir um aluno
                        print("Aluno excluido!")
                    case "4": #Alterar aluno
                        if not ger_aluno.verificando():  
                            print("Nenhum aluno cadastrado para alterar!")
                            continue
                        campos_validos = { #Dicionario de campos validos, siginifica que cada numero retorna uma palavra diferente, nas quais foram especificadas
                            "1": "nome_aluno",
                            "2": "email_aluno",
                            "3": "telefone_aluno",
                            "4": "cpf_aluno"
                        }
                        nome = input("Digite o nome do aluno que deseja alterar") #Escolher o aluno que você queira alterar
                        if not ger_aluno.buscando(nome):  
                            print(f"Aluno '{nome}' não encontrado!")
                            continue
                        print("""
                        1 - Nome
                        2 - Email
                        3 - Telefone
                        4 - CPF
                        """)
                        opcao = input("Escolha o campo: ") #Escolher qual campo deseja alterar
                        if opcao in campos_validos: #Validação para que a opção escolhida
                            campo = campos_validos[opcao]
                            valor_alterado = input("Digite o novo valor: ") #Escolher o novo valor do campo
                            print(f"Alterando {campo} do aluno {nome}")
                            ger_aluno.alterando(nome, campo, valor_alterado) #Selecionado cada valor atribuido, o campo é alterado
                        else:
                            print("Opção invalida")
                    case "5": #Opção para um aluno "Contratar um personal", vale ressaltar que quando você adiciona um aluno apesar de não pedir um personal, o id_personal é criado
                        nome_aluno = input("Digite o nome do aluno: ").strip()
                        if not nome_aluno:
                            print("Erro: nome não pode ser vazio!")
                            continue
                        if not ger_aluno.buscando(nome_aluno):  
                            print(f"Aluno '{nome_aluno}' não encontrado!")
                            continue
                        print("Instrutores disponiveis: ")
                        ger_instrutor.listando() #Listando os instrutores/Personais
                        id_instrutor = input("Digite o ID do Instrutor: ")
                        if not id_instrutor.isdigit():
                            print("Erro: ID inválido!")
                            continue
                        id_instrutor = int(id_instrutor)
                        ger_aluno.alterando(nome_aluno, "id_instrutor", id_instrutor)
                        print("Personal contratado!")
                    case "0":
                        break
                    case _:
                       print("Opção invalida!") 
        case "2": #Gerenciar Instrutores/personais
            while True:
                print("-" * 30)
                print("Escolha uma opção!")
                print("""
                1- Adicionar
                2- Listar
                3- Remover
                4- Altualizar      
                0- Sair            
                """)
                op = input()
                match op:
                    case "1": #Adicionando os devidos campos necessadio para criar um instrutor e com as suas devidas validações. Como são codigos quase identicos ao do gen_aluno não irei comentar
                        nome = input("Digite o nome do Instrutor que deseja adicionar!").strip()
                        if not nome:
                            print("Erro: nome não pode ser vazio!")
                            continue
                        cpf = input("Digite o CPF do Instrutor!").strip()
                        if not cpf.isdigit() or len(cpf) != 11:
                            print("Erro: CPF inválido Digite 11 números sem pontos ou traços.")
                            continue
                        email = input("Digite o E-mail do Instrutor!").strip()
                        if "@" not in email or "." not in email:
                            print("Erro: E-mail invalido!")
                            continue
                        telefone = input("Digite o Telefone do Instrutor!").strip()
                        if not telefone.isdigit() or len(telefone) not in [10, 11]:
                            print("Erro: telefone invalido, Digite 10 ou 11 números.")
                            continue
                        instrutor = Instrutor(nome, cpf, email, telefone)
                        ger_instrutor.adicionando(instrutor)
                        print("Instrutor adicionado!")
                    case "2": #Listando Instrutores
                        ger_instrutor.listando()
                    case "3": #Removendo um Instrutor especifico
                        if not ger_instrutor.verificando():
                            print("Nenhum instrutor cadastrado!")
                            continue
                        name = input("Digite o nome do Instrutor que você deseja excluir!").strip()
                        if not ger_instrutor.buscando(name):  
                            print(f"Instrutor '{name}' não encontrado!")
                            continue
                        ger_instrutor.limpando(name)
                        print("Instrutor excluido!")
                    case "4": #alterando um Instrutor 
                        if not ger_instrutor.verificando():  
                            print("Nenhum instrutor cadastrado para alterar!")
                            continue
                        campos_validos = {
                            "1": "nome_instrutor",
                            "2": "cpf_instrutor",
                            "3": "email_instrutor",
                            "4": "telefone_instrutor"
                        }
                        nome = input("Digite o nome do Instrutor que deseja alterar")
                        if not ger_instrutor.buscando(nome):
                            print(f"Instrutor '{nome}' não encontrado!")
                            continue
                        print("""
                        1 - Nome
                        2 - Email
                        3 - CPF      
                        4 - Telefone
                        """)
                        opcao = input("Escolha o campo: ")
                        if opcao in campos_validos:
                            campo = campos_validos[opcao]
                            valor_alterado = input("Digite o novo valor: ")
                            print(f"Alterando {campo} do instrutor {nome}")
                            ger_instrutor.alterando(nome, campo, valor_alterado)
                        else:
                            print("Opção invalida")
                    case "0":
                        break
                    case _:
                       print("Opção invalida!") 
        case "3": #Gerenciador de Planos, novamente, como são bem parecidos, não repetir o que ja comentei/expliquei
            while True:
                print("-" * 30)
                print("Escolha uma opção!")
                print("""
                1- Adicionar
                2- Listar
                3- Remover
                4- Altualizar      
                0- Sair            
                """)
                op = input()
                match op:
                    case "1": #Adicionado um plano
                        nome = input("Digite o nome do Plano que deseja adicionar!").strip()
                        if not nome:
                            print("Erro: nome não pode ser vazio!")
                            continue
                        preco = input("Digite o preço: ").strip().replace(",", ".") #Replace para conseguir formatar do jeito certo de float e não dar erro(trocando a ',' por '.')
                        if not preco.replace(".", ""):
                            print("Erro: preço inválido!")
                            continue
                         
                        vantagens = input("Digite a vantagens!").strip()
                        desvantagens = input("Digite a desvantagens!").strip()
                        plano = Plano(nome, preco, vantagens, desvantagens) 
                        ger_plano.adicionando(plano)
                        print("Plano adicionado!")
                    case "2": #Listando os planos
                        ger_plano.listando()
                    case "3": #Excluir um plano
                        if not ger_plano.verificando():
                            print("Nenhum plano cadastrado!")
                            continue
                        name = input("Digite o nome do Plano que você deseja excluir: ")
                        if not ger_plano.buscando(name):  
                            print(f"Plano '{name}' não encontrado!")
                            continue
                        ger_plano.limpando(name)
                        print("Plano excluido!")
                    case "4": #Alterando um plano
                        if not ger_plano.verificando():  
                            print("Nenhum plano cadastrado para alterar!")
                            continue
                        campos_validos = {
                            "1": "nome_plano",
                            "2": "preco_plano",
                            "3": "vantagens",
                            "4": "desvantagens",
                        }
                        nome = input("Digite o nome do Plano que deseja alterar: ")
                        if not ger_plano.buscando(nome):
                            print(f"Plano '{nome}' não encontrado!")
                            continue
                        print("""
                        1 - Nome
                        2 - Preço
                        3 - Vantagens     
                        4 - Desvantagens
                        """)
                        opcao = input("Escolha o campo: ")
                        if opcao in campos_validos:
                            campo = campos_validos[opcao]
                            valor_alterado = input("Digite o novo valor: ")
                            print(f"Alterando {campo} do plano {nome}")
                            ger_plano.alterando(nome, campo, valor_alterado)
                        else:
                            print("Opção invalida")
                    case "0":
                        break
                    case _:
                       print("Opção invalida!")
        case "0":
            break
        case _:
            print("Opção invalida!")
conexao.close() #Necessario para encerrar a conexão com o banco de dados