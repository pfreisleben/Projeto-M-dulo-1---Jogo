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
        self.dinheiro = 10000
        self.salario = 100
        self.faltasTrabalho = 7
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
        self.estoque_de_moveis = {"sofa": 3000,
                                  "mesa": 2299,
                                  "video game": 1450,
                                  "tv": 11900}

    def estoque(self):
        return f"Você tem {self.remedios} remedio(s) e {self.comida} alimentos"

    def moveis(self, personagem):
        # super().__init__()
        print(f'Você já tem: {self.ja_tem}')
        print(f'Móveis disponiveis para compra: ')
        print(self.estoque_de_moveis)

        while True:
            escolha_do_movel = input(
                f"Você tem {personagem.dinheiro} \nEscolha o móvel que deseja ou sair: ").lower()
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
                        return print(f"{escolha_do_movel} foi adquirido por {preco} e você ficou com {personagem.dinheiro}")
                    else:
                        return print(f"Você não tem dinheiro para comprar esse produto, falta {preco - personagem.dinheiro}")
                else:
                    return print("Produto inválido!")


class Dia:
    def __init__(self):
        self.dia = 1
        self.finalDeSemana = False

    def __str__(self):
        return f"{self.dia}, {self.semana()}"

    # Se for sáb ou dom, FDS = True.
    def avancaDia(self):
        if 6 <= self.dia <= 7:
            self.finalDeSemana = True
        else:
            self.finalDeSemana = False
        if self.dia == 7:
            self.dia = 1
        else:
            self.dia += 1

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
