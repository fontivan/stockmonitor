from bs4 import BeautifulSoup
import os
from vendor import Vendor

'''
TODO: Add header
'''
class BestBuy(Vendor):

    '''
    TODO: Add header
    '''
    def __init__(self):
        super().__init__("Best Buy", os.getcwd() + "/vendors/best_buy")

    '''
    TODO: Add header
    '''
    def parse_item_page(self, item_page_html, stores_to_check):

        online_store = BeautifulSoup(item_page_html, features="html.parser") \
            .body \
            .find_all('div', attrs={'class': 'availabilityMessage_1MO75 container_3LC03'})

        for div in online_store:
            if not 'Sold out online' in div.text:
                return self.in_stock_result

        return self.out_of_stock_result