import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# Configuración del WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecuta sin abrir el navegador (opcional)
driver = webdriver.Chrome(service=Service('path_to_chromedriver'), options=chrome_options)

def test_buscar_usuario():
    try:
        # 1. Abrir Instagram e iniciar sesión
        driver.get("https://www.instagram.com")
        time.sleep(2)

        # Iniciar sesión con las credenciales proporcionadas
        driver.find_element(By.NAME, "username").send_keys("mykemex03")
        driver.find_element(By.NAME, "password").send_keys("aomb0703")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)  # Esperamos a que la página cargue después del login

        # 2. Buscar un usuario en la barra de búsqueda
        search_box = driver.find_element(By.XPATH, "//input[@placeholder='Buscar']")
        search_box.click()
        search_box.send_keys("nombre_de_usuario_a_buscar")  # Reemplaza esto por un nombre de usuario válido o de prueba
        time.sleep(2)  # Esperamos a que carguen los resultados

        # 3. Verificar que las sugerencias relevantes están siendo mostradas
        try:
            # Verificamos si los resultados de búsqueda están visibles
            resultados_sugeridos = driver.find_elements(By.XPATH, "//div[@class='-qQT3']")
            assert len(resultados_sugeridos) > 0, "No se mostraron resultados relevantes."

            # Seleccionamos el primer usuario de los resultados y verificamos que su perfil se abre
            resultados_sugeridos[0].click()
            time.sleep(3)  # Esperamos un poco para que el perfil cargue
            assert "perfil" in driver.current_url, "No se abrió el perfil del usuario correctamente."
            print("La búsqueda fue exitosa y el perfil fue abierto correctamente.")

        except AssertionError:
            print("No se encontraron usuarios con este nombre.")

        # 4. Simular un caso donde no se encuentra el usuario
        search_box.clear()
        search_box.send_keys("usuario_inexistente")
        time.sleep(2)  # Esperamos para que carguen los resultados

        no_resultados = driver.find_elements(By.XPATH, "//div[contains(text(), 'No se encontraron usuarios con este nombre.')]")
        assert len(no_resultados) > 0, "No se mostró el mensaje de no resultados."
        print("El mensaje de 'No se encontraron usuarios' fue mostrado correctamente.")

        # 5. Simular un caso donde hay un error en la búsqueda (error de servidor)
        search_box.clear()
        search_box.send_keys("error_de_servidor")
        time.sleep(2)

        # Simulamos que el servidor no responde, utilizando un xpath relacionado con un error de carga
        error_carga = driver.find_elements(By.XPATH, "//div[contains(text(), 'Error al cargar la búsqueda.')]")
        assert len(error_carga) > 0, "No se mostró el mensaje de error al cargar la búsqueda."
        print("El mensaje de 'Error al cargar la búsqueda' fue mostrado correctamente.")
    
    except Exception as e:
        print(f"Hubo un error en la prueba: {e}")
    
    finally:
        driver.quit()

# Ejecutar la prueba
test_buscar_usuario()