import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configuración del WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Opcional: para ejecutar sin abrir la ventana del navegador
driver = webdriver.Chrome(service=Service('path_to_chromedriver'), options=chrome_options)

def test_ver_notificaciones():
    try:
        # 1. Abrir Instagram e iniciar sesión
        driver.get("https://www.instagram.com")
        time.sleep(2)

        # Iniciar sesión con las credenciales proporcionadas
        driver.find_element(By.NAME, "username").send_keys("mykemex03")
        driver.find_element(By.NAME, "password").send_keys("aomb0703")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)  # Esperamos un poco a que cargue la página después del login

        # 2. Acceder a la sección de notificaciones desde la barra superior
        notificaciones_icono = driver.find_element(By.XPATH, "//span[@aria-label='Actividad']")  # Icono de actividad (notificaciones)
        notificaciones_icono.click()
        time.sleep(3)  # Esperamos para que carguen las notificaciones

        # 3. Verificar que las notificaciones están visibles (likes, comentarios, seguidores)
        try:
            # Verificar que haya notificaciones
            notificaciones = driver.find_elements(By.XPATH, "//div[@class='Mr508']")
            if len(notificaciones) > 0:
                print(f"Se encontraron {len(notificaciones)} notificaciones.")
                for notificacion in notificaciones[:5]:  # Limitar a las primeras 5 notificaciones
                    print(notificacion.text)
            else:
                # Si no hay notificaciones
                no_notificaciones = driver.find_elements(By.XPATH, "//div[contains(text(), 'No tienes nuevas notificaciones.')]")
                assert len(no_notificaciones) > 0, "No se mostró el mensaje de 'No tienes nuevas notificaciones.'"
                print("El mensaje 'No tienes nuevas notificaciones.' fue mostrado correctamente.")
        
        except Exception as e:
            # Si ocurre un error al cargar las notificaciones
            error_carga = driver.find_elements(By.XPATH, "//div[contains(text(), 'Error al cargar las notificaciones.')]")
            assert len(error_carga) > 0, "No se mostró el mensaje de error al cargar las notificaciones."
            print("El mensaje 'Error al cargar las notificaciones.' fue mostrado correctamente.")
    
    except Exception as e:
        print(f"Hubo un error en la prueba: {e}")
    
    finally:
        driver.quit()

# Ejecutar la prueba
test_ver_notificaciones()
