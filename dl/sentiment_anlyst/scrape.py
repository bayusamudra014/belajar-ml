from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait

import time
import json

driver = webdriver.Chrome()
driver.get('https://www.goodreads.com/')

input("Login to goodreads and press enter to continue...")

print("Get all books from new release page")

date = [(i, j) for i in range(2022, 2025) for j in range(1, 13)]
# date = [(2024, 7)]

books = []

for i, j in date:
    driver.get(f'https://www.goodreads.com/new_releases/{i}/{j}')
    driver.implicitly_wait(10)

    for i in driver.find_elements(By.CSS_SELECTOR, "#new_releases .cover a"):
        books.append(i.get_attribute('href'))

with open("datasets/books.txt", "w") as f:
    f.write("\n".join(books))


# Scrape corpus
print("Get all corpus from books review")
books = open("datasets/books.txt").read().split("\n")

cnt = 0

for i in books:
    cnt += 1
    print(
        f"Scraping progress: {cnt} of {len(books)} ({cnt/len(books)*100:.2f}%)")

    corpus = []

    driver.get(i)
    time.sleep(3)

    for i in driver.find_elements(By.CSS_SELECTOR, ".TruncatedContent"):
        text = i.text
        text = text.replace("\n", " ")
        text = text.replace("show more", " ")
        text = text.replace("show less", " ")

        corpus.append(text)

    with open("datasets/corpus.txt", "a") as f:
        f.write("\n".join(corpus))

# Scrape comments
print("Get all reviews from books")
books = open("datasets/books.txt").read().split("\n")


def try_close_overlay():
    try:
        time.sleep(1)
        res = driver.find_element(
            By.CSS_SELECTOR, ".Overlay .Overlay__close button")

        wait = WebDriverWait(driver, timeout=10)
        wait.until(lambda driver: res.is_displayed())

        if res:
            res.click()
    except NoSuchElementException:
        pass


def get_rating_with_value(value):
    rating = driver.find_elements(
        By.CSS_SELECTOR, ".RatingsHistogram .RatingsHistogram__bar")

    for i in rating:
        if i.get_attribute("aria-label").startswith(f"{value} star"):
            wait = WebDriverWait(driver, timeout=10)
            wait.until(lambda driver: i.is_displayed())
            return i

    return None


START_IDX = 0
cnt = START_IDX
comment_cnt = 0

driver.implicitly_wait(10)

for i in books[START_IDX:]:
    cnt += 1
    print(
        f"Scraping progress: {cnt} of {len(books)} ({cnt/len(books)*100:.2f}%) with {comment_cnt} comments")

    driver.get(i)
    time.sleep(1)

    ref = driver.find_element(
        By.CSS_SELECTOR, ".ReviewsList .Divider .Button").get_attribute("href")

    driver.get(ref)
    try_close_overlay()

    for i in range(5, 0, -1):
        time.sleep(3)

        driver.execute_script("window.scrollTo(0,0)")
        rating = get_rating_with_value(i)

        time.sleep(3)
        rating.click()

        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        for i in driver.find_elements(By.CSS_SELECTOR, ".ReviewCard"):
            rating = i.find_element(
                By.CSS_SELECTOR, ".RatingStars").get_attribute("aria-label")

            text = i.find_element(By.CSS_SELECTOR, ".ReviewText").text

            with open("datasets/comments.ljson", "a") as f:
                f.write(json.dumps({
                    "rating": rating,
                    "text": text
                }))
                f.write("\n")

            comment_cnt += 1
