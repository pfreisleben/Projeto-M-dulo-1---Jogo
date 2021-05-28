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
        self.dinheiro = 1000
        self.salario = 100
        self.faltasTrabalho = 0
        self.desempregado = False

    def __str__(self):
        return "Você está " + ("sujo" if self.sujo else "limpo")+", "+("com" if self.fome else "sem")+" fome e "+("" if self.medicado else "não ")+"tomou sua medicação. Você tem "+str(self.dinheiro)+" reais na sua conta."

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.medicado = False


class Casa():
    def __init__(self):
        self.remedios = 1
        self.comida = 5
        self.ja_tem = ["cama", "geladeira", "fogão"]
        self.estoque_de_moveis = {"sofa": 300,
                                  "mesa": 230,
                                  "video game": 150,
                                  "tv": 170}

    def estoque(self):
        return f"Você tem {self.remedios} remedio(s) e {self.comida} alimentos"

    def moveis(self, personagem):
        print(f'Móveis que você já tem: {self.ja_tem}')
        while True:
            print(f'Estoque disponível para compra: ')
            print(self.estoque_de_moveis)
            escolha_do_movel = input(
                f"Você tem R${personagem.dinheiro:.2f} \nEscolha o móvel que deseja ou digite sair: ").lower()
            if escolha_do_movel == "sair":
                print("Até logo")
                break
            else:
                if escolha_do_movel in self.estoque_de_moveis:
                    preco = self.estoque_de_moveis.get(escolha_do_movel)
                    if preco <= personagem.dinheiro:
                        personagem.dinheiro -= preco
                        self.ja_tem.append(escolha_do_movel)
                        self.estoque_de_moveis.pop(escolha_do_movel)
                        if len(escolha_do_movel) == 0:
                            print(
                                f'Você comprou todos os móveis, você ganhou o jogo!')
                            break
                        print(
                            f"{escolha_do_movel} foi adquirido por R${preco:.2f} e você ficou com R${personagem.dinheiro:.2f}")
                    else:
                        print(
                            f"Você não tem dinheiro para comprar esse produto, falta {preco - personagem.dinheiro}")
                else:
                    print("Produto inválido!")


class Dia:
    def __init__(self):
        self.dia = 1
        self.finalDeSemana = False

    def __str__(self):
        return f"{self.dia}, {self.semana()}"

    # Se for sáb ou dom, FDS = True.
    def avancaDia(self):
        if self.dia == 7:
            self.dia = 1
        else:
            self.dia += 1
        if self.dia == 6 or self.dia == 7:
            self.finalDeSemana = True
        else:
            self.finalDeSemana = False

    def semana(self):
        if self.dia == 1:
            return "Segunda-feira"
        elif self.dia == 2:
            return "Terça-feira"
        elif self.dia == 3:
            return "Quarta-feira"
        elif self.dia == 4:
            return "Quinta-feira"
        elif self.dia == 5:
            return "Sexta-feira"
        elif self.dia == 6:
            return "Sábado"
        elif self.dia == 7:
            return "Domingo"
