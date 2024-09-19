import requests
import mysql.connector  # ou outra biblioteca de conexão com banco de dados (ex: psycopg2 para PostgreSQL)

# Função para obter a cotação do dólar
def obter_cotacao_dolar():
    # URL da API de cotação
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"

    # Faz a requisição GET para a API
    response = requests.get(url)

    # Verifica se a resposta foi bem-sucedida
    if response.status_code == 200:
        dados = response.json()
        # Extração da cotação do dólar (chave 'high')
        cotacao_dolar = float(dados['USDBRL']['high'])
        print(f"Cotação do dólar obtida: {cotacao_dolar}")
        return cotacao_dolar
    else:
        print(f"Erro ao obter a cotação: {response.status_code}")
        return None

# Função para atualizar o valor do dólar no banco de dados
def atualizar_preco_dolar_no_banco(cotacao_dolar, produto_id):
    try:
        # Conectar ao banco de dados (ajuste os parâmetros conforme o seu banco)
        conexao = mysql.connector.connect(
             host='localhost',
            port='3306',
            user='root',
            password='',
            database='Banco'
        )
        
        cursor = conexao.cursor()

        # SQL para atualizar o valor do dólar em um produto específico
        sql = "UPDATE produto SET preco_dolar = %s WHERE id = %s"
        valores = (cotacao_dolar, produto_id)

        # Executa o comando SQL
        cursor.execute(sql, valores)

        # Confirma as alterações
        conexao.commit()

        print(f"Preço do dólar atualizado para o produto com ID {produto_id}: {cotacao_dolar}")

    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ou atualizar o banco de dados: {erro}")

    finally:
        # Fecha o cursor e a conexão com o banco de dados
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def main():
    
    cotacao_dolar = obter_cotacao_dolar()

    
    if cotacao_dolar:
        
        produto_id = 1
        atualizar_preco_dolar_no_banco(cotacao_dolar, produto_id)
        produto_id = 2
        atualizar_preco_dolar_no_banco(cotacao_dolar, produto_id)
        produto_id = 3
        atualizar_preco_dolar_no_banco(cotacao_dolar, produto_id)

if __name__ == "__main__":
    main()
