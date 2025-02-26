import time

from selenium.webdriver.common.by import By

base_url = "https://www.saucedemo.com/"


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.user_name="user-name"
        self.password="password"
        self.submit_button = "login-button"
        self.products="inventory_item_name "
        self.add_car="add-to-cart-sauce-labs-backpack"
        self.check_car="shopping_cart_link"
        self.submit_check = "checkout"
        self.name="first-name"
        self.last_name="last-name"
        self.postal="postal-code"
        self.finish="finish"
        self.continue_button="continue"



    def get_user_name(self):
        return self.driver.find_element(By.ID, self.user_name)
    def get_passwordv(self):
        return self.driver.find_element(By.ID, self.password)
    def get_submit_button(self):
        return self.driver.find_element(By.ID, self.submit_button)

    def get_productos(self):
        return self.driver.find_element(By.CLASS_NAME, self.products)
    def get_add_cars(self):
        return self.driver.find_element(By.ID, self.add_car)
    def get_check_cars(self):
        return self.driver.find_element(By.CLASS_NAME, self.check_car)
    def get_submit_checks(self):
        return self.driver.find_element(By.ID, self.submit_check)
    def get_name(self):
        return self.driver.find_element(By.ID, self.name)
    def get_last_name(self):
        return self.driver.find_element(By.ID, self.last_name)
    def get_postal(self):
        return self.driver.find_element(By.ID, self.postal)
    def get_continue(self):
        return self.driver.find_element(By.ID, self.continue_button)
    def get_finish_process(self):
        return self.driver.find_element(By.ID, self.finish)
        

    def sign_up(self, user_name, passwordv):
        self.get_user_name().send_keys(user_name)
        self.get_passwordv().send_keys(passwordv)
        time.sleep(2)

    def click_sing_up(self):
        self.get_submit_button().click()
    
    def asert_catalogo(self):
        self.get_productos()

    def click_add_car(self):
        self.get_add_cars().click()
    
    def click_check_car(self):
        self.get_check_cars().click()

    def click_checkout(self):
        self.get_submit_checks().click()
    time.sleep(5)

    def register(self, name, last_name, postal):
        self.get_name().send_keys(name)
        self.get_last_name().send_keys(last_name)
        self.get_postal().send_keys(postal)

    def click_continue(self):
        self.get_continue().click()
    
    def finish_button(self):
        self.get_finish_process().click()


    

    @staticmethod
    def get_base_url():
        return base_url
