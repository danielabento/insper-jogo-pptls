# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:49:55 2015

@author: Dani Bento
"""

from random import randint
programa = randint(1,5)
jpontos = 0
ppontos = 0
while jpontos<=3 or ppontos<=3:
    jogador = int(input("Vamos jogar! Coloque o número da sua escolha: 1-Pedra, 2-Papel, 3-Tesoura, 4-Lagarto ou 5-Spock?"))

    if programa == jogador:
        print("Empatou!")
        continue
    elif programa == 1 and (jogador == 3 or jogador == 4):
        print("Você perdeu essa rodada! Tente novamente.")
        ppontos += 1
        if ppontos < 3:
            continue
        if ppontos == 3:
            print("Que pena! O computador ganhou o jogo!")
            break
    elif programa == 2 and (jogador == 1 or jogador == 5):
        print("Você perdeu essa rodada! Tente novamente.")
        ppontos += 1
        if ppontos < 3:
            continue
        if ppontos == 3:
            print("Que pena! O computador ganhou o jogo!")
            break
    elif programa == 3 and (jogador == 2 or jogador == 4):
        print("Você perdeu essa rodada! Tente novamente.")
        ppontos += 1
        if ppontos < 3:
            continue
        if ppontos == 3:
            print("Que pena! O computador ganhou o jogo!")
            break
    elif programa == 4 and (jogador == 2 or jogador == 5):
        print("Você perdeu essa rodada! Tente novamente.")
        ppontos += 1
        if ppontos < 3:
            continue
        if ppontos == 3:
            print("Que pena! O computador ganhou o jogo!")
            break
    elif programa == 5 and (jogador == 3 or jogador == 1):
        print("Você perdeu essa rodada! Tente novamente.")
        ppontos += 1
        if ppontos < 3:
            continue
        if ppontos == 3:
            print("Que pena! O computador ganhou o jogo!")
            break

    else:
        print("Você ganhou essa rodada! Continue assim.")
        jpontos += 1
        if jpontos < 3:
            continue
        if jpontos == 3:
            print("Parabéns! Você ganhou o jogo!")
            break
