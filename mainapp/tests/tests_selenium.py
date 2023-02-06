from django.conf import settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestI18nSelenium(StaticLiveServerTestCase):

    fixtures = ("authapp/fixtures/001_user_admin.json",)

    def setUp(self):
        super().setUp()
        self.selenium = WebDriver(settings.SELENIUM_DRIVER_PATH_FF)
        self.selenium.implicitly_wait(10)
        # Login
        self.selenium.get(f"{self.live_server_url}{reverse('authapp:login')}")
        button_enter = WebDriverWait(self.selenium, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[type="submit"]'))
        )
        self.selenium.find_element_by_id("id_username").send_keys("admin")
        self.selenium.find_element_by_id("id_password").send_keys("admin")
        button_enter.click()
        # Wait for footer
        WebDriverWait(self.selenium, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "mt-auto")))

    def test_i18n_button_clickable(self):
        button_create = WebDriverWait(self.selenium, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, f'[action="/i18n/setlang/"]'))
        )
        print("Trying to click button ...")
        button_create.click()  # Test that button clickable
        WebDriverWait(self.selenium, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "border-right")))
        print("Button clickable!")

    def test_change_i18n(self):
        button_create = WebDriverWait(self.selenium, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, f'[action="/i18n/setlang/"]'))
        )
        button_create.click()
        a = WebDriverWait(self.selenium, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, f'[href="/mainapp/news/"]'))
        )
        if a.text == "Новости":
            print("Language_chancged!")
        else:
            raise

    def tearDown(self):
        # Close browser
        self.selenium.quit()
        super().tearDown()
