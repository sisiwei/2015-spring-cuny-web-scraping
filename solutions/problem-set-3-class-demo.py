#!/usr/bin/env python2.7

import requests
from BeautifulSoup import BeautifulSoup
import csv

def getData(url):
    # url = "http://www.criminaljustice.ny.gov/SomsSUBDirectory/offenderDetails.jsp?offenderid=7227"
    r = requests.get(url)

    content = r.content
    soup = BeautifulSoup(content)

    table = soup.find("ul", attrs={"class":"somsTopTable nameyTable label-value"})

    # If we want to pluck out the right <li> tag with the data
    # all_li = table.findAll("li")
    # offender_id = all_li[0].find("span", attrs={"class":"value"}).text

    # If we want to look through a list of spans
    all_spans = table.findAll("span")
    offender_id = all_spans[1].text.replace("&nbsp;","")
    risk_level = all_spans[13].text.replace("&nbsp;","")

    return [offender_id, risk_level]

url = "http://www.criminaljustice.ny.gov/SomsSUBDirectory/search_index.jsp?offenderSubmit=true&LastName=&County=31&Zip=&Submit=Search"
r = requests.get(url)

# If you want to pass your information in
# contact_info = {
#   'User-Agent': 'Sisi Wei',
#   'From': 'My email address is sisi.wei@journalism.cuny.edu. I work at CUNY. Please contact me if ....'
# }

# r = requests.get(url, headers=contact_info)

content = r.content
soup = BeautifulSoup(content)

table = soup.find("table")

all_rows = []
# you can also do findAll("td")[1:10]
for row in table.findAll("td"):
    name = row.text
    new_url = "URL"
    data = ["Offender ID", "Risk Level"]

    if row.find('a') != None:
        new_url = 'http://www.criminaljustice.ny.gov' + row.find('a').get('href')
        data = getData(new_url)
        # [7227, 2]

    all_rows.append([name, new_url, data[0], data[1]])
    # ["Sisi", "https....", [7227, 2]]

# print all_rows

# Create or open a CSV file named offenders.csv
file = open("offenders.csv", "wb")

# Tell CSV the library, to get ready to write into that file
writer = csv.writer(file)

# Write it and save it
writer.writerows(all_rows)
