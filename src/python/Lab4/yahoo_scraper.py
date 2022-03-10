from bs4 import BeautifulSoup
import requests
from constants import Constants

class YahooScraper:

    def flush(self):
        self.req = None
        self.url = None
        self.soup = None

    def scrape_price(self, symbol):
        self.req = requests.get(Constants.YAHOO_URL + symbol).text
        self.soup = BeautifulSoup(self.req, 'html.parser')
        div = self.soup.find('div', {'class' : 'D(ib) Mend(20px)'})
        if div:
            val = div.find('fin-streamer', {'class' : 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})
            return val.text
        else:
            return ""
