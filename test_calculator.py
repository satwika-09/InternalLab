import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    yield driver

    driver.quit()


def test_calculator(setup_teardown):
    driver = setup_teardown

    driver.get(
        r"file:///C:/Users/vemul/OneDrive/Desktop/Exam/calculator.html"
    )

    driver.find_element(By.ID, "num1").send_keys("10")
    driver.find_element(By.ID, "num2").send_keys("20")

    driver.find_element(By.ID, "calculate").click()

    result = driver.find_element(By.ID, "result").text

    assert result == "Result: 30"