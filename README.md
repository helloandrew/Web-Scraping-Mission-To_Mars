# Web-Scraping-Mission-To_Mars

A web application was built that scrapes data from five different websites to gather data related to the Mission to Mars and displays the information in a single HTML page.

Data Scraping from the following sources:

https://mars.nasa.gov/news/ - collected the latest News Title and Paragraph Text

https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars - used splinter to navigate the site and find the image url for the current Featured Mars Image

https://twitter.com/marswxreport?lang=en - scrape the latest Mars weather tweet from the page

https://space-facts.com/mars/ - Scraped the table containing facts about mars including Diameter, Mass, etc. and converted the data to a HTML table string using Pandas

https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars - obtained high resolution images for each of Mar's hemispheres

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

Create a root route which queries the Mongo database and pass the mars data into the HTML template to display the data.

Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements.





