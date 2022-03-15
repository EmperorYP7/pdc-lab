from bs4 import BeautifulSoup
import requests
import time
import threading
from constants import Constants
from price_scraper import PriceScraper

class CryptoScraper:
    def __init__(self):
        self.req = requests.get(Constants.CRYPTO_URL)
        self.soup = BeautifulSoup(self.req.text, 'html.parser')
        self.table = self.soup.find('table',{'class':'chakra-table css-1bveei3'})
        self.price_scraper = PriceScraper()
        self.cryptos = []
    
    def flush(self):
        self.cryptos = []
        self.price_scraper.flush()

    def scrape_crypto_from_row(self, row):
        td = row.find('td',{'class':'css-1sem0fc'})
        if td:
            crypto = td.find('span',{'class':'chakra-text css-1mrk1dy'}).text
            self.cryptos.append(crypto)
            price = self.price_scraper.scrape_price(crypto)
            print(f"[CryptoScraper]: {crypto} -- {price}")

    def scrape_sequentially(self):
        self.flush()
        start = time.perf_counter()

        for row in self.table.findAll('tr'):
            self.scrape_crypto_from_row(row)

        end = time.perf_counter()

        return end - start

    def scrape_parallelly(self):
        self.flush()
        threads = []
        for row in self.table.findAll('tr'):
            thread = threading.Thread(target=self.scrape_crypto_from_row, args=(row,))
            threads.append(thread)

        start = time.perf_counter()
        for thread in threads:
            thread.start()
        
        for thread in threads:
            thread.join()

        end = time.perf_counter()
        return end - start
