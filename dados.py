import json

def inserirDados(dia_operacao, mes_operacao, ano_operacao,op_positiva, op_empate, op_negativa, valor_inicial, valor_dia, pontos_dia, taxa_op, irrf, acertividade, patrimonio):
    novo_dado = {
        "dia": dia_operacao,
        "mes": mes_operacao,
        "ano": ano_operacao,
        "positiva": op_positiva,
        "empate": op_empate,
        "negativa": op_negativa,
        "valor_inicial": valor_inicial,
        "valor_dia": valor_dia,
        "taxa_op": taxa_op,
        "irrf": irrf,
        "patrimonio": patrimonio,
        "acertividade": acertividade,
        "pontos": pontos_dia
    }
    
    
    dados_dias_uteis = ler_json('operacao.json')
    dados_dias_uteis.append(novo_dado)

    salvar_json(dados_dias_uteis, 'operacao.json')

    json.JSONEncoder()
    
    return dados_dias_uteis

def salvar_json(dados, nome_arquivo):
        try:
            with open(nome_arquivo, 'w') as arquivo:
                json.dump(dados, arquivo, indent=4)
            print(f"Dados salvos com sucesso no arquivo '{nome_arquivo}'.")
        except Exception as e:
            print(f"Erro ao salvar dados no arquivo '{nome_arquivo}': {e}")

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo '{nome_arquivo}'. Verifique se o arquivo está em formato JSON válido.")
        return None