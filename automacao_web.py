from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()

navegador.get("https://ri.magazineluiza.com.br/")
navegador.find_element(By.XPATH,'//*[@id="Form1"]/div[6]/a').click()
navegador.find_element(By.XPATH,'//*[@id="Form1"]/header/div/div/div/div[1]/button').click()
navegador.find_element(By.XPATH,'//*[@id="heading-mobile-3"]/button').click()
# navegador.find_element(By.XPATH,'//*[@id="collapse-mobile-3"]/div/ul/li[2]/a').click()
# navegador.find_element(By.XPATH,'//*[@id="/yn8cix7XmBHQ2FgNBrtCg=="]').click()


#driver.find_element(By.XPATH,
#xpath

# if __name__ == "__main__":
#    webdriver.Chrome()
