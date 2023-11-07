from tkinter import *
from datetime import datetime, timedelta
import login, dados
# import plotly.express as pw
# import pandas as pd

janela_trade = Tk()
janela_trade.title("BALANÇO TRADING JOELSON")
largura = 800  # Largura da janela em pixels
altura = 350   # Altura da janela em pixels
janela_trade.geometry(f"{largura}x{altura}")

dados_dias_uteis = {
    
}

patrimonio_atual = 100.00

# def grafico():
#     datas = [dados_dias_uteis]
#     valores = [patrimonio_atual]
#     df = pd.DataFrame({"Data": datas, "Valor": valores})

def calcular_patrimonio():
    global patrimonio_atual
    
    data_atual = datetime.now().strftime('%d/%m')
    valor_do_dia_atual = dados_dias_uteis[data_atual]["Valor do Dia"]
    patrimonio_atual += valor_do_dia_atual
    texto_resposta.config(text=f"Patrimônio atual: {patrimonio_atual:.2f}")

def calcular():
    operacao_positiva = int(entrada_positiva.get())
    operacao_negativa = int(entrada_negativa.get())
    operacao_empate = int(entrada_empate.get())
    ganho_dia = float(entrada_ganho_dia.get())

    dia_operacao = datetime.now().day
    mes_operacao = datetime.now().month
    ano_operacao = datetime.now().year


    total_op = operacao_positiva + operacao_negativa + operacao_empate
    taxa_op = total_op * 0.5
    acertividade = (operacao_positiva / total_op) * 100
    valor_dia = ganho_dia - taxa_op
    irrf = (valor_dia + taxa_op) * 0.01

    dados_dias_uteis[f"{dia_operacao}/{mes_operacao}"] = {
        "Acertividade": acertividade,
        "Taxa Operacional": taxa_op,
        "Valor do Dia": valor_dia,
        "IRRF": irrf
    }

    texto_resposta.config(text=f"Valor do Dia: R$ {valor_dia:.2f}\nAcertividade: {acertividade}\nTAXA de operação: {taxa_op}\nIRRF: {irrf}")

    dados.inserirDados(dia_operacao, mes_operacao, ano_operacao, operacao_positiva, operacao_empate, operacao_negativa, 100, 200, 35, 25, 10, 95, 10000)


def relatorio_semanal():
    total_acertividade = 0
    total_pontos = 0
    valor_dia = 0

    data_inicio = datetime.now() - timedelta(days=7)

    dados_ultimos_7_dias = {data: valores for data, valores in dados_dias_uteis.items() if datetime.strptime(data, '%d/%m') >= data_inicio}

    for data, valores in dados_ultimos_7_dias.items():
        total_acertividade += valores["Acertividade"]
        total_pontos += valores["Acertividade"]
        valor_dia += valores["Valor do Dia"]

    texto_resposta.config(text=f"Acertividade Semanal: {total_acertividade:.2f}%\n"
                                f"Valor Ganho na Semana: {total_pontos:.0f} pontos\n"
                                f"Ganho da semana: {valor_dia:.2f}")
    
def relatorio_mensal():
    total_acertividade = 0
    total_pontos = 0
    valor_dia = 0

    data_inicio = datetime.now() - timedelta(days=30)

    dados_ultimos_30_dias = {data: valores for data, valores in dados_dias_uteis.items() if datetime.strptime(data, '%d/%m') >= data_inicio}

    for data, valores in dados_ultimos_30_dias.items():
        total_acertividade += valores["Acertividade"]
        total_pontos += valores["Acertividade"]
        valor_dia += valores["Valor do Dia"]

    texto_resposta.config(text=f"Acertividade Semanal: {total_acertividade:.2f}%\n"
                                f"Valor Ganho na Semana: {total_pontos:.0f} pontos\n"
                                f"Ganho da semana: {valor_dia:.2f}")
    
def relatorio_trimestral():
    total_acertividade = 0
    total_pontos = 0
    valor_dia = 0

    data_inicio = datetime.now() - timedelta(days=90)

    dados_ultimos_90_dias = {data: valores for data, valores in dados_dias_uteis.items() if datetime.strptime(data, '%d/%m') >= data_inicio}

    for data, valores in dados_ultimos_90_dias.items():
        total_acertividade += valores["Acertividade"]
        total_pontos += valores["Acertividade"]
        valor_dia += valores["Valor do Dia"]

    texto_resposta.config(text=f"Acertividade Semanal: {total_acertividade:.2f}%\n"
                                f"Valor Ganho na Semana: {total_pontos:.0f} pontos\n"
                                f"Ganho da semana: {valor_dia:.2f}")
    
def limpar_relatorio():
    texto_resposta.config(text='')


# Interface 
texto_resposta = StringVar()  
rotulo_resposta = Label(janela_trade, textvariable=texto_resposta)
rotulo_resposta.grid(column=0, row=6, columnspan=2, padx=10, pady=10) 
texto_resposta = Label(janela_trade, text="")
texto_resposta.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

entrada_positiva = Entry(janela_trade)
entrada_positiva.grid(column=1, row=0, padx=10, pady=10)
entrada_negativa = Entry(janela_trade)
entrada_negativa.grid(column=1, row=1, padx=10, pady=10)
entrada_empate = Entry(janela_trade)
entrada_empate.grid(column=1, row=2, padx=10, pady=10)
entrada_ganho_dia = Entry(janela_trade)
entrada_ganho_dia.grid(column=1, row=3, padx=10, pady=10)

rotulo_positiva = Label(janela_trade, text="Operações Positivas:")
rotulo_positiva.grid(column=0, row=0, padx=10, pady=10)
rotulo_negativa = Label(janela_trade, text="Operações Negativas:")
rotulo_negativa.grid(column=0, row=1, padx=10, pady=10)
rotulo_empate = Label(janela_trade, text="Operações Empate:")
rotulo_empate.grid(column=0, row=2, padx=10, pady=10)
rotulo_ganho_dia = Label(janela_trade, text="Ganho do Dia (em R$):")
rotulo_ganho_dia.grid(column=0, row=3, padx=10, pady=10)

botao_calcular = Button(janela_trade, text="CALCULO", command=calcular)
botao_calcular.grid(column=0, row=5, columnspan=2, padx=10, pady=10)
botao_semana = Button(janela_trade, text="RELATÓRIO SEMANAL", command=relatorio_semanal)
botao_semana.grid(column=2, row=0, columnspan=1, padx=10, pady=10)
botao_mensal = Button(janela_trade, text="RELATÓRIO MENSAL", command=relatorio_mensal)
botao_mensal.grid(column=3, row=0, columnspan=1, padx=10, pady=10)
botao_trimestral = Button(janela_trade, text="RELATORIO TRIMESTRAL", command=relatorio_trimestral)
botao_trimestral.grid(column=4, row=0, columnspan=1, padx=10, pady=10)
botao_limpa_texto = Button(janela_trade, text="Limpar", command=limpar_relatorio)
botao_limpa_texto.grid(column=0, row=5 ,columnspan=1 ,padx=10, pady=10)
botao_patrimonio = Button(janela_trade, text="PATRIMONIO ATUAL", command=calcular_patrimonio)
botao_patrimonio.grid(column=0, row=6, columnspan=1, padx=10, pady=10)


janela_trade.mainloop()
