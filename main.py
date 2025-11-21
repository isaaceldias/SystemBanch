menu = """
=============================
  Bem-vindo ao Banco XYZ
=============================

1 - Depositar
2 - Sacar
3 - Extrato
0 - Sair
=============================
"""

LIMITE_SAQUES = 3
VALOR_LIMITE_SAQUE = 500
saques = 0
saldo = 0
extrato = {"Entradas": [], "Saídas": [], "Saldo": saldo}

while True:
    input_usuario = int(input(menu))
    match input_usuario:
        case 0:
            print("Obrigado por usar o Banco XYZ. Até logo!")
            break
        case 1:
            valor_deposito = float(input("Digite o valor do depósito: R$ "))
            saldo += valor_deposito
            extrato["Entradas"].append(valor_deposito)
            extrato["Saldo"]=saldo
            print(
                f"""
Valor depositado com sucesso!
                  
Saldo atualizado: R${saldo:.2f}
                  """
            )
        case 2:
            valor_saque = float(input("Informe o valor que deseja sacar: R$ "))
            if valor_saque > VALOR_LIMITE_SAQUE:
                print(
                    """
    OPERAÇÃO FALHOU!!!
                    
O valor informado é maior que o limite disponível!
                """
                )
            elif saques >= LIMITE_SAQUES:
                print(
                    """
    OPERAÇÃO FALHOU!!!
                    
A quantidade de saques atingiu seu limite!
                    """
                )
            elif valor_saque > saldo and valor_saque > 0:
                print(
                    """
    OPERAÇÃO FALHOU!!!
                    
O valor informado é maior que o saldo disponível!
                    """
                )
            else:
                saldo -= valor_saque
                saques+=1
                extrato["Saídas"].append(valor_saque)
                extrato["Saldo"]=saldo
                
                print(
                    f"""
    OPERAÇÃO CONCLUÍDA!!!
                
Saldo atualizado: R$ {saldo:.2f}
                    """
                )
        case 3:
            texto_entradas = ""
            for valor in extrato["Entradas"]:
                texto_entradas += f"R${valor:.2f}\n"

            texto_saidas = ""
            for valor in extrato["Saídas"]:
                texto_saidas += f"R${valor:.2f}\n"

            print(
                """
====================================
        EXTRATO BANCÁRIO
====================================
                """)
            print("\n[ + ] ENTRADAS: ")
            print(f"{texto_entradas if texto_entradas else "Sem movimentações"}\n")
            print("\n[ - ] SAÍDAS: ")
            print(f"{texto_saidas if texto_saidas else "Sem movimentações"}\n")
            print(f"""
====================================
    SALDO ATUAL:      R$ {extrato['Saldo']:.2f}
====================================
                  """)
        case _:
            print("Opção inválida, selecione novamente uma operação.")
