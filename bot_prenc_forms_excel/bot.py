# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()
    bot.browse("https://docs.google.com/forms/d/e/1FAIpQLSfDzqYUoNJMY09vo4o9NNmwWWzgoNHMX3on6wctH2z3rQkB1A/viewform")

    # Implement here your logic...
    if not bot.find("nome", matching=0.97, waiting_time=10000):
        not_found("nome")
    bot.click_relative(30, 96)
    bot.paste("Rodrigo Lima de Souza")

    if not bot.find("genero", matching=0.97, waiting_time=10000):
        not_found("genero")
    bot.click_relative(18, 86)
    bot.paste("Rodrigo Lima de Souza")

    if not bot.find("email", matching=0.97, waiting_time=10000):
        not_found("email")
    bot.click_relative(21, 99)
    bot.paste("Rodrigo@Souza.com")
    
    if not bot.find("departamento", matching=0.97, waiting_time=10000):
        not_found("departamento")
    bot.click()
    bot.paste("engenharia")

    if not bot.find("endereco", matching=0.97, waiting_time=10000):
        not_found("endereco")
    bot.click_relative(38, 98)
    bot.paste("cidade nova")

    if not bot.find("cpf", matching=0.97, waiting_time=10000):
        not_found("cpf")
    bot.click_relative(34, 95)
    bot.paste("000.000.000-66")

    if not bot.find("rg", matching=0.97, waiting_time=10000):
        not_found("rg")
    bot.click_relative(31, 95)
    bot.paste("55555555")

    if not bot.find("turno", matching=0.97, waiting_time=10000):
        not_found("turno")
    bot.click_relative(16, 85)

    # if not bot.find("enviar", matching=0.97, waiting_time=10000):
    #     not_found("enviar")
    # bot.click()
    

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()