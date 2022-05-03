# Inspired by Johnny Cao's Steam Web Scraper at https://github.com/j253cao/Webscraper/blob/main/main.py
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date

my_url = 'https://store.steampowered.com/search/?specials=1&filter=topsellers'

request_page = urlopen(my_url)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

steam_items = html_soup.find_all('div', class_="responsive_search_name_combined")

# field names
fields = ["Game Title", "Original Price CDN$", "Sale Price CDN$"]

# rows
gamePrices = []

# name of csv file
filename = "SteamSales-" + date.today().strftime("%m-%d-%Y") +".csv"

# writing to csv file
with open(filename, 'w') as gameProducts:
    # creating a csv writer object
    csvWriter = csv.writer(gameProducts)
    # writing the fields
    csvWriter.writerow(fields)
    for sales in steam_items:
        row = []
        price = sales.find('div', class_='col search_price discounted responsive_secondrow').text.replace("CDN$", '').split()
        title = sales.find('span', class_='title').text

        # Appends title and both prices
        row.append(title)
        row.append(price[0])
        row.append(price[1])
        # Append row to rows
        gamePrices.append(row)

    csvWriter.writerows(gamePrices)
