from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import sys
from selenium.webdriver import FirefoxOptions
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()
PROJECT = 3
class Bot():
    def __init__(self, id):
        options = FirefoxOptions()
        options.headless = True
        self.driver = webdriver.Firefox(executable_path=os.path.join(os.getcwd(), "geckodriver"), options=options)
        self.id = id
        self.project = PROJECT
        self.base_url = "http://146.190.25.75:3601/"
    def log_in(self):
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

def main():
    b = Bot(sys.argv[1])
    b.sign_up()
    b.log_in()
    time.sleep(1)
    # b.run_project()

if __name__ == "__main__":
    main()
