from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    # Usamos un ChromeDriver instalado previamente para evitar demoras
    servicio = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")  # Evita detección de bot
    options.add_argument("--headless=new")  # Ejecuta en segundo plano (quítalo si quieres ver la ventana)
    
    # Inicializamos el driver con las opciones optimizadas
    driver = webdriver.Chrome(service=servicio, options=options)
    driver.implicitly_wait(5)  # Espera implícita para que cargue rápido
    
    # Carga la página
    driver.get("https://wargameserver3.evilgrog.com/profile/index/id/109336/i/7YxS1WI5xsE3DelGY9s6LfrJJeoNhGkG/h/4ccbe5f7f583cd1f2fdf817d147a59e3/t/1742246967/linkDefense/9cdf7ddd744d73c6ac6d315ee820f3ddad7607ce")

    try:
        # Esperamos a que el botón esté presente y hacemos clic
        boton_ataque = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btnFury"))
        )
        boton_ataque.click()
        print("✅ ¡Botón 'Ataque' clickeado con éxito!")
    except Exception as e:
        print(f"⚠️ Error al hacer clic en el botón: {e}")

    time.sleep(3)  # Espera corta para ver la acción antes de cerrar
    driver.quit()  # Cerramos el navegador

if __name__ == "__main__":
    main()
