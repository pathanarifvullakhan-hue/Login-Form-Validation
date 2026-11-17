import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")
SELENIUM_URL = os.getenv("SELENIUM_URL", "http://localhost:4444/wd/hub")


class LoginFormTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        cls.driver = webdriver.Remote(command_executor=SELENIUM_URL, options=options)
        cls.driver.set_window_size(1280, 900)

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, "driver"):
            cls.driver.quit()

    def setUp(self):
        self.driver.get(BASE_URL)
        WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(By.ID, "loginForm")
        )

    def test_empty_fields_show_validation(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.assertEqual(
            "Username is required.",
            self.driver.find_element(By.ID, "usernameError").text
        )
        self.assertEqual(
            "Password is required.",
            self.driver.find_element(By.ID, "passwordError").text
        )

    def test_short_password_shows_validation(self):
        self.driver.find_element(By.ID, "username").send_keys("student")
        self.driver.find_element(By.ID, "password").send_keys("abc")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.assertEqual(
            "Password must be at least 6 characters.",
            self.driver.find_element(By.ID, "passwordError").text
        )

    def test_valid_login(self):
        self.driver.find_element(By.ID, "username").send_keys("student")
        self.driver.find_element(By.ID, "password").send_keys("Demo@123")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.assertIn("Login successful", self.driver.find_element(By.ID, "message").text)

    def test_invalid_credentials(self):
        self.driver.find_element(By.ID, "username").send_keys("wronguser")
        self.driver.find_element(By.ID, "password").send_keys("Wrong@123")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.assertEqual(
            "Invalid username or password.",
            self.driver.find_element(By.ID, "message").text
        )


if __name__ == "__main__":
    unittest.main()
