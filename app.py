import os

restaurantes = [{'nome': 'Outback','categoria':'Diversos','ativo':False},
                {'nome': 'Dominos','categoria':'Pizza','ativo':True},
                {'nome': 'SushiNight','categoria':'Sushi','ativo':False}
                
                
                ]

def exibir_nome_do_programa():
    print('Sabor express \n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()
    
def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite o nome da categoria do restaurante do {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso \n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f' - {nome_restaurante} | {categoria_restaurante} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurente = input('Dgite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurente == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurente} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()    
    
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()