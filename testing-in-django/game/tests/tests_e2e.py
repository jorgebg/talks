from django.test import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver

# Make sure to chromedriver is installed first
# https://sites.google.com/a/chromium.org/chromedriver/downloads


class IndexTests(LiveServerTestCase):
    fixtures = ['rounds.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_index(self):
        driver = self.selenium
        driver.get(self.live_server_url)
        driver.find_element_by_xpath('//p[contains(text(), "Choose a shape")]')
        driver.find_element_by_xpath('//li[contains(text(), "Paper vs Rock")]')
        driver.find_element_by_xpath('//li[contains(text(), "Rock vs Paper")]')

    def test_play(self):
        driver = self.selenium
        driver.get(self.live_server_url)
        driver.find_element_by_xpath('//button[@value="Scissors"]').click()
        driver.find_element_by_xpath('//li[contains(text(), "Scissors vs")]')
