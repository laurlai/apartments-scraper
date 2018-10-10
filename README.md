# Web Scraping Proof-of-Concept for Apartments.com
Apartment hunting is tough, especially when you live in a city where there are so many to choose from. I wanted to figure out a way to make this burdensome task a bit easier. :house_with_garden: :blush:

### Methodology
Because Apartments.com is consistently structured across all apartment buildings, I thought it would be a good site to start experimenting with collecting data. 

**Skills and Libraries:**
* *HTML requests* to grab data
* *BeautifulSoup* for parsing text
* *RegEx* for pattern recognition
* *pandas* for organizing, processing, and storing the data in an analysis-friendly way

### Future State
* Rather than selecting URLs manually, I need to figure out a way to automatically grab buildings of interest
* Incorporate the Zillow API so the data includes for rent by owner and relevant neighborhood metadata
  * If this works, I can start doing some cool data analysis!
* Create a "true cost of moving" calculator that adds fees to first month's rent
