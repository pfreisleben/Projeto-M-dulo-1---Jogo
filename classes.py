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

    def moveis(self):
        escolha_do_movel = input("Escolha o móvel que deseja: ")
        estoque_de_moveis = {"Sofá de 3 lugares, retrátil 2.80m": 3000.0,
                             "Mesa de jantar com 4 cadeiras": 2299.0,

                             }
