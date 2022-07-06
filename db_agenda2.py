from db_agenda import *

class Menu:
    def __init__(self):
        agenda = DbAgenda()


        while True:
            entrada = input('1 - Novo Contato \n'
                            '2 - Listar Contato \n'
                            '3 - Alterar Telefone \n'
                            '4 - Alterar Nome  \n' 
                            '5 - Alterar Email \n'
                            '6 - Excluir \n'
                            '0 - Sair')
            if entrada =='1':
                cod = None
                nome = input('Entre com o nome: ')
                telefone = input('Entre com o telefone: ')
                email = input('Entre com o email: ')

                agenda.armazenar_contatos(cod, nome, telefone, email)
            elif entrada =='2':
                agenda.listar_contatos()
            elif entrada =='3':
                cod = int(input('Informe o código do contato: '))
                valor = input('Entre com o novo Nome: ')
                atributo = 'nome'
                agenda.alterar_contato(atributo, valor, cod)
            elif entrada =='4':
                cod = int(input('Informe o código do contato'))
                valor = input('Entre com o novo telefone: ')
                atributo = 'telefone'
                agenda.alterar_contato(atributo, valor, cod)
            elif entrada =='5':
                cod = int(input('Informe o código do contato: '))
                valor = input('Entre com o novo email: ')
                atributo = 'email'
                agenda.alterar_contato(atributo, valor, cod)
            elif entrada =='6':
                cod = int(input('Informe o código do contato: '))
                agenda.excluir_contato(cod)
            elif entrada =='0':
                break
            else:
                print('Opção inválida!')