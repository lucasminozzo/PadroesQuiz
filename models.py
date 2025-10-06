import random
class Pergunta:
    def __init__(self, enunciado, alternativas):
        self.enunciado = enunciado
        self.alternativas = alternativas

    def exibir(self, numero):
        print(f"\nPergunta {numero}: {self.enunciado}")
        random.shuffle(self.alternativas)
        for i, alt in enumerate(self.alternativas, 1):
            print(f"  {i}. {alt['alt']}")
        return self.alternativas
