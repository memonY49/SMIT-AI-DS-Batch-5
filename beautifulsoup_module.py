import requests as rs
from bs4 import BeautifulSoup
import csv

# url = 'https://quotes.toscrape.com'

# response = rs.get(url)
# html_doc = response.text
# soup = BeautifulSoup(html_doc, "html.parser")

# h2 = soup.find('h2')
# tags = h2.find_parent()
# for link in tags.find_all('a'):
#     category_route = link.get('href')
#     category = category_route.split('/')[2]
#     category_res = rs.get(url+category_route)
#     category_soup = BeautifulSoup(category_res.text,'html.parser')

#     print(category)
#     # print(category_soup.find("span").text)
#     qoutes = category_soup.findAll('span',attrs={"class":"text"})
    
#     with open(f"qoutes/{category}.csv","a") as file:
#         writer = csv.writer(file)
#         writer.writerow(["Category","Qoutes","Url"])
#         for line in qoutes:

#             writer.writerow([category,line.text,url+category_route])


book_url = "https://books.toscrape.com/"
response = rs.get(book_url)
book_html = response.text
bsoup = BeautifulSoup(book_html,'html.parser')

#Finding Categories
category_div = bsoup.find('div',class_="side_categories")
category_a = category_div.find_all('a')
category_links = [link.get('href') for link in category_a]
categories = [c.text.strip() for c in category_a]

for route, category in zip(category_links, categories):
    c_page = rs.get(book_url+route)
    p_soup = BeautifulSoup(c_page.text,'html.parser')
    book_ol = p_soup.find('ol', class_ = 'row')
    images = [pro.get('src') for pro in book_ol.find_all('img')]
    titles = [pro.text for pro in book_ol.find_all('h3')]
    price = [pro.text for pro in book_ol.find_all('p', class_="price_color")]
    availability = [pro.text for pro in book_ol.find_all('p', class_="instock availability")]
    print(titles)





