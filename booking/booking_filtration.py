#Esse arquivo vai incluir uma classe com metodos que
#farao a interacao com o site.
#Apos receber os resultados, aplicaremos os filtros
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_start_rating(self, *star_values):
        for star_value in star_values:
            star_filtration_box = self.driver.find_element_by_css_selector(
                f'div[data-filters-item="class:class={star_value}"]'
            )
            star_filtration_box.click()

    def sort_lowest(self):
        sort_lowest_button = self.driver.find_element_by_css_selector(
            f'li[data-id="price"]'
        )
        sort_lowest_button.click()





# star_child_elements = star_filtration_box.find_elements_by_css_selector('*')
        # for star_element in star_child_elements:
        #     if star_element.find_element_by_css_selector(
        #         f'div[data-filters-item="class:class={star_value}"]'
        #     ):
        #         star_element.click()