# Proposta de projeto de ficção interativa para avaliação de OO
# Sugestão: completar com classes filhas colocando pessoas saudáveis,
# trabalhos menos remunerados, casas melhor equipadas et cetera
#   IDEIAS
# Variar o preço do café da manhã - Italo - Feito
# desconto de salário em % e talvez até demissão de faltar demais.
# comprar moveis, criar uma lista de produtos
# criar a opção de FDS, dia 6 e 7. Talvez um elemento random dentro dos dias, sorteando um feriado - PEDRO
# randomizar o que for possível.
# Criação da opção 8, estoque. Feito mas pode melhorar

# teste
import random


class Relogio:
    def __init__(self):
        self.horas = 6
        self.minutos = 0

    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"

    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1

    def atrasado(self):
        return (self.horas > 7 or (self.horas == 7 and self.minutos > 0))


class Personagem:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.medicado = False
        self.dinheiro = 0
        self.salario = 100

    def __str__(self):
        return "Você está " + ("sujo" if self.sujo else "limpo")+", "+("com" if self.fome else "sem")+" fome e "+("" if self.medicado else "não ")+"tomou sua medicação. Você tem "+str(self.dinheiro)+" reais na sua conta."

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.medicado = False


class Casa:
    def __init__(self):
        self.remedios = 1
        self.comida = 5

    def estoque(self):
        return f"Você tem {self.remedios} remedio(s) e {self.comida} alimentos"


if(__name__ == "__main__"):
    dia = 1
    relogio = Relogio()
    personagem = Personagem()
    casa = Casa()
    cafe_da_manha = False
    while True:
        print("---")
        print("São "+str(relogio)+" do dia "+str(dia) +
              ". Você tem que sair pro trabalho até às 07:00.")
        print(personagem)
        print("")
        print("Ações:")
        print("1 - Tomar banho e escovar os dentes")
        print("2 - Fazer café da manhã")
        print("3 - Pedir café da manhã")
        print("4 - Tomar café da manhã")
        print("5 - Tomar remédio")
        print("6 - Comprar remédio")
        print("7 - Ir trabalhar")
        print("8 - Ver estoque de remédio e comida")
        print("0 - Sair do jogo")
        opcao = input("Escolha sua ação:")
        if(opcao == "1"):
            personagem.sujo = False
            relogio.avancaTempo(20)
        elif(opcao == "2"):
            if(casa.comida > 0):
                casa.comida -= 1
                cafe_da_manha = True
            else:
                print("Não há comida em casa.")
            relogio.avancaTempo(15)
        elif(opcao == "3"):
            lanche = random.randint(5,15)
            if(personagem.dinheiro >= lanche):
                personagem.dinheiro -= lanche
                cafe_da_manha = True
                print(
                    f"O café da manhã custou {lanche} reais.")
            else:
                print(
                    f"O café da manhã custa {lanche} reais, você não tem dinheiro suficiente.")
            relogio.avancaTempo(5)
        elif(opcao == "4"):
            if(cafe_da_manha):
                personagem.fome = False
                cafe_da_manha = False
                relogio.avancaTempo(15)
            else:
                print("Não tem café da manhã na sua casa.")
                relogio.avancaTempo(5)
        elif(opcao == "5"):
            if(casa.remedios > 0):
                casa.remedios -= 1
                personagem.medicado = True
            else:
                print("Não tem remédio na sua casa")
            relogio.avancaTempo(5)
        elif(opcao == "6"):
            if(personagem.dinheiro >= 20):
                casa.remedios += 10
                personagem.dinheiro -= 20
                relogio.avancaTempo(10)
            else:
                print(
                    "A cartela com 10 remédios custa 20 reais, você não tem dinheiro suficiente.")
                relogio.avancaTempo(5)
        elif(opcao == "7"):
            print("-=-=-")
            print("Você foi trabalhar.")
            print(personagem)
            print("-=-=-")
            recebido = personagem.salario
            if(not personagem.medicado):
                print(
                    "Como você não tomou seu remédio, você ficou doente no caminho e não chegou no trabalho")
                recebido = 0
            elif(personagem.sujo):
                print(
                    "Como você estava sujo, seus colegas reclamaram para seu chefe, e você levou uma advertência.")
                recebido *= 0.9
            elif(personagem.fome):
                print(
                    "Como você estava com fome, você trabalhou metade do que consegue trabalhar.")
                recebido *= 0.5
            elif(relogio.atrasado()):
                print(
                    "Como você chegou atrasado, você produziu menos do que de costume.")
                recebido *= 0.8
            print("Você recebeu "+str(recebido) +
                  " reais pelo seu trabalho hoje.")
            print("-=-=-")

            personagem.dinheiro += recebido
            personagem.dormir()
            relogio = Relogio()
            dia += 1

        elif(opcao == "8"):
            print(casa.estoque())

        elif(opcao == "0"):
            break
        else:
            print("Opção inválida!")
            relogio.avancaTempo(5)
