import time

from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage


class Test_covalto(WebDriverSetup):

    def test_add_item_to_course_pack(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        time.sleep(3)
        home_page.sign_up("standard_user", "secret_sauce")
        home_page.click_sing_up()
        home_page.asert_catalogo()
        home_page.click_add_car()
        home_page.click_check_car()
        home_page.click_checkout()
        home_page.register("Andres", "Mosquera", "111031")
        home_page.click_continue()
        home_page.finish_button()






