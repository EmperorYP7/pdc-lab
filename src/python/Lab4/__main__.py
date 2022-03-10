import time
from wiki_scaper import WikiScraper

def main():
    scaper = WikiScraper()
    sequential_runtime = scaper.scrape_sequentially()
    parallel_runtime = scaper.scrape_parallelly()

    print(f"---------- Results ----------")
    print(f"Sequential Runtime:\t {sequential_runtime} s")
    print(f"Parallel Runtime:\t {parallel_runtime} s")

if __name__ == "__main__":
    main()
