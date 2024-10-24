from models.classes import Jogadores, Tabuleiro
import random

class Jogo:
    def __init__(self):
        self.jogadores = [
            Jogadores("Impulsivo"),
            Jogadores("Exigente"),
            Jogadores("Cauteloso"),
            Jogadores("Aleatório")
        ]
        self.tabuleiro = Tabuleiro()

    def jogar(self):
        rodada = 0
        while len([j for j in self.jogadores if j.esta_no_jogo]) > 1 and rodada < 1000:
            for jogador in self.jogadores:
                if jogador.esta_no_jogo:
                    self.jogar_rodada(jogador)
            rodada += 1
        vencedor = max(self.jogadores, key=lambda j: j.saldo if j.esta_no_jogo else float('-inf'))
        return vencedor.tipo, [j.tipo for j in sorted(self.jogadores, key=lambda j: j.saldo, reverse=True)]    

    def jogar_rodada(self, jogador):
        #jogar dado
        dado = random.randint(1,6)
        posicao = jogador.mover(dado, len(self.tabuleiro.propriedades))
        propriedade = self.tabuleiro.propriedades[posicao]
        #verificar compra ou pagamento do aluguel
        if propriedade.proprietario is None:
            jogador.comprar_propriedade(propriedade)
        elif propriedade.proprietario != jogador:
            jogador.ajustar_saldo(-propriedade.valor_aluguel)
            propriedade.proprietario.ajustar_saldo(propriedade.valor_aluguel)

        # Adicionar 100 ao saldo se completou uma volta
        if posicao < dado:
            jogador.ajustar_saldo(100)