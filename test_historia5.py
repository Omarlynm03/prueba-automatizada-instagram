import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configuración del WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar sin abrir la ventana del navegador
driver = webdriver.Chrome(service=Service('path_to_chromedriver'), options=chrome_options)

def test_editar_perfil():
    try:
        # 1. Abrir Instagram e iniciar sesión
        driver.get("https://www.instagram.com")
        time.sleep(2)

        # Iniciar sesión con las credenciales proporcionadas
        driver.find_element(By.NAME, "username").send_keys("mykemex03")
        driver.find_element(By.NAME, "password").send_keys("aomb0703")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)  # Esperamos a que cargue la página después del login

        # 2. Acceder a la configuración del perfil
        icono_perfil = driver.find_element(By.XPATH, "//span[@aria-label='Perfil']")
        icono_perfil.click()
        time.sleep(2)

        # 3. Acceder a la opción de editar perfil
        boton_editar = driver.find_element(By.XPATH, "//button[text()='Editar perfil']")
        boton_editar.click()
        time.sleep(2)

        # 4. Modificar algunos campos del perfil (nombre y biografía)
        nombre_input = driver.find_element(By.NAME, "username")
        biografia_input = driver.find_element(By.NAME, "biography")

        # Modificar los campos con nuevos valores
        nuevo_nombre = "Nuevo Nombre"
        nueva_biografia = "Esta es una biografía de prueba."

        nombre_input.clear()  # Limpiar el campo del nombre
        nombre_input.send_keys(nuevo_nombre)  # Ingresar nuevo nombre

        biografia_input.clear()  # Limpiar la biografía
        biografia_input.send_keys(nueva_biografia)  # Ingresar nueva biografía

        # 5. Guardar los cambios
        guardar_boton = driver.find_element(By.XPATH, "//button[contains(text(), 'Enviar')]")
        guardar_boton.click()
        time.sleep(3)  # Esperamos para que los cambios se guarden

        # 6. Verificar que los cambios se han reflejado
        # Volver al perfil para verificar que los cambios se guardaron
        icono_perfil.click()
        time.sleep(2)

        # Verificar el nombre y la biografía actualizados
        nombre_reflejado = driver.find_element(By.XPATH, "//h1[@class='_7UhW9   fKFBl yUEEX   KV-D4t q5bIY']")
        biografia_reflejada = driver.find_element(By.XPATH, "//div[@class='-vDIg']")

        assert nuevo_nombre in nombre_reflejado.text, "El nombre no se actualizó correctamente."
        assert nueva_biografia in biografia_reflejada.text, "La biografía no se actualizó correctamente."

        print("Los cambios de perfil fueron guardados y reflejados correctamente.")

        # 7. Caso de campo obligatorio vacío
        # Dejar el campo de nombre vacío
        nombre_input.clear()
        biografia_input.clear()

        guardar_boton.click()
        time.sleep(2)

        # Verificar si aparece el mensaje de error por campo obligatorio vacío
        error_campo_vacio = driver.find_elements(By.XPATH, "//p[contains(text(), 'Por favor complete todos los campos obligatorios.')]")
        assert len(error_campo_vacio) > 0, "No se mostró el mensaje de campo obligatorio vacío."

        print("El mensaje 'Por favor complete todos los campos obligatorios.' fue mostrado correctamente.")

        # 8. Caso de error al guardar los cambios
        # Simulamos un error con la actualización de perfil (esto dependería del comportamiento real de Instagram en caso de error)
        nombre_input.send_keys(nuevo_nombre)
        biografia_input.send_keys(nueva_biografia)
        
        # Simulamos un error en el guardado (no es real, solo un ejemplo)
        driver.execute_script("arguments[0].click();", guardar_boton)  # Hacemos clic manualmente para simular el error
        time.sleep(2)

        # Verificar si aparece el mensaje de error al guardar los cambios
        error_guardar = driver.find_elements(By.XPATH, "//div[contains(text(), 'Error al guardar los cambios.')]")
        assert len(error_guardar) > 0, "No se mostró el mensaje de error al guardar los cambios."

        print("El mensaje 'Error al guardar los cambios. Inténtelo nuevamente.' fue mostrado correctamente.")
    
    except Exception as e:
        print(f"Hubo un error en la prueba: {e}")
    
    finally:
        driver.quit()

# Ejecutar la prueba
test_editar_perfil()
