import strategies as s
import random
import pergunta_Factory as pf

class Quiz:
    def __init__(self, dados_json):
        self.dados_json = dados_json
        self.strategy = None
        self.pontos = 0

    def escolher_dificuldade(self):
        print("=== Bem-vindo ao Quiz de One Piece ===\n")
        print("Escolha a dificuldade:")
        print("1. Fácil")
        print("2. Médio")
        print("3. Difícil")
        print("4. Misto")

        escolha = int(input("\nDigite o número da dificuldade: "))

        if escolha == 1:
            self.strategy = s.FacilStrategy()
        elif escolha == 2:
            self.strategy = s.MedioStrategy()
        elif escolha == 3:
            self.strategy = s.DificilStrategy()
        elif escolha == 4:
            self.strategy = s.MistoStrategy()
        else:
            print("Opção inválida, saindo...")
            exit()

    def jogar(self):
        if self.strategy is None:
            self.escolher_dificuldade()

        perguntas_raw = self.strategy.selecionar_perguntas(self.dados_json)
        random.shuffle(perguntas_raw)

        perguntas = [pf.criar(p) for p in perguntas_raw]

        for idx, pergunta in enumerate(perguntas, 1):
            alternativas = pergunta.exibir(idx)

            while True:  # validação de entrada
                resposta = input("Sua resposta: ").strip()

                if not resposta.isdigit():  # não é número
                    print("⚠️ Digite um número válido entre 1 e 4.")
                    continue

                resposta = int(resposta)
                if resposta < 1 or resposta > len(alternativas):  # fora do intervalo
                    print("⚠️ Escolha um número entre 1 e 4.")
                    continue

                break  # entrada válida

            # verificar resposta
            if alternativas[resposta - 1]["correct"]:
                print("✅ Correto!")
                self.pontos += 1
            else:
                print("❌ Errado!")
                correta = next(alt['alt'] for alt in alternativas if alt['correct'])
                print(f"A resposta correta era: {correta}")

        print("\n=== Fim do quiz! ===")
        print(f"Você acertou {self.pontos} de {len(perguntas)} perguntas.")