# Este arquivo vai ser utilizando pra criar e estruturar as classes, que serão importadas no projeto principal.
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


class Dia:
    def __init__(self):
        self.dia = 1
        self.finalDeSemana = False

    def __str__(self):
        return f"Hoje é dia {self.dia}, {self.semana()}"

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
