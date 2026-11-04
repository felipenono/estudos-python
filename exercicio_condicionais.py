"""
PROBLEMA: Sistema de Desconto em Compras
Uma loja oferece descontos progressivos de acordo com o valor total da compra do cliente. 
Crie um programa que peça o valor da compra e aplique as seguintes regras:
- Compras abaixo de R$ 100,00: Sem desconto.
- Compras entre R$ 100,00 e R$ 300,00: Desconto de 10%.
- Compras acima de R$ 300,00: Desconto de 15%.
No final, o programa deve exibir o valor original, o desconto aplicado e o valor final a pagar.
"""

# Função principal que contém a lógica do programa
def calcular_compra():
    
    # Solicita ao usuário que digite o valor da compra e armazena na variável 'valor_compra'
    # O 'float()' converte o texto digitado (string) para um número decimal.
    valor_compra = float(input("Digite o valor total da compra: R$ "))
    
    # Cria a variável 'desconto' começando com 0 (nenhum desconto aplicado inicialmente)
    desconto = 0.0
    
    # Estrutura condicional (if/elif/else) para verificar as regras de desconto
    # Verifica se a compra é menor que 100
    if valor_compra < 100.00:
        # Se for menor, o desconto permanece 0.0 (já definido acima)
        print("Compras abaixo de R$ 100,00 não possuem desconto.")
        
    # O 'elif' (else if) só é executado se a condição anterior (if) for falsa.
    # Aqui verifica se a compra está entre 100 e 300.
    elif valor_compra >= 100.00 and valor_compra <= 300.00:
        # Se a condição for verdadeira, aplica o desconto de 10% (multiplica por 0.10)
        desconto = valor_compra * 0.10
        
    # O 'else' é executado apenas se nenhuma das condições anteriores for verdadeira.
    # Neste caso, será para compras acima de 300.
    else:
        # Aplica o desconto de 15% (multiplica por 0.15)
        desconto = valor_compra * 0.15
        
    # Calcula o valor final subtraindo o valor do desconto do valor original da compra
    valor_final = valor_compra - desconto
    
    # Exibe os resultados na tela.
    # O ':,.2f' é uma formatação que coloca o ponto de milhar e limita a 2 casas decimais (ex: 1.250.50)
    print("-" * 30)
    print(f"Valor original: R$ {valor_compra:,.2f}")
    print(f"Desconto aplicado: R$ {desconto:,.2f}")
    print(f"Valor final a pagar: R$ {valor_final:,.2f}")

# Verifica se o arquivo está sendo executado diretamente (e não apenas importado por outro arquivo)
# Isso é uma boa prática em Python.
if __name__ == "__main__":
    
    # Chama a função para iniciar o programa
    calcular_compra()
