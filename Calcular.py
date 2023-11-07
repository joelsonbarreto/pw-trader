from tkinter import *
import json
from pathlib import Path
import datetime
from datetime import datetime

# Janela principal
janela_trade = Tk()
janela_trade.title("BALANÇO TRADING JOELSON")
largura = 900  # Largura da janela em pixels
altura = 500   # Altura da janela em pixels
janela_trade.geometry(f"{largura}x{altura}")

texto_hora = Label(janela_trade, text="", font=("Arial", 10, "bold"))
texto_hora.grid(column=8, row=0, columnspan=2, padx=10, pady=10) 

texto_positiva = Label(janela_trade, text="Positiva:")
texto_positiva.grid(column=0, row=0, padx=10, pady=10)
positiva = Entry(janela_trade)
positiva.grid(column=1, row=0, padx=10, pady=10)

texto_negativa = Label(janela_trade, text="Negativa:")
texto_negativa.grid(column=0, row=1, padx=10, pady=10)  
negativa = Entry(janela_trade)
negativa.grid(column=1, row=1, padx=10, pady=10)  

texto_empate = Label(janela_trade, text="Zero:")
texto_empate.grid(column=0, row=2, padx=10, pady=10)
empate = Entry(janela_trade)
empate.grid(column=1, row=2, padx=10, pady=10)

texto_valor_dia = Label(janela_trade, text="Valor do dia:")
texto_valor_dia.grid(column=0, row=3, padx=10, pady=10)
valor_dia = Entry(janela_trade)  
valor_dia.grid(column=1, row=3, padx=10, pady=10)  

texto_resposta = Label(janela_trade, text="")
texto_resposta.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# BOTÕES
botao_calcular = Button(janela_trade, text="Calcular dia", command=calcular)
botao_calcular.grid(column=0, row=5, columnspan=2, padx=10, pady=10)
botao_semanal = Button(janela_trade, text="RELATORIO SEMANAL",)
botao_semanal.grid(column=10, row=0, columnspan=3, padx=10, pady=10)
botao_mensal = Button(janela_trade, text="RELATORIO MENSAL",)
botao_mensal.grid(column=20, row=0, columnspan=4, padx=10, pady=10)
botao_trimestal = Button(janela_trade, text="RELATORIO TRIMESTRAL",)
botao_trimestal.grid(column=30, row=0, columnspan=2, padx=10, pady=10)
botao_taxa = Button(janela_trade, text="TAXAS")
botao_taxa.grid(column=0, row=15, columnspan=1, padx=10, pady=10)
botao_irrf = Button(janela_trade, text="IRRF")
botao_irrf.grid(column=0, row=15, columnspan=2, padx=10, pady=10)

def atualizar_hora():
    # Obtém a hora atual
    hora_atual = datetime.now().strftime("%H:%M:%S")
    # Atualiza o rótulo de texto com a hora atual
    texto_hora.config(text=hora_atual)
    # Atualiza a hora a cada 1000 milissegundos (1 segundo)
    texto_hora.after(1000, atualizar_hora)
    
atualizar_hora()


def data_op(dia, mes, valor_dia):
    
    current_directory = Path.cwd()
    file_path = current_directory / "datas.json"
    dados = {}
    if file_path.exists():
        with open(file_path, 'r', encoding='utf8') as file:
            dados = json.load(file)
    dados[str(mes)] = dia
    with open(file_path, 'w', encoding='utf8') as file:
        json.dump(dados, file)

def calcular():
    global pontos, valor_dia  
    try:

        valor_dia_entrada = float(valor_dia.get())  
        pontos = (valor_dia_entrada / 20) * 100
        
        data_atual = datetime.now()
        dia = data_atual.day
        mes = data_atual.month

        data_op(dia, mes, valor_dia)

        if valor_dia_entrada >= 60:
            texto_resposta.config(text="Atingiu a meta!")  
        elif valor_dia_entrada >= 0:
            texto_resposta.config(text=f"Você ganhou {pontos:.0f} pontos no dia.") 
        else:
            texto_resposta.config(text="STOP!")  
   
        
    except ValueError:
        texto_resposta.config(text="Por favor, insira valores numéricos.")









janela_trade.mainloop()
