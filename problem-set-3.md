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

## Updates & Hints

- Hint: Remember that I showed all of you mechanize last week because it will help you with your final projects. You do not need to use mechanize for this homework assignment.

- Hint: A great way to tackle this problem set is in two parts:   

  1. Try to scrape one of the URLs you saved from the last assignment, such as: http://www.criminaljustice.ny.gov/SomsSUBDirectory/offenderDetails.jsp?offenderid=7227 All of these pages are structured the same, so once you scrape one, it's like you've scraped them all.

  2. Try to merge your new scraper into your problem-set-2.py.

- Hint: Don't forget about lists. Sometimes plucking data out of a list is the easiest way to scrape.

- Hint: Code getting a little messy? Remember how we used functions in our first problem set? Sometimes it's easier to organize your code into functions, and then call them later. But remember, if you write a function, you can only call it *later* in the code.

- Hint: Since we're asking your scripts to visit so many URLs, running the entire scrape will take time. Give yourself some peace of mind by printing out some progress statements. For example, print out the name of the offender every time you get to a new one. This way, you won't be stuck wondering if your script is working.




