# Aqui vao os metodos que extrairao o melhor preco
#pela busca realizada
from selenium.webdriver.remote.webelement import WebElement

class BookingReport:
    def __init__(self, boxes_section_element:WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements_by_css_selector(
            f'div[data-testid="price-and-discounted-price"]'
        )

    def pull_titles(self):
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element_by_class_name(
                'fde444d7ef _c445487e2'
            ).get_attribute('innerHTML').strip()
            print(hotel_name)



