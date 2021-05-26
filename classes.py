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
        super().__init__()
        money = self.dinheiro
        adquiridos = []
        estoque_de_moveis = {"sofá":3000,
        "mesa":2299,
        "video game":1450,
        "tv":1900}
        print(estoque_de_moveis)
        print(type(estoque_de_moveis))
        escolha_do_movel = input(f"Você tem {money} \nEscolha o móvel que deseja ou sair:").lower()
        while True:    
            if escolha_do_movel == "sair":
                print("Até logo")
                break
            else:
                for item in estoque_de_moveis:
                    if escolha_do_movel in estoque_de_moveis:
    
                        preco = estoque_de_moveis.get(escolha_do_movel)
                        print(preco)
                        print(type(preco))
                        self.dinheiro = money - preco
                        print(f"{escolha_do_movel} foi adquirido por {preco} e você ficou com {self.dinheiro}")
                        adquiridos = estoque_de_moveis.pop()
                        print(f"Você já tem {adquiridos}")
                    elif escolha_do_movel in adquiridos or adquiridos == "":
                        print("Produto indisponivel, você já tem.")
                        break
                    else:
                        print("Produto inválidoa!")
                        break


#=======


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
#>>>>>>> f8da74d132b64d8b691e5f89a99e0cc32b73c8b5
