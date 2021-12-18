import asyncio
import datetime
import sys
from concurrent.futures import ProcessPoolExecutor
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


async def run_blocking_tasks(executor):
    # headless mode?
    headless = False
    if len(sys.argv) > 1:
        if sys.argv[1] == "headless":
            print("Running in headless mode")
            headless = True

    loop = asyncio.get_event_loop()

    # set variables
    output_timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    output_filename = f"output_{output_timestamp}.csv"

    # scrape and crawl
    blocking_tasks = [
        loop.run_in_executor(executor, run_process, output_filename, headless)
        for i in range(1, 21)
    ]
    completed, pending = await asyncio.wait(blocking_tasks)


if __name__ == "__main__":
    start_time = time()
    executor = ProcessPoolExecutor()

    # create event loop
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(run_blocking_tasks(executor))
    finally:
        event_loop.close()
    end_time = time()
    elapsed_time = end_time - start_time
    print(f"Elapsed run time: {elapsed_time} seconds")
