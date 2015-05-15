#!/usr/bin/env python2.7

import requests
from BeautifulSoup import BeautifulSoup
import csv

def getRecords(url):
	r = requests.get(url)
	content = r.content
	soup = BeautifulSoup(content)

	table = soup.find("ul", attrs = {"class": "somsTopTable nameyTable label-value"})
	data = table.findAll("span", attrs = {"class": "value"})

	offender_id = data[0].text.replace("&nbsp;", "")
	risk_level = data[6].text.replace("&nbsp;", "")

	return [offender_id, risk_level]

url = "http://www.criminaljustice.ny.gov/SomsSUBDirectory/search_index.jsp?offenderSubmit=true&LastName=&County=31&Zip=&Submit=Search"
r = requests.get(url)

content = r.content
soup = BeautifulSoup(content)

table = soup.find("table")

all_rows = []
for row in table.findAll("td"):
	  name = row.text
	  new_url = ""
	  extra_data = []

	  if row.find('a') == None:
	      new_url = "URL"
	      extra_data = ["Offender ID", "Risk Level"]
	  else:
	      new_url = "http://www.criminaljustice.ny.gov" + row.find('a').get('href')
	      extra_data = getRecords(new_url)

	  all_rows.append([name, new_url, extra_data[0], extra_data[1]])

print all_rows

# Create or open a CSV file named offenders.csv
file = open("offenders-full.csv", "wb")

# Tell CSV the library, to get ready to write into that file
writer = csv.writer(file)

# Write it and save it
writer.writerows(all_rows)
