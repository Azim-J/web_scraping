https://tribridgeschessclub.com/events/category/tournaments/ contains a list of upcoming tournaments for the Tribridges Chess Club.

Tribridges_Tournament_Finder.ipynb contains the code necessary to scrape information from the upcoming tournaments, and has a sample output from 7/27/2026

Process:
First, I found the url for the list of tournaments (linked above). However, there was no specific url to give just the cost or the date of the tournament, and the website was encoded in Javascript, so I used selenium to get general information about the tournament, such as the date, cost, and title of the tournament. I was also able to retrieve the url for the specific tournament using Selenium, which allowed me to access the tournament page and gather more details, such as the time control, various sections, and full description of the tournament.

Use/Purpose:
This program allows me to gather information about the upcoming tournaments in my local chess club (the Tribridges Chess Club) at a fast pace and have it formatted without me having to manually go through each tournament page.
