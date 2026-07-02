This project takes in a list of USCF (US Chess Federation) player IDs and prints the names of the players in the orders of most regular rating, most blitz rating, and most improvement in regular rating.

Process:
Every player on USCF is given an ID. Using this ID, a player's chess information can be found at the url https://ratings.uschess.org/player/{id}, substituting in the actual player id for {id}.
However, there is no endpoint url to specifically retrieve ratings, and the ratings themselves are not encoded in html. Therefore, Selenium was used to access the ratings of the player.
Selenium searched for certain classes, CSS selectors, or XPATHs, which were found using DevTools and inspecting the website.
