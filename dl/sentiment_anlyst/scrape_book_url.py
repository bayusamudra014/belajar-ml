from selenium import webdriver
from selenium.webdriver.common.by import By


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
