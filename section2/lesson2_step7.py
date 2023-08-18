import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

link = "http://suninjuly.github.io/file_input.html"


try:
    driver.get(link)

     
    current_dir = os.path.abspath(os.path.dirname(__file__))    
    # получаем путь к директории текущего исполняемого файла 
    print(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'file.txt')          
    # добавляем к этому пути имя файла 
    print(os.path.abspath(os.path.dirname(__file__)))
    # element.send_keys(file_path)


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла