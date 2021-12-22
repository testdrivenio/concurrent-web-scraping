import datetime
import sys
from itertools import repeat
from multiprocessing import Pool, cpu_count
from time import sleep, time

from scrapers.scraper import connect_to_base, get_driver, parse_html, write_to_file


def run_process(filename, headless):

    # init browser
    browser = get_driver(headless)

    if connect_to_base(browser):
        sleep(2)
        html = browser.page_source
        output_list = parse_html(html)
        write_to_file(output_list, filename)

        # exit
        browser.quit()
    else:
        print("Error connecting to Wikipedia")
        browser.quit()


if __name__ == "__main__":

    # headless mode?
    headless = False
    if len(sys.argv) > 1:
        if sys.argv[1] == "headless":
            print("Running in headless mode")
            headless = True

    # set variables
    start_time = time()
    output_timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    output_filename = f"output_{output_timestamp}.csv"

    # scrape and craw
    with Pool(cpu_count() - 1) as p:
        p.starmap(run_process, repeat(output_filename), repeat(headless)))
    p.close()
    p.join()

    end_time = time()
    elapsed_time = end_time - start_time
    print(f"Elapsed run time: {elapsed_time} seconds")
