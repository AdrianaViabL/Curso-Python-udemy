"""
automatizando tareafas no navegador
vai precisar acessar o site do python para baixar o
drive do navegador usado para ter a conexao entre a
automatizacao e o navegador
https://sites.google.com/a/chromium.org/chromedriver/downloads

"""
from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.driver_path = './chromedriver'
        self.options = webdriver.ChromeOptions()  # salvando a sessao na mesma pasta que esta sendo executado o script
        self.options.add_argument('user-data-dir=Perfils')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def clica_sign_in(self):
        try:
            # prcurando o nome por extenso pois o botao nao tem ID
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sign_in.click()
        except Exception as e:
            print('Erro clicar sign in: ', e)
            pass

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')

            input_login.send_keys('usuario github')  # vai mandar para o campo o que for digitado aqui
            input_password.send_keys('senha do github')
            sleep(3)
            btn_login.click()

        except Exception as e:
            print('erro no login: ', e)

    def verifica_usuario(self, usuario):
        profile_link = self.chrome.find_element_by_class_name('user-profile-link')
        profile_link_html = profile_link.get_attribute('innterHTML')  #verificando o conteudo dentro do HTML
        assert usuario in profile_link_html  #valida se o usuario esta certo

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details')
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no perfil: ', e)

    def faz_logout(self):
        try:
            perfil = self.chrome.find_element_by_css_selector(
                'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            perfil.click()
        except Exception as e:
            print('Erro ao clicar em logout: ', e)


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')
    chrome.clica_sign_in()
    chrome.faz_login()
    chrome.clica_perfil()
    chrome.verifica_usuario('usuariogithub')
    sleep(3)
    chrome.faz_logout()

    chrome.sair()
