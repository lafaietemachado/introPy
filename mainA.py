# 1 - imports / bibliotecas

# 2 - Classe

# 3 - Métodos e Funções
# def = definition = definição
def print_hi(name):
    print(f'Oi, {name}')
    print('Oi, ' + name)

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_quadrado(lado):
    return lado ** 2
    # return lado * lado

def calcular_area_do_triangulo(largura, comprimento):
    return largura * comprimento / 2

def contagem_progressiva(fim):
    for numero in range(fim):
        print(numero)

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        #contador = numero + 1
        #print(f'{contador} - {nome}')

        if numero < 9:
            print(f'00{numero + 1} - {nome}')
        elif numero < 99:
            print(f'0{numero + 1} - {nome}')
        else:
            print(numero + 1, '-', nome)

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>3}'.format(numero))

def exibir_dia_da_semana_if(numero):
    print('Execução com IF')
    if numero == 1:
        print('O dia é Segunda')
    elif numero ==2:
        print('O dia é Terça')
    elif numero ==3:
        print('O dia é Quarta')
    elif numero ==4:
        print('O dia é Quinta')
    elif numero ==5:
        print('O dia é Sexta')
    elif numero ==6:
        print('O dia é Sábado')
    elif numero ==7:
        print('O dia é Domingo')
    else:
        print('Número de dia inválido. Digite um número de 1 a 7.')

def exibir_dia_da_semana_match(numero):
    print('Execução com MATCH')
    match numero:
        case 1:
            print('O dia é Segunda')
        case 2:
            print('O dia é Terça')
        case 3:
            print('O dia é Quarta')
        case 4:
            print('O dia é Quinta')
        case 5:
            print('O dia é Sexta')
        case 6:
            print('O dia é Sábado')
        case 7:
            print('O dia é Domingo')
        case _:
            print('Número de dia inválido. Digite um número de 1 a 7.')

def brincar_de_para_ou_continua():
    resposta = 'C'

    #while resposta == 'C' or resposta == 'c':
    while resposta.upper() == 'C':
        resposta = input('Digite C para continuar ou qualquer letra para parar')

    print('Você decidiu parar com a brincadeira')

# estrutura de identificação / execução do script
if __name__ == '__main__':
    print_hi('Lafaiete')

    # chamar a função de calculo do retangulo
    resultado = calcular_area_do_retangulo(3,4)
    print(f'A área do retângulo é de {resultado} m²')

    # chamar a função de calculo do quadrado
    resultado = calcular_area_do_quadrado(5)
    print(f'A área do quadrado é de {resultado} m²')

    # chamar a função de calculo do triangulo
    resultado = calcular_area_do_triangulo(6,7)
    print(f'A área do triângulo é de {resultado} m²')

    # executar uma contagem progressiva
    contagem_progressiva(10)

    # executar um apoiar candidato
    apoiar_candidato('Faker', 100)

    # executar brincar de Plim
    brincar_de_plim(100)

    # exemplo de dia da semana com IF - ELIF - ELSE
    exibir_dia_da_semana_if(9)

    # exemplo de dia da semana com match - case
    exibir_dia_da_semana_match(6)

    # exemplo com while - para ou continua
    brincar_de_para_ou_continua()