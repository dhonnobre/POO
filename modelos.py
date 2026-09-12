from abc import ABC, abstractmethod

class Pessoa(ABC): #Classe mãe para usar como herança
    def __init__(self, nome, cpf, email, telefone): #Inicializador 
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

    @abstractmethod
    def __str__(self):#Metodo abstrato para Exibir dados
        pass

class Aluno(Pessoa): #Classe filha da herança
    def __init__(self, nome, cpf, email, telefone, id_plano, id_instrutor=None):
        super().__init__(nome, cpf, email, telefone)
        self.id_plano = id_plano
        self.id_instrutor = id_instrutor 
    def __str__(self): 
        instrutor = self.id_instrutor if self.id_instrutor else "Nenhum"
        return (f"\n        Nome:     {self.nome}"
                f"\n        CPF:      {self.cpf}"
                f"\n        E-mail:   {self.email}"
                f"\n        Telefone: {self.telefone}"
                f"\n        Plano ID: {self.id_plano}"
                f"\n        Instrutor ID: {instrutor}"
                f"\n        {'-' * 30}")
class Instrutor(Pessoa): #Classe filha da herança
    def __init__(self, nome, cpf, email, telefone):
        super().__init__(nome, cpf, email, telefone)
    def __str__(self):
        return (f"\n        Nome:          {self.nome}"
                f"\n        CPF:           {self.cpf}"
                f"\n        E-mail:        {self.email}"
                f"\n        Telefone:      {self.telefone}"
                f"\n        {'-' * 30}")
class Plano: #Classe plano
    def __init__(self, nome, preco, vantagens, desvantagens):
        self.nome = nome
        self.preco = preco
        self.vantagens = vantagens
        self.desvantagens = desvantagens

    def __str__(self):
        return (f"\n        Nome:         {self.nome}"
                f"\n        Preço:        R$ {self.preco}"
                f"\n        Vantagens:    {self.vantagens}"
                f"\n        Desvantagens: {self.desvantagens}"
                f"\n        {'-' * 30}")

