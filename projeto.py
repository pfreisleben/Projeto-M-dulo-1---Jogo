# Ideias implantadas:
# Opção 8 - Chequar estoque de comida e remédio
# Opção 9 - Compra de móveis, validando estoque disponivel, dinheiro, e caso compre tudo, ganha o jogo.
# Variar o preço do café da manhã
# Criação da classe "Dia", responsavél por armazenar a data, e valida se é final de semana ou não.
# Caso vá dormir sem trabalhar, adiciona uma falta ao trabalho(caso não seja final de semana)
# Caso seja final de semana, não pode trabalhar, e a opção desaparece do menu.
# Caso falte mais de 5 vezes no trabalho, é demitido e perde o Jogo.
# Informe o nome do dia da semana: Segunda, Terça....
# Opção 10 - O personagem pode dormir direto, avançando um dia.
# Criado menu adaptado para o final de semana, com opções únicas.

# As ideias implantadas usaram os conceitos de Encapsulamento, Módulo, Classe, Variavel, Loops, Metodos, Operadores Lógicos e
# condicionais.

# A idéia principal foi melhorar e implantar novas funcionalidades no projeto, ao invés de criar uma história totalmente
# diferente, caso o personagem consiga comprar todos os móveis, ele ganha. Se for demitido, perde.

# Integrantes: Pedro Freisleben, Italo, Marcio Salu Pereira
# Criamos um projeto no git e todos os integrantes do projeto foram adicionados como colaboradores, então todas as
# alterações foram feitas através de commits, sincronizando todo o trabalho. Definimos


import random


from classes import Personagem, Dia, Casa, Relogio


if(__name__ == "__main__"):
    dia = Dia()
    relogio = Relogio()
    personagem = Personagem()
    casa = Casa()
    while True:
        if dia.finalDeSemana:
            print("É final de semana! :)")
            print("São "+str(relogio)+" do dia "+str(dia) +
                  (". Você precisa sair para trabalhar até 07h00" if not dia.finalDeSemana else "."))
            print(personagem)
            print("")
            print("Ações:")
            print("1 - Tomar banho e escovar os dentes")
            print("2 - Fazer café da manhã")
            print("3 - Pedir café da manhã")
            print("4 - Tomar café da manhã")
            print("5 - Tomar remédio")
            print("6 - Comprar remédio")
            print("7 - Ir pro barzinho")
            print("8 - Ir para restaurante")
            print("9 - Futebol")
            print("10 - Dormir")
            print("11 - Trabalho Extra")
            print("0 - Sair do jogo")
            opcao = input(f'Digite sua opção: ')
            if(opcao == "1"):  # Toma Banho, escova dentes
                personagem.setSujo(False)
                relogio.avancaTempo(20)
            elif(opcao == "2"):  # Faz café da manhã
                if(casa.getComida() > 0):
                    casa.setComida(1)
                    personagem.cafeDaManha = True
                else:
                    print("Não há comida em casa.")
                relogio.avancaTempo(15)
            elif(opcao == "3"):  # Pede café da manhã
                lanche = random.randint(5, 15)
                if(personagem.getDinheiro() >= lanche):
                    personagem.setDinheiro(-lanche)
                    casa.setComida(1)
                    personagem.cafeDaManha = True
                    print(
                        f"O café da manhã custou {lanche} reais.")
                else:
                    print(
                        f"O café da manhã custa {lanche} reais, você não tem dinheiro suficiente.")
                relogio.avancaTempo(5)
            elif(opcao == "4"):  # Toma café da manhã
                if(personagem.cafeDaManha):
                    personagem.setFome(False)
                    personagem.cafeDaManha = False
                    relogio.avancaTempo(15)
                else:
                    print("Não tem café da manhã na sua casa.")
                    relogio.avancaTempo(5)
            elif(opcao == "5"):  # Toma remédio
                if(casa.getRemedios() > 0):
                    casa.setRemedios(1)
                    personagem.setMedicado(True)
                else:
                    print("Não tem remédio na sua casa")
                relogio.avancaTempo(5)
            elif(opcao == "6"):  # Compra remédio
                if(personagem.getDinheiro() >= 20):
                    casa.remedios += 10
                    personagem.setDinheiro(-20)
                    relogio.avancaTempo(10)
                    print(personagem.getDinheiro())
                    print(
                        f"A cartela com 10 remédios custa 20 reais, você ficou com {personagem.getDinheiro()}")
                else:
                    print(
                        f"A cartela com 10 remédios custa 20 reais, e você tem apenas {personagem.getDinheiro()}.")
                    relogio.avancaTempo(5)
            elif(opcao == "7"):  # ir pro barzinho
                barzinho = random.randint(30, 90)
                if personagem.getDinheiro() >= 140:
                    print(
                        f'É final de semana e você foi pro barzinho!Você gastou {barzinho}')
                    personagem.getDinheiro() -= barzinho
                    if personagem.getFome():
                        print(
                            f'Como você foi para o barzinho sem comer, você passou mal!')
                        print(
                            f'Você vomitou no carro do Uber, e precisou pagar R$ 50')
                        personagem.setDinheiro(-50)
                else:
                    print(
                        "Você não tem grana para ir pro bar. Ficou em casa tomando uma de boa")
                personagem.dormir()
                relogio = Relogio()
                dia.avancaDia()

            elif(opcao == "8"):  # Ir para restaurante
                restaurante = random.randint(30, 80)
                if personagem.getDinheiro() >= restaurante:
                    print(
                        f'É final de semana e você foi pro restaurante!Você gastou {restaurante}')
                    personagem.setDinheiro(-restaurante)
                else:
                    print(
                        "Você não tem grana para ir pro bar. Ficou em casa comendo miojo")
                personagem.dormir()
                relogio = Relogio()
                dia.avancaDia()

            elif(opcao == "9"):  # Futebol
                futebol = random.randint(10, 35)

                if 10 <= personagem.getDinheiro() <= 35:
                    print(
                        f'É final de semana e você foi pro futebol!Você gastou {futebol}')
                    personagem.setDinheiro(-futebol)
                elif personagem.getDinheiro() >= 65:
                    print(
                        f'É final de semana e você foi pro futebol e depois para uma resenha das boas \n!Você gastou {futebol+30}')
                    personagem.setDinheiro(-futebol-30)
                else:
                    print(
                        "Você não tem grana para ir pro futebol. Ficou em casa jogando video")
                personagem.dormir()
                relogio = Relogio()
                dia.avancaDia()
            elif(opcao == "10"):
                personagem.dormir()
                relogio = Relogio()
                dia.avancaDia()
                if not dia.finalDeSemana:
                    personagem.faltasTrabalho += 1

            elif(opcao == "11"):  # Trabalho extra
                extra = random.randint(150, 200)
                if personagem.getRemedio():
                    f"Você passou mal e não conseguiu trabalhar direito, recebeu metade do valor"
                    print(f'Você trabalhou o dia todo e ganhou R$ {extra/2}.')
                    personagem.setDinheiro(extra/2)
                else:
                    print(f'Você trabalhou o dia todo e ganhou R$ {extra}.')
                    personagem.setDinheiro(extra)
                personagem.dormir()
                relogio = Relogio()
                dia.avancaDia()

            elif(opcao == "0"):
                break
            else:
                print("Opção inválida!")
                relogio.avancaTempo(5)
        else:
            print("---")
            print("São "+str(relogio)+" do dia "+str(dia) +
                  (". Você precisa sair para trabalhar até 07h00" if not dia.finalDeSemana else "."))
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
            print("9 - Comprar móveis")
            print("10 - Dormir")
            print("0 - Sair do jogo")
            opcao = input("Escolha sua ação:")
            if(opcao == "1"):  # Toma Banho, escova dentes
                personagem.setSujo(False)
                relogio.avancaTempo(20)
            elif(opcao == "2"):  # Faz café da manhã
                if(casa.getComida() > 0):
                    casa.setComida(1)
                    personagem.cafeDaManha = True
                else:
                    print("Não há comida em casa.")
                relogio.avancaTempo(15)
            elif(opcao == "3"):  # Pede café da manhã
                lanche = random.randint(5, 15)
                if(personagem.getDinheiro() >= lanche):
                    casa.setComida(1)
                    personagem.setDinheiro(-lanche)
                    personagem.cafeDaManha = True
                    print(
                        f"O café da manhã custou {lanche} reais.")
                else:
                    print(
                        f"O café da manhã custa {lanche} reais, você não tem dinheiro suficiente.")
                relogio.avancaTempo(5)
            elif(opcao == "4"):  # Toma café da manhã
                if(personagem.cafeDaManha):
                    personagem.setFome(False)
                    personagem.cafeDaManha = False
                    relogio.avancaTempo(15)
                else:
                    print("Não tem café da manhã na sua casa.")
                    relogio.avancaTempo(5)
            elif(opcao == "5"):  # Toma remédio
                if(casa.getRemedios() > 0):
                    casa.setRemedios(1)
                    personagem.setMedicado
                    print("Não tem remédio na sua casa")
                relogio.avancaTempo(5)
            elif(opcao == "6"):  # Compra remédio
                if(personagem.getDinheiro() >= 20):
                    casa.setRemedios(10)
                    personagem.setdinheiro(-20)
                    relogio.avancaTempo(10)
                    print(
                        f"A cartela com 10 remédios custa 20 reais, você ficou com {personagem.dinheiro}")
                else:
                    print(
                        f"A cartela com 10 remédios custa 20 reais, e você tem apenas {personagem.dinheiro}.")
                    relogio.avancaTempo(5)
            elif(opcao == "7"):  # Vai trabalhar
                print("-=-=-")
                print("Você foi trabalhar.")
                print(personagem)
                print("-=-=-")
                recebido = personagem.getSalario()
                if personagem.faltasTrabalho > 5:
                    print(
                        "Como você faltou ao trabalho mais de 5 vezes, o seu chefe demitiu você. Por justa causa... ")
                    print(f'Você retornou a sua casa. ')
                    print(
                        f'Como você foi demitido, você perdeu o jogo, Game Over!')
                    break
                elif(not personagem.medicado):
                    print(
                        "Como você não tomou seu remédio, você ficou doente no caminho e não chegou no trabalho")
                    recebido = 0
                elif(personagem.getSujo()):
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

                personagem.setDinheiro(recebido)
                personagem.dormir()
                relogio = Relogio()
                dia.avancaDia()

            elif(opcao == "8"):  # Mostra estoque de comida e remédio
                print(casa.estoque())

            elif(opcao == "9"):  # Inicia compra de moveis
                casa.moveis(personagem)
                relogio.avancaTempo(10)
                if len(casa.estoque_de_moveis) == 0:
                    print(f'Você comprou todos os móveis e ganhou o jogo!')
                    break

            elif(opcao == "10"):
                personagem.dormir()
                relogio = Relogio()
                dia.avancaDia()
                if not dia.finalDeSemana:
                    personagem.faltasTrabalho += 1

            elif(opcao == "0"):
                break
            else:
                print("Opção inválida!")
                relogio.avancaTempo(5)
