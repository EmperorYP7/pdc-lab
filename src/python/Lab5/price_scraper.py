from bs4 import BeautifulSoup
import requests
from constants import Constants

class PriceScraper:

    def flush(self):
        self.req = None
        self.url = None
        self.soup = None

    def scrape_price(self, symbol):
        url = Constants.CRYPTO_URL + (symbol.replace(" ","-").lower())
        self.req = requests.get(url).text
        self.soup = BeautifulSoup(self.req, 'html.parser')
        div = self.soup.find('div',{'class':'css-yt38q3'})
        if div:
            val = div.find('span',{'class':'chakra-text css-13hqrwd'})
            return val.text
        else:
            return ""
