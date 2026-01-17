import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import allure

# from conftest import driver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Open URL")
@allure.description("open the URL of DEMO QA Website")
def test_openurl(driver):
    driver.get("https://demoqa.com/automation-practice-form")

    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(1)


@allure.title("Verify the Functionality of Student Registratiojn Form")
@allure.description("Test The Functionality of form By entering the Valif=d input in all Fields")
def test_login(driver):

    #
    # driver.get("https://demoqa.com/automation-practice-form")
    #
    # driver.execute_script("window.scrollBy(0, 400);")
    # time.sleep(1)

    test_openurl(driver)
    driver.find_element(By.XPATH,"//input[@id='firstName']").send_keys("Haseeb")
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='lastName']").send_keys("Ahmed")
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='userEmail']").send_keys("haseeb.ahmed@test.com")
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@id='genterWrapper']//div[@class='col-md-9 col-sm-12']//div[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='userNumber']").send_keys("01234567890")
    time.sleep(2)

    date = "12 Dec 1998"  # Format must match the site (e.g., "dd mmm yyyy")
    script = "document.getElementById('dateOfBirthInput').value = '{}';".format(date)
    driver.execute_script(script)
    time.sleep(2)

    subject_input = driver.find_element(By.ID, "subjectsInput")
    subject_input.send_keys("Computer Science")
    time.sleep(1)
    subject_input.send_keys(Keys.ENTER)
    driver.find_element(By.XPATH,"(//label[@class='custom-control-label'])[5]").click()
    driver.find_element(By.XPATH,"//input[@id='uploadPicture']").send_keys("C:\\Users\\Admin\\Downloads\\SampleJPGImage_2mbmb.jpg")
    time.sleep(2)

    driver.find_element(By.XPATH,"//textarea[@id='currentAddress']").send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.")
    dropdown_input = driver.find_element(By.XPATH, "//input[@id='react-select-3-input']")
    dropdown_input.send_keys("NCR")  # Type part of the option
    time.sleep(1)
    dropdown_input.send_keys(Keys.ENTER)

    city_input = driver.find_element(By.ID, "react-select-4-input")
    city_input.send_keys("Gurgaon")
    time.sleep(1)
    city_input.send_keys(Keys.ENTER)
    time.sleep(2)

    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(1)
    submit_button.click()





