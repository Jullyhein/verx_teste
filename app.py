from fastapi import FastAPI
from jogo import Jogo

app = FastAPI()

@app.get("/jogo/simular")
def simular_jogo():
    jogo = Jogo()
    vencedor, jogadores_ordenados = jogo.jogar()
    jogadores_com_saldo = sorted(
        [{"tipo": j.tipo, "saldo": j.saldo} for j in jogo.jogadores], 
        key=lambda j: j["saldo"], 
        reverse=True
    )
    
    return {
        "vencedor": vencedor,
        "jogadores": jogadores_com_saldo
    }