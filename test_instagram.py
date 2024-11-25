from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login():
    try:
        # Configurar el navegador
        print("Iniciando el navegador...")
        driver = webdriver.Chrome()  
        driver.maximize_window()

        # Navegar a la página de inicio de Instagram
        print("Navegando a Instagram...")
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)  # Esperar a que la página cargue

        # Localizar elementos de inicio de sesión
        print("Buscando campos de usuario y contraseña...")
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")

        # Ingresar credenciales
        print("Ingresando credenciales...")
        username.send_keys("mykemex03")  
        password.send_keys("aomb0703")
        password.send_keys(Keys.RETURN)

        time.sleep(5)  # Esperar para verificar el resultado

        # Validar si el inicio de sesión fue exitoso
        try:
            assert "login" not in driver.current_url  # URL debe cambiar tras inicio exitoso
            print("Inicio de sesión exitoso")
        except AssertionError:
            print("Inicio de sesión fallido")

        # Tomar una captura de pantalla
        driver.save_screenshot("login_result.png")

        # Cerrar el navegador
        driver.quit()
    except Exception as e:
        print(f"Ocurrió un error: {e}")

test_login()
