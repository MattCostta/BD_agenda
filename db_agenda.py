import mysql.connector
from classe_contato import Contato

class DbAgenda:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host= 'localhost',
            user='root',
            password='q1w2e3',
            database='agenda'
        )
        self.meu_cursor = self.conexao.cursor()


    def armazenar_contatos(self, cod, nome, telefone, email):
        objcontato = Contato(cod, nome, telefone, email)
        comando_sql = f'insert into Contatos (nome, telefone, email) value ("{objcontato.nome}","{objcontato.telefone}","{objcontato.email}")'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def listar_contatos(self):
        comando_sql = 'select * from Contatos'
        self.meu_cursor.execute(comando_sql)
        lista = self.meu_cursor.fetchall()
        for i in lista:
            print(i)

    def alterar_contato(self, atributo, valor, cod):
        comando_sql =f'update Contatos set {atributo} = "{valor}" where id = {cod}'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()

    def excluir_contato(self, cod):
        comando_sql = f'delete from Contatos where id = "{cod}"'
        self.meu_cursor.execute(comando_sql)
        self.conexao.commit()