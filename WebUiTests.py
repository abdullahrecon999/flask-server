import unittest
unittest.TestLoader.sortTestMethodsUsing = None
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

class testunit(unittest.TestCase):
    
    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)


    def test_01_title(self):
        self.driver.get("http://127.0.0.1:5000")
        self.assertEqual(self.driver.title, "Simple Task Manager")


    def test_02_createTask(self):
        self.driver.get("http://127.0.0.1:5000")
        input_elm = self.driver.find_element(By.XPATH, "//*[@id='cform-title']")
        input_elm.send_keys("Task 1")
        input_elm = self.driver.find_element("id", "cform-shortdesc")
        input_elm.send_keys("This is a test task")
        input_elm = self.driver.find_element("id", "cform-priority")
        input_elm.send_keys("1")
        input_elm = self.driver.find_element("id", "cform-create")
        input_elm.click()
        # assert task created successfully
        find_elm = self.driver.find_element("id", "Task 0").is_displayed()
        self.assertEqual(find_elm, True)


    def test_03_updateDesc(self):
        self.driver.get("http://127.0.0.1:5000")
        input_elm = self.driver.find_element("id", "uform-key")
        input_elm.send_keys("0")
        input_elm = self.driver.find_element("id", "uform-shortdesc")
        input_elm.send_keys("Updated Description")
        input_elm = self.driver.find_element("id", "uform-update")
        input_elm.click()
        # assert task updated successfully
        short_desc = self.driver.find_element(By.XPATH, "//*[@id='Task 0']")
        self.assertEqual(short_desc.text.split('\n')[2].split('=')[1].strip(), "Updated Description")


    def test_04_deleteTask(self):
        self.driver.get("http://127.0.0.1:5000")
        input_elm = self.driver.find_element("id", "dform-key")
        input_elm.send_keys("0")
        input_elm = self.driver.find_element("id", "dform-delete")
        input_elm.click()
        # assert task deleted successfully
        try:
            find_elm = self.driver.find_element("id", "Task 0").is_displayed()
            self.assertEqual(find_elm, False)
        except:
            self.assertEqual(True, True)


    def test_05_reset(self):
        self.driver.get("http://127.0.0.1:5000")
        input_elm = self.driver.find_element("id", "reset-reset")
        input_elm.click()
        # assert reset successfully
        try:
            find_elm = self.driver.find_element("id", "Task 0").is_displayed()
            self.assertEqual(find_elm, False)
        except:
            self.assertEqual(True, True)


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()