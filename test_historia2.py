from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Ejecutar sin interfaz gráfica
driver = webdriver.Chrome(options=options)

def login_instagram():
    # Acceder a Instagram
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)  # Esperar que la página cargue

    # Ingresar el nombre de usuario y contraseña
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    
    username_field.send_keys("mykemex03")
    password_field.send_keys("aomb0703")
    
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)  # Esperar a que la página cargue después del login

def upload_photo():
    # Abrir la página de subida de fotos
    driver.get("https://www.instagram.com/create/details/")
    time.sleep(3)

    # Seleccionar el archivo de la foto
    upload_button = driver.find_element(By.XPATH, '//*[contains(@aria-label, "Imagen o video")]')
    upload_button.send_keys("Rob.png.png")  # Ruta al archivo de la imagen
    time.sleep(3)  # Esperar que el archivo se cargue

    # Añadir descripción
    description_field = driver.find_element(By.XPATH, '//textarea[@aria-label="Escribe una leyenda..."]')
    description_field.send_keys("Una hermosa foto para compartir con mis seguidores!")
    
    # Etiquetas (opcional)
    description_field.send_keys(" #momento #instagood")

    # Intentar publicar
    try:
        publish_button = driver.find_element(By.XPATH, '//button[text()="Compartir"]')
        
        # Verificar si el botón está habilitado
        if publish_button.is_enabled():
            publish_button.click()
            print("Foto publicada correctamente.")
        else:
            print("Error: El botón 'Publicar' está deshabilitado.")
    
    except Exception as e:
        print(f"Error al subir la foto. Inténtelo nuevamente. Error: {e}")

def verify_post():
    # Verificar si la foto está en el feed personal (revisar que se ha publicado correctamente)
    time.sleep(5)  # Esperar a que la publicación aparezca
    driver.get("https://www.instagram.com/mykemex03/")
    time.sleep(3)

    try:
        # Buscar la foto en el feed
        posts = driver.find_elements(By.CSS_SELECTOR, 'article img')
        if posts:
            print("La foto se ha subido correctamente al feed.")
        else:
            print("La foto no se ha publicado.")
    except Exception as e:
        print(f"Error al verificar la publicación: {e}")

def main():
    try:
        login_instagram()
        upload_photo()
        verify_post()
    finally:
        driver.quit()  # Cerrar el navegador

if __name__ == "__main__":
    main()