import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager as CM
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

USERNAME = os.getenv('USERNAME')
dirname = os.path.dirname(__file__)


def scrape(instagram_account=None):
    if not instagram_account:
        instagram_account = USERNAME
    options = webdriver.ChromeOptions()
    # Uncomment this option to run it headless
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    # Add a Mozila firefox user-agent so instagram doesn't block you.
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36')

    bot = webdriver.Chrome(executable_path=CM().install(), options=options)
    instagram_url = f'https://www.instagram.com/{instagram_account}/'

    print(f'[Info] - Scraping followers for {instagram_account}...')
    try:
        bot.get(instagram_url)
        time.sleep(3.5)
        followers_span = bot.find_element(By.CSS_SELECTOR,
                                          "span[title]")

        total_followers = followers_span.get_attribute('title')

        print(total_followers)
        print('[Info] - Saving...')
        print(
            f'[Info] - Total of {total_followers} followers for {instagram_account}')

        with open(os.path.join(dirname, f'{instagram_account}_followers.txt'), 'w+') as file:
            file.write(total_followers)
        print(
            f'[DONE] - Your total followers are saved in {instagram_account}_followers.txt file!')

    except NoSuchElementException:
        print(NoSuchElementException)
        print('erro')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        account_name = sys.argv[1]
    else:
        account_name = None
    scrape(account_name)