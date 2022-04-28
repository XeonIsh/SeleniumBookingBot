from selenium import webdriver
import os
import booking.constants as const
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"F:\python\SeleniumBOT",
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()


 #
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Escolha sua moeda"]'
        )
        currency_element.click()
        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="changed_currency=1;selected_currency={currency}"]'
        )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_date = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        check_out_date.click()

    def select_adults(self, count=1):
        selection_element = self.find_element_by_id('xp__guests__toggle')
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element_by_css_selector(
                'button[aria-label="Diminuir número de Adultos"]'
            )
            decrease_adults_element.click()
            #Se o valor de adultos atingir 1, o loop encerrara
            adults_value_element = self.find_element_by_id('group_adults')
            adults_value = adults_value_element.get_attribute(
                'value') #retorna num de adultos

            if int(adults_value) == 1:
                break


        increase_button_element = self.find_element_by_css_selector(
            'button[aria-label="Aumentar número de Adultos"]'
        )

        for _ in range (count - 1):
            increase_button_element.click()

    def click_search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_start_rating(3, 4)
        filtration.sort_lowest()

    def report_results(self):
        cards_casas = self.find_elements_by_xpath('//div[@data-testid="property-card"]')

        for casa in cards_casas:
            precos = casa.find_elements_by_xpath(
                './/span[contains(text(), "R$") and (not(contains(text(), "Ganhe")))] '
            )

            for preco in precos:
                print(preco.text)





