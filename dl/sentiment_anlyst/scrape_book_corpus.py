from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.goodreads.com/')

input("Login to goodreads and press enter to continue...")

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

driver.quit()
