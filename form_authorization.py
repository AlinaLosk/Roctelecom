import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Воспроизвести тесты:
# python -m pytest -v --driver Chrome --driver-path C:\Chromedriver/chromedriver.exe form_authorization.py

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

# Позитивный сценарий:
# 1
def test_phone_authorization(driver):
    # Перейти на страницу авторизации
    driver.get(URL)

    # Дождаться элемента вкладки "Телефон"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))

    # Выбрать вкладку "Телефон"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()

    # Ввести номер мобильного телефона
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('79672405968')

    # Ввести действующий пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Bey-Jq4-5rQ-Qss')

    # Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="id_app_lk_b2c"]/div[2]/span')))
    assert driver.find_element(By.XPATH, '//*[@id="id_app_lk_b2c"]/div[2]/span').text == 'Личный кабинет'

    # Нажать кнопку "Выйти"
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="logout-btn"]').click()

# 2
def test_login_authorization(driver):
    # Перейти на страницу авторизации
    driver.get(URL)

    # Дождаться появления элемента "Логин"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-login"]')))

    # Выбрать вкладку "Логин"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]').click()

    # Ввести логин
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('rtkid_1721572375936')
    time.sleep(5)

    # Ввести пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Bey-Jq4-5rQ-Qss')
    time.sleep(5)

    # Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    time.sleep(3)

    # Проверка, что авторизация прошла успешно
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="id_app_lk_b2c"]/div[2]/span')))
    assert driver.find_element(By.XPATH, '//*[@id="id_app_lk_b2c"]/div[2]/span').text == 'Личный кабинет'

    # Нажать кнопку "Выйти"
    driver.find_element(By.XPATH, '//*[@id="logout-btn"]').click()

# 3
def test_email_authorization(driver):
    # Перейти на страницу авторизации
    driver.get(URL)

    # Дождаться появления элемент "Почта"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-mail"]')))

    # Выбрать вкладку "Почта"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()

    # Ввести почту
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('barmalina90@yandex.ru')
    time.sleep(3)

    # Ввести пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Bey-Jq4-5rQ-Qss')
    time.sleep(3)

    # Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    time.sleep(3)

    # Проверка, что авторизация прошла успешно
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="id_app_lk_b2c"]/div[2]/span')))
    assert driver.find_element(By.XPATH, '//*[@id="id_app_lk_b2c"]/div[2]/span').text == 'Личный кабинет'

    # Нажать кнопку "Выйти"
    driver.find_element(By.XPATH, '//*[@id="logout-btn"]').click()
    time.sleep(5)

# 4
def test_automatic_tab_switching(driver):
    # Перейти на страницу авторизации
    driver.get(URL)

    # Дождаться появления элемент "Почта"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-mail"]')))

    # Выбрать вкладку "Почта"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()

    # Ввести почту
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('79672405968')
    time.sleep(3)

    # Ввести пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Bey-Jq4-5rQ-Qss')

    # Проверка автоматического переключения вкладки
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))
    assert driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').text == 'Телефон'

# Негативный сценарий:
# 5
def test_empty_field_email(driver):
    # Перейти на страницу авторизации
    driver.get(URL)

    # Дождаться появления вкладки "Почта"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-mail"]')))

    # Выбрать вкладку "Почта"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()
    # Оставить поле электронная почта пустым

    # Ввести действующий пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Bey-Jq4-5rQ-Qss')
    time.sleep(3)

    # Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()

    # Проверка, что авторизация прошла не успешно
    assert driver.find_element(By.XPATH, '//*[@id="username-meta"]').text == 'Введите адрес, указанный при регистрации'
    time.sleep(5)

# 6
def test_invalid_email_and_pass(driver):
    # Перейти на страницу авторизации
    driver.get(URL)

    # Дождаться появления вкладки "Почта"
    WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-mail"]')))

    # Выбрать вкладка "Почта"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()

    # Ввести невалидную почту
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('456465dvsdvsvsc fdb@bk.ru')

    # Ввести невалидный пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('bhghhhhhhhhhhhhhggggggggygcfcftfcffffgfc12225')

    # Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    time.sleep(3)

    # Проверка, что авторизация прошла не успешно
    assert driver.find_element(By.XPATH,
                               '//*[@id="form-error-message"]').text == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'

# 7
def test_hieroglyphs_email_and_pass(driver):
    # Перейти на страницу авторизации
    driver.get(URL)

    # Дождаться появления вкладки "Почта"
    WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-mail"]')))

    # Выбрать вкладку "Почта"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]').click()

    # Ввести невалидную почту
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('犯外处冬鸟务包饥主市立冯玄闪兰')

    # Ввести не валидный пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('犯外处冬鸟务包饥主市立冯玄闪兰')

    # Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    time.sleep(3)

    # Проверка, что авторизация прошла не успешно
    assert driver.find_element(By.XPATH,
                               '//*[@id="form-error-message"]').text == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'

# 8
def test_invalid_phone(driver):
    # Перейти на страницу авторизации
    driver.get(URL)
    # Дождаться элемент вкладки "Телефон"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))

    # Выбрать вкладку "Телефон"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()

    # Ввести невалидный номер мобильного телефона
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('0000000000000')

    # Ввести невалидный пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Bey-Jq4-5rQ-Qss')

    # Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    time.sleep(5)

    # Проверка, что авторизация прошла не успешно
    assert driver.find_element(By.XPATH,
                               '//*[@id="form-error-message"]').text == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'

# 9
def test_invalid_phone_and_pass_255symbol(driver):
    # Перейти на страницу авторизации
    driver.get(URL)

    # Дождаться элемент вкладки "Телефон"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-phone"]')))

    # Выбрать "Телефон"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]').click()

    # Ввести номер мобильного телефона
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('0000000000000')

    # Ввести пароль 255 символов
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('hgfgtykiu1235nhjbhgyhgfgtykiu1235nhjbhgyhgf'
                                                                   'gtykiu1235nhjbhgyhgfgtykiu1235nhjbhgyhgfgtykiu1235nhjb'
                                                                   'hgyhgfgtykiu1235nhjbhgyhgfgtykiu1235nhjbhgyhgfgtykiu12'
                                                                   '35nhjbhgyhgfgtykiu1235nhjbhgyhgfgtykiu1235nhjbhgyhgf'
                                                                   'gtykiu1235nhjbhgyhgfgtykiu1235nhjbhgyhgfgtykiu1')

    # Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    time.sleep(5)

    # Проверка, что авторизация прошла не успешно
    assert driver.find_element(By.XPATH,
                               '//*[@id="form-error-message"]').text == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'

# 10
def test_empty_field_login(driver):
    # Перейти на страницу авторизации
    driver.get(URL)
    # Дождаться появления элемента "Логин"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-login"]')))

    # Выбрать вкладку "Логин"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]').click()
    # Поле логин оставить пустым

    # Ввести пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Bey-Jq4-5rQ-Qss')
    time.sleep(3)

    # Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    time.sleep(3)
    # Проверка, что авторизация прошла не успешно
    assert driver.find_element(By.XPATH, '//*[@id="username-meta"]').text == 'Введите логин, указанный при регистрации'

# 11
def test_empty_field_LS(driver):
    # Перейти на страницу авторизации
    driver.get(URL)

    # Дождаться появления элемента "Лицевой счет"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-ls"]')))

    # Выбрать вкладку "Лицевой счет"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-ls"]').click()
    # Оставить поле лицевой счет пустым

    # Ввести пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Bey-Jq4-5rQ-Qss')
    time.sleep(3)

    # Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    time.sleep(3)

    # Проверка, что авторизация прошла не успешно
    assert driver.find_element(By.XPATH, '//*[@id="username-meta"]').text == 'Введите номер вашего лицевого счета'

# 12
def test_invalid_LS_and_pass(driver):
    # Перейти на страницу авторизации
    driver.get(URL)
    # Дождаться появления элемента "Лицевой счет"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-ls"]')))

    # Выбрать вкладку "Лицевой счет"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-ls"]').click()

    # Ввести в поле лицевой счет невалидные данные
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('456546546546546546546545')
    time.sleep(5)

    # Ввести пароль из китайских иероглифов
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('犯外处冬鸟务包饥主市立冯玄闪兰')
    time.sleep(3)

    # Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    time.sleep(3)

    # Проверка, что авторизация прошла не успешно
    assert driver.find_element(By.XPATH,
                               '//*[@id="form-error-message"]').text == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'

# 13
def test_login_XSS(driver):
    # Перейти на страницу авторизации
    driver.get(URL)

    # Дождаться появления элемента "Логин"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-login"]')))

    # Выбрать вкладку "Логин"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]').click()

    # Ввести логин
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('<script>alert("ok")</script>')
    time.sleep(3)

    # Ввести пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('<script>alert()</script>')
    time.sleep(3)

    # Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    time.sleep(3)

    # Проверка, что запрос откланен из соображений безопастности
    assert driver.find_element(By.TAG_NAME, 'h2').text != ('Ваш запрос был отклонен из соображений безопасности. '
                                                           'Обратитесь в техническую поддержку по номеру 8 (800) 1000'
                                                           ' 800.')
# 14
def test_automatic_tab_and_XSS(driver):
    # Перейти на страницу авторизации
    driver.get(URL)

    # Дождаться появления элемента "Логин"
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="t-btn-tab-login"]')))

    # Выбрать вкладку "Логин"
    driver.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]').click()

    # Ввести в поле логин email
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('<b>prostotak@inbox.ru<b>"<br>sfsfsf')
    time.sleep(3)

    # Ввести пароль
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('<script>alert("ok")</script>')
    time.sleep(3)

    # Нажать кнопку "Войти"
    driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
    time.sleep(3)

    # Проверка, что запрос откланен из соображений безопастности
    assert driver.find_element(By.TAG_NAME, 'h2').text != ('Ваш запрос был отклонен из соображений безопасности. '
                                                           'Обратитесь в техническую поддержку по номеру 8 (800) 1000'
                                                           ' 800.')

