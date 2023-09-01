# Thays Machado 09/09/2023
import random
while True:
    print("Sejam bem vindos ao jogo Pedra, papel, tesoura!")
    print("Você, jogador, terá que escolher alguma das opções: \n   1) Pedra 2) Papel 3) Tesoura")
    print("Há apenas três regras para os jogadores se atentarem e analisar quem ganhou/perdeu:")
    print("-Pedra perde para o papel (papel embrulha a pedra")
    print("-Papel perde para tesoura (tesoura corta o papel)")
    print("-Tesoura perde para a pedra (pedra quebra a tesoura")
    escolha = int(input("Vamos começar??? \n Escolha alguma das opções abaixo: \n 1) Pedra 2) Papel 3) Tesoura \n"))
    if 4 > escolha > 0:
        print("A sua escolha foi:", escolha)
        escolha_computador = random.randint(1, 3)
        print("A escolha do computador foi:", escolha_computador)
        if escolha == 1 and escolha_computador == 2:
            print("Computador venceu!")
        if escolha == 1 and escolha_computador == 3:
            print("Você venceu!")
        if escolha == 2 and escolha_computador == 1:
            print("Você venceu!")
        if escolha == 2 and escolha_computador == 3:
            print("Computador venceu!")
        if escolha == 3 and escolha_computador == 1:
            print("Computador venceu!")
        if escolha == 3 and escolha_computador == 2:
            print("Você venceu!")
        if escolha == escolha_computador:
            print("Empate!")
    else:
        print("Insira um número válido!")
    saida = input("Gostaria de jogar novamente? (y/n)\n")
    if saida == 'y':
        print('\n')
    if saida == 'n':
        break