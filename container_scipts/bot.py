from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
PROJECT = 1
class Bot():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=os.path.join(os.getcwd(), "geckodriver"))
        self.id = 1
        # self.id = os.environ['TEST_ID']
        self.project = PROJECT
        self.base_url = "http://localhost:3601/"
    def log_in(self):
    #     # t = self.driver.get("http://146.190.25.75:3601/login")
        self.driver.get(self.base_url + "login")
    #     # fill user and password

        self.driver.find_element(By.ID, "uname-normal").send_keys(f"test_account_id_{self.id}")
        self.driver.find_element(By.ID, "password-normal").send_keys(f"test_account_id_{self.id}")
        self.driver.find_element(By.XPATH, '//button[text()="Log in"]').click()



    def sign_up(self):
        self.driver.get(self.base_url + "signUp")
        inputs = self.driver.find_elements(By.XPATH, '//input')
        for input_field in inputs:
            input_field.send_keys(f"test_account_id_{self.id}")
            
        self.driver.find_element(By.XPATH, '//button[text()="Sign up"]').click()
    
    def run_project(self):
        self.driver.get(self.base_url + f"api/runproject/{self.project}")

        # "//*[text()[contains(., 'Welcome to the admin page!')]]
        # class="MuiSvgIcon-root MuiSvgIcon-fontSizeMedium MuiAvatar-fallback css-13y7ul3"

b = Bot()
b.sign_up()
b.log_in()
time.sleep(1)
b.run_project()