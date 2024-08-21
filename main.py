#funcoes
def mostrar_menu():
    print(' 1 - Somar.')
    print(' 2 - Subtrair.')
    print(' 3 - Dividir')
    print(' 4 - Multiplicar.')
    print(' 5 - Extrair o resto da divisão.')
    print(' 6 - Potênciação.')
    print(' Qualquer valor - Sair do Programa.')

#lambda
somar       = lambda x,y: x + y 
substrair   = lambda x,y: x - y
dividir     = lambda x,y: x / y
multiplicar = lambda x,y: x * y 
resto       = lambda x,y: x % y
potenciacao = lambda x,y: x ** y

#programa principal
#é possivel importar para outro arquivo o programa principal por isso precisa utilizar o comando do "if __name__ == '__main__':"  para que nao seja importado para outro lugar
#precisa criar auma protecao para o algoritmo principal do programa para impedir que seja importado para outros arquivos
#usa para que o programa nao seja importado para outro arquivo, questao de segurança
# o que esta dentro do if nao sera importado, o codigo "if __name__ == '__main__':" sempre vai ser esse, é padrao do python, nao esta relacionado ao nome do arquivo
if __name__ == '__main__':
    while True:
        mostrar_menu()
        try:
            opcao = int(input('Informe opção desejada: '))
            if opcao > 0 and opcao < 7:
                x = float(input('Informe o valor de x: ').replace(',','.'))
                y = float(input('Informe o valor de y: ').replace(',','.'))
                match opcao:
                    case 1:
                        print(f'A soma entre {x} e {y} é: {somar(x,y)}.')
                        continue
                    case 2:
                        print(f'A subtração entre {x} e {y} é: {substrair(x,y)}.')
                        continue
                    case 3:
                        print(f'A multiplicação entre {x} e {y} é: {multiplicar(x,y)}.')
                        continue
                    case 4:
                        print(f'A divisão entre {x} e {y} é: {dividir(x,y)}.')
                        continue
                    case 5:
                        print(f'O resto da divisão entre {x} e {y} é: {resto(x,y)}.')
                        continue
                    case 6:
                        print(f'{x} elevado a {y} é: {potenciacao(x,y)}.')
                        continue
                    case _:
                        print('Opção inválida!')
                        continue
            else:
                print('Programa encerrado.')
                break
        except:
            print('Não foi possível verificar a opção desejada.')
            break