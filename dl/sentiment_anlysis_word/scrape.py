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

# date = [(i, j) for i in range(2017, 2022) for j in range(1, 13)]
# date = [(2024, 7)]

# books = []

# for i, j in date:
#     driver.get(f'https://www.goodreads.com/new_releases/{i}/{j}')
#     driver.implicitly_wait(10)

#     for i in driver.find_elements(By.CSS_SELECTOR, "#new_releases .cover a"):
#         books.append(i.get_attribute('href'))

# with open("datasets/books.txt", "w") as f:
#     f.write("\n".join(books))


# Scrape corpus
print("Get all corpus from books review")
books = open("datasets/books.txt").read().split("\n")

# cnt = 0

# for i in books:
#     cnt += 1
#     print(
#         f"Scraping progress: {cnt} of {len(books)} ({cnt/len(books)*100:.2f}%)")

#     corpus = []

#     driver.get(i)
#     time.sleep(3)

#     for i in driver.find_elements(By.CSS_SELECTOR, ".TruncatedContent"):
#         text = i.text
#         text = text.replace("\n", " ")
#         text = text.replace("show more", " ")
#         text = text.replace("show less", " ")

#         corpus.append(text)

#     with open("datasets/corpus.txt", "a") as f:
#         f.write("\n".join(corpus))

# Scrape comments
print("Get all reviews from books")
books = open("datasets/books.txt").read().split("\n")


def try_close_overlay():
    try:
        time.sleep(1)
        res = driver.find_element(
            By.CSS_SELECTOR, ".Overlay .Overlay__close button")

        wait = WebDriverWait(driver, timeout=3)
        wait.until(lambda driver: res.is_displayed())

        if res:
            res.click()
    except NoSuchElementException:
        pass


START_IDX = 0
cnt = START_IDX
comment_cnt = 0

driver.implicitly_wait(10)
is_closed = False

for i in books[START_IDX:]:
    cnt += 1
    print(
        f"Scraping progress: {cnt} of {len(books)} ({cnt/len(books)*100:.2f}%) with {comment_cnt} comments")

    driver.get(i)
    time.sleep(1)

    if not is_closed:
        try_close_overlay()
        is_closed = True

    for i in driver.find_elements(By.CSS_SELECTOR, ".ReviewCard"):
        for _ in range(3):
            try:
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
                break
            except NoSuchElementException:
                print("No element found. skip...")
                break
            except Exception as e:
                print("Error when scraping comment", e, ". retry...")
