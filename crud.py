from modelos import Aluno, Plano, Instrutor
from abc import ABC, abstractmethod

class Gerenciador(ABC): #Classe mãe com metodos abstratos para herdar as classes filhas
    def __init__(self, conexao): 
        self.conexao = conexao # armazena a conexão com o banco
        self.cursor = conexao.cursor() # cursor executa os comandos SQL, necessario para todos gerenciadores
    #CRUD padrão obrigatorio para todos os Gerenciadores
    @abstractmethod
    def adicionando(self):
        pass
    @abstractmethod
    def listando(self):
        pass
    @abstractmethod
    def limpando(self):
        pass
    @abstractmethod
    def alterando(self):
        pass

    def verificando(self, tabela, coluna_nome): #Verificador para testar se tem campos cadastrados, nos poderiamos ter criado todos esses metodos aqui dessa mesma forma, mas pensamos em fazer dessa forma só quando o projeto ja estava pronto. pouparia muitas linhas de codigo kkkk
        self.cursor.execute(f'SELECT COUNT(*) FROM {tabela}')
        quantidade = self.cursor.fetchone()[0]
        return quantidade > 0
    
    def buscando(self, tabela, coluna_nome, nome): #Buscador ele testa se o campo requisitado existe, novamente se tivessimos usado dessa forma com todos os metodos seria muito menor o codigo.
        self.cursor.execute(f'SELECT * FROM {tabela} WHERE {coluna_nome} = %s', (nome,))
        return self.cursor.fetchone()

class GerenciadorAluno(Gerenciador):
    def __init__(self, conexao):
        super().__init__(conexao) #Cursor
    def adicionando(self, aluno):
        comando = 'INSERT INTO aluno (nome_aluno, cpf_aluno, email_aluno, telefone_aluno, id_plano, id_instrutor) VALUES (%s, %s, %s, %s, %s, %s)' #comando em que é executado no Cursor
        valores = (aluno.nome, aluno.cpf, aluno.email, aluno.telefone, aluno.id_plano, aluno.id_instrutor) #valores encapsulados em Alunos que esta em modelos.py e puxado no menu)
        self.cursor.execute(comando, valores) #Executador do cursor
        self.conexao.commit() #Necessario para editar/salvar o comando no banco de dados
    def listando(self):
        comando = 'SELECT * FROM aluno'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall() # ler o banco de dados
        if not resultado:
            print("Nenhum aluno cadastrado")
            return
        for aluno in resultado:
            obj = Aluno(aluno[1],  aluno[2], aluno[3], aluno[4], aluno[5], aluno[6]) #Encapsulamento de um objeto em Alunos para exibir os dados
            print(obj)
    def limpando(self, nome_aluno):
        comando = 'DELETE FROM aluno WHERE nome_aluno = %s'
        self.cursor.execute(comando, (nome_aluno,))
        self.conexao.commit()
    def alterando(self, nome, campo, valor_alterado):
        comando = f'UPDATE aluno SET {campo} = %s WHERE nome_aluno = %s' #Apesar de perigoso, utlizar o 'f' não ocasionou erros
        self.cursor.execute(comando, (valor_alterado, nome))
        self.conexao.commit()
    
    def verificando(self):
        return super().verificando('aluno', 'nome_aluno') #Puxando o metodo verificando ja pronto da super classe gerenciador
    
    def buscando(self, nome):
        return super().buscando('aluno', 'nome_aluno', nome) #Puxando o metodo buscando ja pronto da super classe gerenciador


class GerenciadorInstrutor(Gerenciador):
    def __init__(self, conexao):
        super().__init__(conexao)
    def adicionando(self, instrutor):
        comando = 'INSERT INTO instrutor (nome_instrutor, cpf_instrutor ,email_instrutor, telefone_instrutor) VALUES (%s, %s, %s, %s)'
        valores = (instrutor.nome, instrutor.cpf, instrutor.email, instrutor.telefone)
        self.cursor.execute(comando, valores)
        self.conexao.commit()
    def listando(self):
        comando = 'SELECT * FROM instrutor'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall() # ler o banco de dados
        if not resultado:
            print("Nenhum Instrutor encontrado!")
            return
        for instrutor in resultado:
            obj = Instrutor(instrutor[1], instrutor[2], instrutor[3], instrutor[4])
            print(obj)
    
    def limpando(self, nome_instrutor):
        comando = 'DELETE FROM instrutor WHERE nome_instrutor = %s'
        self.cursor.execute(comando, (nome_instrutor,))
        self.conexao.commit() #edita o banco de dados
    def alterando(self, nome, campo, valor_alterado):
        comando = f'UPDATE instrutor SET {campo} = %s WHERE nome_instrutor = %s'
        self.cursor.execute(comando, (valor_alterado, nome))
        self.conexao.commit()
    def verificando(self):
        return super().verificando('instrutor', 'nome_instrutor')
    
    def buscando(self, nome):
        return super().buscando('instrutor', 'nome_instrutor', nome)

class GerenciadorPlano(Gerenciador):
    def __init__(self, conexao):
        super().__init__(conexao)
    def adicionando(self, plano):
        comando = 'INSERT INTO plano (nome_plano,  preco_plano, vantagens, desvantagens) VALUES (%s, %s, %s, %s)'
        valores = (plano.nome, plano.preco, plano.vantagens, plano.desvantagens)
        self.cursor.execute(comando, valores)
        self.conexao.commit()
    def listando(self):
        comando = 'SELECT * FROM plano'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall() # ler o banco de dados
        if not resultado:
            print("Nenhum Plano encontrado!")
            return
        for plano in resultado:
            obj = Plano(plano[1], plano[2], plano[3], plano[4])
            print(obj)
    def limpando(self, nome_plano):
        comando = 'DELETE FROM plano WHERE nome_plano = %s'
        self.cursor.execute(comando, (nome_plano,))
        self.conexao.commit() #edita o banco de dados
    def alterando(self, nome, campo, valor_alterado):
        comando = f'UPDATE plano SET {campo} = %s WHERE nome_plano = %s'
        self.cursor.execute(comando, (valor_alterado, nome))
        self.conexao.commit()
    
    def verificando(self):
        return super().verificando('plano', 'nome_plano')

    def buscando(self, nome):
        return super().buscando('plano', 'nome_plano', nome)