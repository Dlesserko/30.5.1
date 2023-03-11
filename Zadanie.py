import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://petfriends.skillfactory.ru/new_user")
    driver.find_element_by_id("email").send_keys("darcon@list.ru")
    driver.find_element_by_id("pass").send_keys("Dellin5000")
    driver.find_element_by_css_selector("button[type='submit']").click()
    time.sleep(3)
    
    # переходим на страницу со списком питомцев
    driver.get("https://petfriends.skillfactory.ru/my_pets")
    
    # Проверяем наличие всех питомцев
    pet_cards = driver.find_elements_by_css_selector('.card')
    assert len(pet_cards) == 6, "Количество питомцев не соответствует ожидаемому"
    
    # Проверяем наличие фото хотя бы у половины питомцев
    photos = driver.find_elements_by_css_selector('.card-img-top')
    assert len(photos) >= 3, "Фото не у половины питомцев"
    
    # Проверяем, что у всех питомцев есть имя, возраст и порода
    pet_info = driver.find_elements_by_css_selector('.card-title')
    for info in pet_info:
        assert info.text != "", "Отсутствует имя питомца"
    pet_info = driver.find_elements_by_css_selector('.card-text')
    for info in pet_info:
        assert info.text != "", "Отсутствует возраст и порода питомца"
    
    # Проверяем, что все имена разные
    pet_names = driver.find_elements_by_css_selector('.card-title')
    names = []
    for name in pet_names:
        assert name.text not in names, "У питомцев одинаковые имена"
        names.append(name.text)
    
    # Проверяем, что нет повторяющихся питомцев
    pet_breeds = driver.find_elements_by_css_selector('.card-subtitle')
    breeds = []
    for breed in pet_breeds:
        assert breed.text not in breeds, "На странице есть повторяющиеся питомцы"
        breeds.append(breed.text)

finally:
    driver.quit()
