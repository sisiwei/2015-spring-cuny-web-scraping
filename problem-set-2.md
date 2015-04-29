# Problem Set 2
<i>Assigned: April 30th<i>
<br/><b>Due: May 6th at 11:59 p.m. (6 days to complete)</b>

Please remember the [Academy Honesty policy on problem sets](http://cdn.cs50.net/2014/fall/lectures/0/w/syllabus/syllabus.html#academic_honesty). If you are ever confused about what is okay and what isn't, ask me. 

## Goal
The goal of this problem set is to give you practice scraping websites similar to, but not identical to the one we scraped during class.

## Problems
The New York State Division of Criminal Justice Services publishes a regularly updated database of sex offenders on [its website](http://www.criminaljustice.ny.gov/SomsSUBDirectory/search_index.jsp). Your assignment this week is to write a Python scraper that is able to get the latest list of sex offenders for New York county.

The specific URL you'll need to scrape is http://www.criminaljustice.ny.gov/SomsSUBDirectory/search_index.jsp?offenderSubmit=true&LastName=&County=31&Zip=&Submit=Search

In addition to scraping all the names from the page, you'll also need to scrape the URL associated with each name into a CSV file.

For example, your final CSV should look something like the following:

| OffenderName | URL |
| --- | --- |
| ABDUL-HAKEEM, AS-SUFI | http://www.criminaljustice.ny.gov/SomsSUBDirectory/offenderDetails.jsp?offenderid=7227 |
| ACES, HARRY | http://www.criminaljustice.ny.gov/SomsSUBDirectory/offenderDetails.jsp?offenderid=6706 |
| ALCARAZ, JORGE | http://www.criminaljustice.ny.gov/SomsSUBDirectory/offenderDetails.jsp?offenderid=25377 |

<b>A few things to look out for:</b>
- Some names will appear twice. Do not worry about that this week.
- The URLs that are on the website are not full URLs, meaning that if you were to copy and paste them into a web browser, they will not work.
    - Ex: "SomsSUBDirectory/offenderDetails.jsp?offenderid=7227" 
    - Make sure to add "http://www.criminaljustice.ny.gov/" to the front of these URLs when you are saving them.


