from tkinter import *
import datetime
import json
from pathlib import Path

janela_trade = Tk()
janela_trade.title("BALANÇO TRADING JOELSON")
largura = 900  # Largura da janela em pixels
altura = 500   # Altura da janela em pixels
janela_trade.geometry(f"{largura}x{altura}")


dados_dias_uteis = {}

texto_hora = Label(janela_trade, text="", font=("Arial", 10, "bold"))
texto_hora.grid(column=60, row=0, columnspan=1, padx=0, pady=0)  

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

# Obtenha a hora atual
hora_atual = datetime.datetime.now().strftime("%H:%M")
        
# Atualize o rótulo com a hora atual como título
texto_hora.config(text=f"{hora_atual}")

def data_op(dia, mes, valor_dia):
    
    current_directory = Path.cwd()
    file_path = current_directory / "operacao.json"
    dados = {}
    if file_path.exists():
        with open(file_path, 'r', encoding='utf8') as file:
            dados = json.load(file)
    dados[str("dia") == dia,
          ("mes") == mes],
    with open(file_path, 'w', encoding='utf8') as file:
        json.dump(dados, file)

    return (dia)



def calcular():
    global pontos, valor_dia  
    try:

        valor_dia_input = float(valor_dia.get())  
        pontos = (valor_dia_input / 20) * 100  
        
        #data_atual = datetime.now()
        # dia = data_atual.day
        # mes = data_atual.month
        # data_op(dia, mes, valor_dia)

        if valor_dia_input >= 60:
            texto_resposta.config(text="META!")  
        elif valor_dia_input >= 0:
            texto_resposta.config(text=f"Você ganhou {pontos:.0f} pontos no dia.") 
        else:
            texto_resposta.config(text="STOP!") 

        data_op()
        
   
        
    except ValueError:
        texto_resposta.config(text="Por favor, insira valores numéricos.")

def calcular_taxa(positiva, negativa, empate):
    taxa = (positiva + negativa + empate) *0.5



# BOTÕES
botao_calcular = Button(janela_trade, text="CALCULO", command=calcular)
botao_calcular.grid(column=0, row=5, columnspan=2, padx=10, pady=10)
botao_semanal = Button(janela_trade, text="RELATORIO SEMANAL")
botao_semanal.grid(column=10, row=0, columnspan=3, padx=10, pady=10)
botao_mensal = Button(janela_trade, text="RELATORIO MENSAL",)
botao_mensal.grid(column=20, row=0, columnspan=4, padx=10, pady=10)
botao_trimestal = Button(janela_trade, text="RELATORIO TRIMESTRAL",)
botao_trimestal.grid(column=30, row=0, columnspan=2, padx=10, pady=10)
botao_taxa = Button(janela_trade, text="TAXAS")
botao_taxa.grid(column=0, row=15, columnspan=1, padx=10, pady=10)
botao_irrf = Button(janela_trade, text="IRRF")
botao_irrf.grid(column=0, row=15, columnspan=2, padx=10, pady=10)



janela_trade.mainloop()
