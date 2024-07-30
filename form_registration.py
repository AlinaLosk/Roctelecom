"""Воспроизведение тестов:"""
# python -m pytest -v --driver Chrome --driver-path C:\Chromedriver/chromedriver.exe form_registration.py


from cgitb import text
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='module')
def driver():
    service = Service('C:\PycharmProjects\Rostelecom_tests\Rostelecom/tests/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


URL = (
    'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https'
    '://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=b0a423ab-3aed-4b3b-9414'
    '-707bda611620')


# Негативный сценарий:

# 1
def test_invalid_pass_registration(driver):
    # Перейти на страницу авторизации
    driver.get(URL)

    # Дождаться элемент вкладки "Телефон"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))

    # Выбрать вкладку "Телефон"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()

    # Дождаться появления элемента "Зарегистрироваться"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="kc-register"]')))

    # Выбрать ссылку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(3)

    # Заполнить личные данные в полях регистрации
    # Ввести имя пользователя
    driver.find_element(By.XPATH,
                        '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('Семен')

    # Заполнить поле "Фамилия"
    driver.find_element(By.XPATH,
                        '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys('Ли-Про')
    # Выбор региона оставить по умолчанию г. Москва

    # Ввести невалидный email
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('000000000000@email.ru')
    time.sleep(3)

    # Ввести  пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Ad456')
    time.sleep(3)

    # Подтвердить пароль
    driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('Ad456')
    time.sleep(5)

    # Нажать кнопку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button').click()
    time.sleep(5)

    # Проверка, что регистрация не успешна.
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span').text == 'Длина пароля должна быть не менее 8 символов'
    time.sleep(5)


# 2
def test_invalid_email_registration(driver):
    # Перейти на страницу авторизации
    driver.get(URL)
    time.sleep(3)

    # Дождаться элемент вкладки "Телефон"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))
    # Выбрать "Телефон"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()

    # Дождаться появления элемента "Зарегистрироваться"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="kc-register"]')))
    # Выбрать ссылку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(3)

    # Заполнить личные данные в полях регистрации
    # Ввести имя пользователя
    driver.find_element(By.XPATH,
                        '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('Семен')

    # Заполнить поле "Фамилия"
    driver.find_element(By.XPATH,
                        '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys('Ли-Про')
    # Выбор региона оставить по умолчанию г. Москва

    # Ввести нвалидный email
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('45654ssd')
    time.sleep(3)

    # Ввести пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Bey-Jq4-5rQ-Qss')
    time.sleep(5)
    # Проверка, что регистрация не успешна.
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/span').text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'


# 3
def test_invalid_name_registration(driver):
    # Перейти на страницу авторизации
    driver.get(URL)
    time.sleep(3)

    # Дождаться элемент вкладки "Телефон"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))
    # Выбрать вкладку "Телефон"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()

    # Дождаться появления элемента "Зарегистрироваться"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="kc-register"]')))
    # Выбрать ссылку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(3)

    # Заполнить личные данные в полях регистрации
    # Ввести имя
    driver.find_element(By.XPATH,
                        '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('565jkl')

    # Заполнить поле "Фамилия"
    driver.find_element(By.XPATH,
                        '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys('Ли-Про')
    # Выбор региона оставить по умолчанию г. Москва

    # Ввести мобильный телефон
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('79672405986')
    time.sleep(3)

    # Ввести пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Bey-Jq4-5rQ-Qss')
    # Проверка не успешной авторизации пользователя
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span').text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


# 4
def test_invalid_name_and_lastName_registration(driver):
    # Перейти на страницу авторизации
    driver.get(URL)
    time.sleep(3)

    # Дождаться элемент вкладки "Телефон"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))
    # Выбрать вкладку "Телефон"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()

    # Дождаться появления элемента "Зарегистрироваться"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="kc-register"]')))
    # Выбрать ссылку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(3)

    # Заполнить личные данные в полях регистрации
    # Ввести невалидные данные в поле "Имя"
    driver.find_element(By.XPATH,
                        '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('565jkl')

    # Заполнить поле Фамилия невалидными
    driver.find_element(By.XPATH,
                        '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys('-55犯务554 kj')
    # Выбор региона оставить по умолчанию г. Москва

    # Ввести мобильный телефон
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('79672405986')
    time.sleep(3)

    # Ввести пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Bey-Jq4-5rQ-Qss')
    # Проверка не успешной регистрации пользователя.
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span').text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


# 5
def test_empty_field_registration(driver):
    # Перейти на страницу авторизации
    driver.get(URL)
    time.sleep(3)

    # Дождаться элемент вкладки "Телефон"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))
    # Выбрать вкладку "Телефон"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()

    # Дождаться появления элемента "Зарегистрироваться"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="kc-register"]')))
    # Выбрать ссылку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(3)

    # Оставить все поля регистрации для регистрации пустыми
    # Нажать кнопку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button').click()
    # Проверка не успешной регистрации на сайте
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span').text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/span').text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span').text == 'Длина пароля должна быть не менее 8 символов'


# 6
def test_XSS_registration(driver):
    # Перейти на страницу авторизации
    driver.get(URL)
    time.sleep(3)

    # Дождаться элемент вкладки "Телефон"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))
    # Выбрать вкладку "Телефон"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()

    # Дождаться появления элемента "Зарегистрироваться"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="kc-register"]')))
    # Выбрать ссылку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(3)

    # Заполнить личные данные в полях регистрации
    # Ввести имя
    driver.find_element(By.XPATH,
                        '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys(
        'Семен<script>alert()</script>')

    # Заполнить поле "Фамилия"
    driver.find_element(By.XPATH,
                        '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys(
        '<h1>Hello</h1>')

    # Выбор региона оставить по умолчанию г. Москва
    # Ввести мобильный телефон
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('<script>alert(123)</script>')
    time.sleep(3)

    # Ввести пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('="<script>alert()</script>">')

    # Заполнить поле "Подтверждение пароля"
    driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('="<script>alert()</script>">')

    # Нажать кнопку "Зареегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    # Проверка безопастности
    assert driver.find_element(By.TAG_NAME,
                               'h2').text != 'Ваш запрос был отклонен из соображений безопасности. Обратитесь в техническую поддержку по номеру 8 (800) 1000 800.'

# 7
def password_with_hieroglyphs(driver):
    # Перейти на страницу авторизации
    driver.get(URL)
    # Дождаться элемент вкладки "Телефон"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))

    # Выбрать "Телефон"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()

    # Дождаться появления элемента "Зарегистрироваться"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="kc-register"]')))

    # Выбрать ссылку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(3)

    # Заполнить личные данные в полях регистрации
    # Ввести имя
    driver.find_element(By.XPATH,
                        '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys(
        'Семен')

    # Заполнить поле "Фамилия"
    driver.find_element(By.XPATH,
                        '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys(
        'Ли-Про')
    # Выбор региона оставить по умолчанию г. Москва
    # Ввести невалидный email
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('000000000000@email.ru')
    time.sleep(5)

    # Ввести  пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('犯外处冬鸟务包饥主市立冯玄闪兰')
    time.sleep(5)

    # Подтвердить пароль
    driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('犯外处冬鸟务包饥主市立冯玄闪兰')
    time.sleep(5)

    # Нажать кнопку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button').click()
    time.sleep(5)
    # Проверка, что регистрация не успешна
    assert driver.find_element(By.XPATH,'//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span').text == 'Пароль должен содержать только латинские буквы'

# Позитивный сценарий:
# 8
def test_registration_by_phone(driver):
    # Перейти на страницу авторизации
    driver.get(URL)

    # Дождаться появления вкладки "Телефон"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))

    # Нажать на ссылку "Зарегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="kc-register"]').click()
    time.sleep(3)

    # Заполнить поле "Имя"
    driver.find_element(By.XPATH,
                        '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys(
        'Мальвина')

    # Заполнить поле "Фамилия"
    driver.find_element(By.XPATH,
                        '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys(
        'Петрова')

    # Заполнить поле "Email или телефон"
    driver.find_element(By.XPATH, '//*[@id="address"]').send_keys('79635696969')

    # Заполнить поле "Пароль"
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Bey-!!!-5rQ-Qss')

    # Заполнить поле "Подтверждение пароля"
    driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('Bey-!!!-5rQ-Qss')

    # Нажать кнопку "Зареегистрироваться"
    driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()

    # Дождаться появления формы ввода СМС-кода
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="otp"]/div[1]/div[1]/input')))

    # Ввести валидный СМС-код
    # Задержка для ввода СМС-код вручную
    time.sleep(25)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="id_app_lk_b2c"]/div[2]/span')))
    assert driver.find_element(By.XPATH, '//*[@id="id_app_lk_b2c"]/div[2]/span').text == 'Личный кабинет'

    # Нажать кнопку "Выйти"
    driver.find_element(By.XPATH, '//*[@id="logout-btn"]').click()
    time.sleep(5)
