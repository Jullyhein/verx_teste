import random 

class Propriedades:
    def __init__(self, id, custo_venda, valor_aluguel, proprietario=None):
        self.id = id
        self.custo_venda = custo_venda
        self.valor_aluguel = valor_aluguel
        self.proprietario = proprietario
        
    def __repr__(self):
        return f'Propriedade id = {self.id}, custo_venda = {self.custo_venda}, valor_aluguel = {self.valor_aluguel}, proprietario = {self.proprietario})'


class Jogadores():
    def __init__(self, tipo, saldo_inicial = 300):
        self.tipo = tipo
        self.saldo = saldo_inicial
        self.propriedades = [] 
        self.posicao = 0
        self.esta_no_jogo = True

    def ajustar_saldo(self, valor):
       self.saldo += valor
       if self.saldo < 0:
           self.esta_no_jogo = False

    def perfil_de_compra(self, propriedade):
        if self.tipo == "impulsivo":
            return self.saldo >= propriedade.custo_venda
        elif self.tipo == "exigente":
            return self.saldo >= propriedade.custo_venda and propriedade.valor_aluguel > 50
        elif self.tipo == "cauteloso":
            return self.saldo >= propriedade.custo_venda and (self.saldo - propriedade.custo_venda) >= 80
        elif self.tipo == "aleatorio":
            return self.saldo >= propriedade.custo_venda and random.choice([True, False])

    def comprar_propriedade(self,propriedade):
        if self.perfil_de_compra(propriedade):
            self.saldo(-propriedade.custo_venda)
            propriedade.proprietario = self
            self.propriedades.append(propriedade)

    def mover(self, num_posicoes, total_propriedades):
       self.posicao = (self.posicao + num_posicoes) % total_propriedades
       return self.posicao

    def __repr__(self):
        return f'Tipo de Jogador = {self.tipo}, saldo = {self.saldo}, propriedades = {self.propriedades})'



class Tabuleiro:
    def __init__(self):
        self.propriedades = [Propriedades(i, random.randint(50, 150), random.randint(10, 50)) for i in range(20)]


if __name__ == "__main__":
    propriedade1 = Propriedades(id=2, custo_venda=1000, valor_aluguel=150, proprietario=None)
    jogador1 = Jogadores(tipo="cauteloso")

    
    print(f"Estado inicial do jogador: {jogador1}")
    print(f"Estado inicial da propriedade: {propriedade1}")

    if jogador1.comprar_propriedade(propriedade1):
        print("\nJogador comprou a propriedade com sucesso")
    else:
        print("\nJogador não conseguiu comprar a propriedade.")


    print(f"Estado final do jogador: {jogador1}")
    print(f"Estado final da propriedade: {propriedade1}")
