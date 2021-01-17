import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


def remove_repetidos(titulo):
    l = []
    for i in range(0, len(titulo)):
        if titulo[i] != 'No title':
            l.append(titulo[i])
        else:
            l.sort
    return l


def remove_stars(estrelas):
    l = []
    for j in range(0, len(titulo)):
        if estrelas[j][1] != 'star-rating':
            l.append(estrelas[j][1])
        else:
            l.sort
    return l


titulo = []
preco = []
estrelas = []
estoque = []
url = ["http://books.toscrape.com/catalogue/category/books_1/page-1.html", "http://books.toscrape.com/catalogue/category/books_1/page-2.html", "http://books.toscrape.com/catalogue/category/books_1/page-3.html", "http://books.toscrape.com/catalogue/category/books_1/page-4.html", "http://books.toscrape.com/catalogue/category/books_1/page-5.html", "http://books.toscrape.com/catalogue/category/books_1/page-6.html", "http://books.toscrape.com/catalogue/category/books_1/page-7.html", "http://books.toscrape.com/catalogue/category/books_1/page-8.html", "http://books.toscrape.com/catalogue/category/books_1/page-9.html", "http://books.toscrape.com/catalogue/category/books_1/page-10.html", "http://books.toscrape.com/catalogue/category/books_1/page-11.html", "http://books.toscrape.com/catalogue/category/books_1/page-12.html", "http://books.toscrape.com/catalogue/category/books_1/page-13.html", "http://books.toscrape.com/catalogue/category/books_1/page-14.html", "http://books.toscrape.com/catalogue/category/books_1/page-15.html", "http://books.toscrape.com/catalogue/category/books_1/page-16.html", "http://books.toscrape.com/catalogue/category/books_1/page-17.html", "http://books.toscrape.com/catalogue/category/books_1/page-18.html", "http://books.toscrape.com/catalogue/category/books_1/page-19.html", "http://books.toscrape.com/catalogue/category/books_1/page-20.html",  "http://books.toscrape.com/catalogue/category/books_1/page-21.html", "http://books.toscrape.com/catalogue/category/books_1/page-22.html", "http://books.toscrape.com/catalogue/category/books_1/page-23.html", "http://books.toscrape.com/catalogue/category/books_1/page-24.html", "http://books.toscrape.com/catalogue/category/books_1/page-25.html",
       "http://books.toscrape.com/catalogue/category/books_1/page-26.html", "http://books.toscrape.com/catalogue/category/books_1/page-27.html", "http://books.toscrape.com/catalogue/category/books_1/page-28.html", "http://books.toscrape.com/catalogue/category/books_1/page-29.html", "http://books.toscrape.com/catalogue/category/books_1/page-30.html", "http://books.toscrape.com/catalogue/category/books_1/page-31.html", "http://books.toscrape.com/catalogue/category/books_1/page-32.html", "http://books.toscrape.com/catalogue/category/books_1/page-33.html", "http://books.toscrape.com/catalogue/category/books_1/page-34.html", "http://books.toscrape.com/catalogue/category/books_1/page-35.html", "http://books.toscrape.com/catalogue/category/books_1/page-36.html", "http://books.toscrape.com/catalogue/category/books_1/page-37.html", "http://books.toscrape.com/catalogue/category/books_1/page-38.html", "http://books.toscrape.com/catalogue/category/books_1/page-39.html", "http://books.toscrape.com/catalogue/category/books_1/page-40.html",  "http://books.toscrape.com/catalogue/category/books_1/page-41.html", "http://books.toscrape.com/catalogue/category/books_1/page-42.html", "http://books.toscrape.com/catalogue/category/books_1/page-43.html", "http://books.toscrape.com/catalogue/category/books_1/page-44.html", "http://books.toscrape.com/catalogue/category/books_1/page-45.html", "http://books.toscrape.com/catalogue/category/books_1/page-46.html", "http://books.toscrape.com/catalogue/category/books_1/page-47.html", "http://books.toscrape.com/catalogue/category/books_1/page-48.html", "http://books.toscrape.com/catalogue/category/books_1/page-49.html", "http://books.toscrape.com/catalogue/category/books_1/page-50.html"]

for i in range(0, len(url)):
    req = requests.get(url[i])
    soup = BeautifulSoup(req.content, 'html.parser')
    conteudo = soup.find_all('article', class_='product_pod')

    for lista1 in conteudo:
        lista2 = lista1.find_all('a')
        for lista3 in lista2:
            titulo.append(lista3.get('title', 'No title'))

    for lista4 in conteudo:
        lista5 = lista4.find_all('p', class_='price_color')
        for lista6 in lista5:
            preco.append(str(lista6.next_element))

    for lista7 in conteudo:
        lista8 = lista7.find_all('p', class_='star-rating')
        for lista9 in lista8:
            estrelas.append(lista9.get('class'))

    for lista10 in conteudo:
        lista11 = lista10.find_all('p', class_='instock availability')
        for lista12 in lista11:
            lista13 = lista12.stripped_strings
            for lista14 in lista13:
                estoque.append(repr(lista14))

titulo = remove_repetidos(titulo)
estrelas = remove_stars(estrelas)

df = pd.DataFrame({'Product Name': titulo, 'Price': preco,
                   'Rating': estrelas, 'Stock': estoque})
df.to_csv('products.csv', index=False, encoding='utf-8')

pd.read_csv('products.csv')
