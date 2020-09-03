# Concurrent Web Scraping with Python and Selenium

## Want to learn how to build this project?

Check out the [blog post](https://testdriven.io/blog/building-a-concurrent-web-scraper-with-python-and-selenium/).

## Want to use this project?

1. Fork/Clone

1. Create and activate a virtual environment

1. Install the requirements

1. Run the scrapers:

    ```sh
    # sync
    (env)$ python script.py headless

    # parallel with multiprocessing
    (env)$ python script_parallel_1.py headless

    # parallel with concurrent.futures
    (env)$ python script_parallel_2.py headless

    # concurrent with concurrent.futures (should be the fastest!)
    (env)$ python script_concurrent.py headless

    # parallel with concurrent.futures and concurrent with asyncio
    (env)$ python script_asyncio.py headless
    ```

1. Run the tests:

    ```sh
    (env)$ python -m pytest test/test_scraper.py
    (env)$ python -m pytest test/test_scraper_mock.py
    ```
