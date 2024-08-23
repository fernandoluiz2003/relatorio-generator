import logging
import pyautogui
from time import sleep

from ezNavigator.webdriver_manager import WebDriverManager
from errors.captcha_error          import CaptchaException
from errors.blocked_access_error   import BlockedAccessException

from functions.cnpj_funcs import (
    cnpj_cleaner, 
    cnpj_finder,
    get_cnpj,
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    logging.info(
        "NOTE: TO WORK PROPERLY THE RECOMMENDED RESOLUTION IS 1366x768"
    )
    
    company_cnpjs = get_cnpj('./empresas.txt')
    company_cnpjs = cnpj_cleaner(company_cnpjs)
    
    url = r'https://cav.receita.fazenda.gov.br/autenticacao/login'
    
    navigator = WebDriverManager()
    driver = navigator.get_driver(
        driver_path = './browser/chromedriver.exe'
    )
    
    driver.maximize_window()
    driver.get(url)
    
    sleep(5)
    login_govbr = navigator.search_by_element(
        driver, 'xpath', '/html/body/div[2]/div/div[2]/div/form/div[2]/p[2]/input'
    )
    login_govbr.click()
    
    sleep(10)
    login_cert = navigator.search_by_element(
        driver, 'xpath', '/html/body/div[1]/main/form/div[1]/div[6]/button'
    )
    login_cert.click()

    cert = navigator.find_img(
        './images/certificado.png', search_time = 5,
    )
    
    if not(cert, tuple):
        driver.quit()
        raise CaptchaException("Captcha appeared and was not solved")
    
    confirm_cert = navigator.find_img(
        './images/confirm_cert.png', search_time = 5, grayscale = True
    )
    
    if not(cert, tuple):
        driver.quit()
        raise pyautogui.ImageNotFoundException()
    
    pyautogui.click(confirm_cert)
    
    if "Error/Erro" in driver.current_url:
        driver.quit()
        raise BlockedAccessException("Many people connected!") 
    
    sleep(5)
    driver.get(r'https://cav.receita.fazenda.gov.br/ecac/Aplicacao.aspx?id=2&origem=menu')
    driver.implicitly_wait(10)
    
    for cnpj in company_cnpjs:
        perfil_information = navigator.search_by_element(
            driver, 'xpath', '/html/body/div[2]/div[1]'
        )
        
        perfil_cnpjs = cnpj_finder(perfil_information.txt)
        
    
    sleep(5)
    safe_exit = navigator.search_by_element(
        driver, 'xpath', '/html/body/div[2]/a[3]/span'
    )
    safe_exit.click()
    
    sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()
