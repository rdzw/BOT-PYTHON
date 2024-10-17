# Import for the Web Bot
from botcity.web import WebBot, Browser, By
# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False
from webdriver_manager.chrome import ChromeDriverManager

'''
Exemplo de implementação com o conceito de HERANÇA
um dos pilares do POO
'''
class Bot(WebBot):

    def configura_bot(self):
        # Configure whether or not to run on headless mode
        self.headless = False
        # Set the Browser to Chrome
        self.browser = Browser.CHROME
        # Set the WebDriver path
        self.driver_path = ChromeDriverManager().install()

    def action(self, execution=None):
        # Runner passes the server url, the id of the task being executed,
        # the access token and the parameters that this task receives (when applicable).
        maestro = BotMaestroSDK.from_sys_args()
        # Fetch the BotExecution with details from the task, including parameters
        execution = maestro.get_execution()

        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}")

        # Configurar o bot
        self.configura_bot()
        # Abrir o site definido
        self.url_site()

    def url_site(self, url="http://127.0.0.1:5500/form.html"):
        try:
            # Open the provided URL
            self.browse(url)
            print(f"Site {url} acessado com sucesso.")
        except Exception as ex:
            print('Erro ao acessar o site:', ex)
            self.save_screenshot('erro.png')

        finally:
            # Wait 3 seconds before closing
            self.wait(3000)
            # Finish and clean up the Web Browser
            self.stop_browser()

            # Uncomment to mark this task as finished on BotMaestro
            # maestro.finish_task(
            #     task_id=execution.task_id,
            #     status=AutomationTaskFinishStatus.SUCCESS,
            #     message="Task Finished OK."
            # )

    def not_found(self, label):
        print(f"Element not found: {label}")

if __name__ == '__main__':
    Bot.main()
