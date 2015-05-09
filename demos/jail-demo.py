#!/usr/bin/env python2.7

import requests
from BeautifulSoup import BeautifulSoup
import csv

# Go to the website
url = "http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp"
response = requests.get(url)

# Read the page
raw_code = response.content

# There's a <table> with class="resultsTable"
# Identify where the table is
soup = BeautifulSoup(raw_code)
table = soup.find("table", attrs={'class': 'resultsTable'})

# Copy each part of the table to somewhere

all_rows = []
for row in table.findAll("tr"):

    type_of_cell = ""
    if row == table.findAll("tr")[0]:
        type_of_cell = "th"
    else:
        type_of_cell = "td"

    list_of_cells = []
    for cell in row.findAll(type_of_cell):
        data = cell.text.replace("&nbsp;", "")
        list_of_cells.append(data)
    all_rows.append(list_of_cells)


# Create or open a CSV file named inmates.csv
file = open("inmates.csv", "wb")

# Tell CSV the library, to get ready to write into that file
writer = csv.writer(file)

# Write it and save it
writer.writerows(all_rows)
