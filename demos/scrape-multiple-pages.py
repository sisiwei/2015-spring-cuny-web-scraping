#!/usr/bin/env python2.7
from BeautifulSoup import BeautifulSoup
import csv
from mechanize import Browser

# Keeping track of how many pages we want to scrape
number_of_pages = 4

url = "http://mapyourtaxes.mo.gov/MAP/Employees/Employee/SearchEmployees.aspx"

# Starting to use mechanize
br = Browser()
br.open(url)

# Select the form
br.select_form("ctl01")

# Fill out the form
br.form['SearchEmployees1$CalendarYear1$ddlCalendarYear'] = ['2013']
br.form['SearchEmployees1$ddlAgencies'] = ['931']
br.form['SearchEmployees1$txtLastName'] = '%'
br.form['SearchEmployees1$txtFirstName'] = '%'

# Push GO!
br.submit('SearchEmployees1$btnSearch')

final_data = []
# [0,1,2,3]

for page in range(number_of_pages):

    br.select_form("ctl01")
    br.form["MozillaPager1$ddlPageNumber"] = [str(page)]
    br.submit('MozillaPager1$btnPageNumber')

    content = br.response()
    soup = BeautifulSoup(content)

    table = soup.find("table", attrs={'id': 'grdEmployees'})

    all_rows = []
    for row in table.findAll("tr"):

        type_of_cell = ""
        if row == table.findAll("tr")[0]:
            type_of_cell = "th"
        else:
            type_of_cell = "td"

        list_of_cells = []
        for cell in row.findAll(type_of_cell):
            data = cell.text
            list_of_cells.append(data)
        final_data.append(list_of_cells)

print final_data

# Create or open a CSV file named offenders.csv
# file = open("salaries.csv", "wb")

# # Tell CSV the library, to get ready to write into that file
# writer = csv.writer(file)

# # Write it and save it
# writer.writerows(all_rows)
