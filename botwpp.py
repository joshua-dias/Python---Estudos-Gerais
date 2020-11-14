from selenium import webdriver
import time

class BotWhatsapp:
    def __init__ (self):
        # Preencher a mensagem à ser enviada
        self.mensagem = "Mensagem de teste"
        # Preencher o nome da pessoa ou grupo abaixo(Sem limite de pessoas)
        self.destinatario = ['João']
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        # Preencher o caminho onde está seu chromedriver.
        self.driver = webdriver.Chrome(executable_path =r'C:\Users\~stan twice\Desktop\Rep Josh\chromedriver.exe')
    
    def EnviarMensagem(self): 
        # Acessando o Whatsapp
        self.driver.get('https://web.whatsapp.com')
        time.sleep(20)
        # Criei um for pois o mesmo pode fazer acesso à quantas pessoas e/ou grupos necessários.
        for grupo in self.destinatario: 
            grupo = self.driver.find_element_by_xpath(f"//span[@title = '{grupo}']")
            time.sleep(3)
            grupo.click()
            # Momento de clicar na Caixa de Texto | Necessário validar o nome da classe abaixo:
            caixadetexto = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            caixadetexto.click()
            caixadetexto.send_keys(self.mensagem)
            # Momento de clicar no botão de enviar.
            enviar = self.driver.find_element_by_xpath(f"//span[@data-icon = 'send']")
            time.sleep(3)
            enviar.click()
            time.sleep(5)

# Chamando o método.
bot = BotWhatsapp()
bot.EnviarMensagem()            