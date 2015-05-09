#!/usr/bin/env python2.7

import requests
from BeautifulSoup import BeautifulSoup
import csv

url = "http://www.criminaljustice.ny.gov/SomsSUBDirectory/search_index.jsp?offenderSubmit=true&LastName=&County=31&Zip=&Submit=Search"
r = requests.get(url)

content = r.content
soup = BeautifulSoup(content)

table = soup.find("table")

all_rows = []
for row in table.findAll("td"):
    name = row.text

    if row.find('a') == None:
        url = "URL"
    else:
        url = '"http://www.criminaljustice.ny.gov' + row.find('a').get('href') + '"'

    for letter in name:
        all_rows.append(letter)

print all_rows

# Create or open a CSV file named offenders.csv
file = open("offenders.csv", "wb")

# Tell CSV the library, to get ready to write into that file
writer = csv.writer(file)

# Write it and save it
writer.writerows(all_rows)
