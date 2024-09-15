import requests
from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager

# Função para buscar o produto na Amazon e pegar o preço em dólar
def pesquisar_produto(bot, produto):
    # Acessa o site da Amazon
    bot.browse("https://www.amazon.com")
    bot.wait(2000)

    # Aguarda até que a barra de pesquisa esteja disponível
    while True:
        search_box = bot.find_elements('//*[@id="twotabsearchtextbox"]', By.XPATH)
        if search_box:  # Verifica se a caixa de pesquisa foi encontrada
            break
        bot.wait(1000)
        print('Carregando...')

    # Encontra a barra de pesquisa, insere o termo "Kindle" e realiza a busca
    search_box[0].send_keys(produto)
    bot.enter()
    bot.wait(2000)
    
    # Aguarda até que o preço esteja disponível
    while True:
        preco_element = bot.find_elements('//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/span/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div[1]/a/span', By.XPATH)
        if preco_element:  # Verifica se o preço foi encontrado
            break
        bot.wait(1000)
        print('Aguardando preço...')

    try:
        # Captura o valor do preço como texto
        preco_texto = preco_element[0].text  # Exemplo: "$244\n97"
        
        # Remove o símbolo de dólar, quebras de linha e espaços, e junta os números
        preco_texto = preco_texto.replace("$", "").replace("\n", "").replace(",", "").strip()

        # Converte para float e ajusta para ter duas casas decimais
        preco_dolar = float(preco_texto) / 100  # Dividir por 100 para considerar as casas decimais corretas
        print(f"O preço do produto é: {preco_dolar:.2f} USD")
        return preco_dolar
    except Exception as ex:
        print(f"Erro ao capturar o preço: {ex}")
        return None

# Função para obter a taxa de câmbio do Dólar para Real via API
def obter_taxa_dolar_real():
    try:
        # Faz a requisição GET para a API da AwesomeAPI
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        response = requests.get(url)
        data = response.json()
        
        # Captura a taxa de câmbio
        taxa_dolar_real = float(data['USDBRL']['bid'])
        print(f"A taxa de câmbio USD/BRL é: {taxa_dolar_real}")
        return taxa_dolar_real
    except Exception as ex:
        print(f"Erro ao obter a taxa de câmbio: {ex}")
        return None
    
def main():
    bot = WebBot()

    # Configuração do navegador
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    try:
        # Realiza a pesquisa do produto "Kindle" na Amazon
        produto = "Kindle"
        preco_dolar = pesquisar_produto(bot, produto)
        bot.wait(2000)

        if preco_dolar:
            # Obtém a taxa de câmbio
            taxa_dolar_real = obter_taxa_dolar_real()

            if taxa_dolar_real:
                # Converte o preço para reais
                preco_reais = preco_dolar * taxa_dolar_real

                # Formata o preço em reais com separador de milhar
                preco_reais_formatado = f"{preco_reais:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                
                print(f"Nome do Produto: {produto}")
                print(f"Valor em Dólar: {preco_dolar:.2f} USD")
                print(f"Valor em Real: {preco_reais_formatado} BRL")
    except Exception as ex:
        print(ex)
        bot.save_screenshot('erro.png')
    finally:
        bot.stop_browser()

if __name__ == '__main__':
    main()
