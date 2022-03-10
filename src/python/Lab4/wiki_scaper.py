from bs4 import BeautifulSoup
import requests
import time
import threading
from constants import Constants
from yahoo_scraper import YahooScraper

class WikiScraper:
    def __init__(self):
        self.req = requests.get(Constants.WIKI_URL)
        self.soup = BeautifulSoup(self.req.text, 'html.parser')
        self.table = self.soup.find('table', { 'class': 'wikitable' })
        self.yahoo_scraper = YahooScraper()
        self.symbols = []
    
    def flush(self):
        self.symbols = []
        self.yahoo_scraper.flush()

    def scrape_data_from_row(self, row):
        td = row.find('td')
        if td:
            symbol = td.find('a').text
            self.symbols.append(symbol)
            price = self.yahoo_scraper.scrape_price(symbol)
            print(f"[WikiScraper]: {symbol} -- {price}")

    def scrape_sequentially(self):
        self.flush()
        start = time.perf_counter()

        for row in self.table.findAll('tr'):
            self.scrape_data_from_row(row)

        end = time.perf_counter()

        return end - start

    def scrape_parallelly(self):
        self.flush()
        threads = []
        for row in self.table.findAll('tr'):
            thread = threading.Thread(target=self.scrape_data_from_row, args=(row,))
            threads.append(thread)

        start = time.perf_counter()
        for thread in threads:
            thread.start()
        
        for thread in threads:
            thread.join()

        end = time.perf_counter()
        return end - start
