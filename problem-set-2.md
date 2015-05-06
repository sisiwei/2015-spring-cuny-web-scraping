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

## Updates & Hints

- We are using version 3 of BeautifulSoup, you can check out the documentation for BeautifulSoup 3 here: http://www.crummy.com/software/BeautifulSoup/bs3/documentation.html

- If you find an answer online that doesn’t work, it might be tailored for BeautifulSoup4. The way you can tell however, is that in answers on the Internet, people usually include what libraries they import at the top of their scripts, just like we did in class. If you see something like ```from BeautifulSoup import BeautifulSoup```, which is what we did in class, the answer is probably using BeautifulSoup version 3. If it includes instead a message saying ```from bs4 import BeautifulSoup```, then you can assume they’re using BeautifulSoup4.

- Hint: If you've tried a million ways to get the URL out of those darn <a> tags, but are still getting errors, consider this: The first line that just says "Offender Name" doesn't actually have any <a> tags inside! So any code you write for every single line of the table won't necessarily work. There are two ways to get around this. (1) See if you can figure out how to check for whether an <a> tag exists, or (2) Skip the first row of the table all together, and just write the header row manually into your Python script.

- Hint: In some ways, the website you're scraping for homework is much simpler than the one we did in class. Don't overthink it! There's only one piece of data in every row of this website, unlike our class demo, which had many pieces of data per column. This might help make your script simpler if it's getting too confusing.
