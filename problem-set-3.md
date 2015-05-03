# Problem Set 3
<i>Assigned: May 7th<i>
<br/><b>Due: May 13th at 11:59 p.m. (6 days to complete)</b>

Please remember the [Academy Honesty policy on problem sets](http://cdn.cs50.net/2014/fall/lectures/0/w/syllabus/syllabus.html#academic_honesty). If you are ever confused about what is okay and what isn't, ask me. 

## Goal
To give you practice scraping multiple pages of a website, and then save all the results in one place.

## Problems
Last week we scraped the New York State Division of Criminal Justice Services database of sex offenders on [its website](http://www.criminaljustice.ny.gov/SomsSUBDirectory/search_index.jsp). Your assignment this week is to scrape additional information about the offenders by going to each of their URLs.

Write a scraper that, after scraping the Name and URL information from [the Ciminal Justice Services database](http://www.criminaljustice.ny.gov/SomsSUBDirectory/search_index.jsp?offenderSubmit=true&LastName=&County=31&Zip=&Submit=Search), also visits each URL and scrapes it for the offender's ID and risk level. Then save this new information into a CSV file.

For example, your final CSV should look something like the following:

| OffenderName | URL | Offender ID | Risk Level
| --- | --- | --- | --- |
| ABDUL-HAKEEM, AS-SUFI | http://www.criminaljustice.ny.gov/SomsSUBDirectory/offenderDetails.jsp?offenderid=7227 | 7227 | 2
| ACES, HARRY | http://www.criminaljustice.ny.gov/SomsSUBDirectory/offenderDetails.jsp?offenderid=6706 | 6706 | 3
| ALCARAZ, JORGE | http://www.criminaljustice.ny.gov/SomsSUBDirectory/offenderDetails.jsp?offenderid=25377 | 25377 | 2

<b>Optional, for extra credit:</b>
- Some Offender IDs may appear multiple times. If this is the case, only include the Offender once.
- Also collect the Offender's address information.


