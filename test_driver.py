from selenium import webdriver

driver = webdriver.Chrome()  
driver.get("https://www.google.com")
print("El navegador se abrió correctamente.")
driver.quit()