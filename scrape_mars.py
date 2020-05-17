import time 
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import re 

def scrape_info():
    #Initiate headless driver for all deployment 
    browser = Browser("chrome", executable_path = "chromedriver", headless = True)
    news_title, news_paragraph = scrape_mars_news(browser)

    # run all scraping functions and store it in one library
    mars_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "image_url": scrape_mars_image(browser),
        "mars_twitter": scrape_mars_tweet(browser),
        "mars_data": scrape_mars_table(),
        "hemisphere_info": scrape_mars_hemisphere(browser)
    }
    #stop webdriver and return data
    browser.quit()
    return mars_data


def scrape_mars_news(browser):
    nasa_url = "https://mars.nasa.gov/news/"
    browser.visit(nasa_url)
    time.sleep(1)
    html = browser.html
    soup = bs(html,"html.parser")
    article = soup.find("div", class_="list_text")
    news_title = article.find("div", class_ = "content_title").text
    news_paragraph = soup.find("div", class_="article_teaser_body").text
    return news_title, news_paragraph


def scrape_mars_image(browser):
    image_page_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_page_url)
    time.sleep(1)
    image_html = browser.html
    soup = bs(image_html, 'html.parser')
    image_url = soup.find('a', class_='fancybox')['data-fancybox-href']
    featured_image_url = 'https://www.jpl.nasa.gov' + image_url
    return featured_image_url

def scrape_mars_tweet(browser):
    Mars_weather_url= "https://twitter.com/marswxreport?lang=en"
    browser.visit(Mars_weather_url)
    time.sleep(1)
    Mars_weather_html=browser.html
    soup = bs(Mars_weather_html, 'html.parser')
    mars_twitters =soup.find('div', attrs={"data-testid": "tweet"}).get_text()
    return mars_twitters

def scrape_mars_table():
    mars_table_url = 'https://space-facts.com/mars/'
    mars_table = pd.read_html(mars_table_url)[0]
    time.sleep(1)
    mars_table.columns=['Description','Data']
    mars_table.set_index('Description',inplace = True)
    return mars_table.to_html()

def scrape_mars_hemisphere(browser):
    cerberus_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    schiaparelli_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    syrtis_major_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    valles_marineris_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    
    hemisphere_image_urls = []

    browser.visit(cerberus_url)
    time.sleep(1)
    cerberus_html = browser.html
    soup = bs(cerberus_html, "html.parser")
    cerberus_image = soup.find('img',class_ = 'wide-image')['src']
    cerberus_image_url = 'https://astrogeology.usgs.gov' + cerberus_image
    cerberus_title = soup.find('h2', class_='title').text
    hemisphere_image_urls.append({"title":cerberus_title, "img_url":cerberus_image_url})

    browser.visit(schiaparelli_url)
    time.sleep(1)
    schiaparelli_html = browser.html
    soup = bs(schiaparelli_html, "html.parser")
    schiaparelli_image = soup.find('img',class_ = 'wide-image')['src']
    schiaparelli_image_url = 'https://astrogeology.usgs.gov' + schiaparelli_image
    schiaparelli_title = soup.find('h2', class_='title').text
    hemisphere_image_urls.append({"title":schiaparelli_title, "img_url":schiaparelli_image_url})

    browser.visit(syrtis_major_url)
    time.sleep(1)
    syrtis_major_html = browser.html
    soup = bs(syrtis_major_html, "html.parser")
    syrtis_major_image = soup.find('img',class_ = 'wide-image')['src']
    syrtis_major_image_url = 'https://astrogeology.usgs.gov' + syrtis_major_image
    syrtis_major_title = soup.find('h2', class_='title').text
    hemisphere_image_urls.append({"title":syrtis_major_title, "img_url":syrtis_major_image_url})

    browser.visit(valles_marineris_url)
    time.sleep(1)
    valles_marineris_html = browser.html
    soup = bs(valles_marineris_html, "html.parser")
    valles_marineris_image = soup.find('img',class_ = 'wide-image')['src']
    valles_marineris_image_url = 'https://astrogeology.usgs.gov' + valles_marineris_image
    valles_marineris_title = soup.find('h2', class_='title').text
    hemisphere_image_urls.append({"title":valles_marineris_title, "img_url":valles_marineris_image_url})

    return hemisphere_image_urls







  
#     #parsing mars news 
# def scrape_mars_news(browser):

#     # Visit url
#     nasa_url = "https://mars.nasa.gov/news/"
#     browser.visit(nasa_url)
#     time.sleep(1)

#     #scrape page into soup
#     html = browser.html
#     soup = bs(html,"html.parser")

#     #get information
#     article = soup.find("div", class_="list_text")
#     news_title = article.find("div", class_ = "content_title").text
#     news_paragraph = soup.find("div", class_="article_teaser_body").text
#     return news_title, news_paragraph

# #parsing mars image
# def scrape_mars_image(browser):
#     image_page_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
#     browser.visit(image_page_url)
#     time.sleep(1)
#     html = browser.html
#     soup = bs(html,"html.parser")
#     image_html = browser.html
#     soup = bs(image_html, 'html.parser')
#     image_url = soup.find('img', class_='fancybox-image')['src']
#     featured_image_url = 'https://www.jpl.nasa.gov' + image_url
#     return featured_image_url

# #parsing mars tweet
# def parse_mars_tweet(browser):
#     Mars_weather_url= "https://twitter.com/marswxreport?lang=en"
#     browser.visit(Mars_weather_url)
#     time.sleep(1)
#     Mars_weather_html=browser.html
#     soup = bs(Mars_weather_html, 'html.parser')
#     mars_twitters =soup.find('div', attrs={"data-testid": "tweet"}).get_text()
#     return mars_twitters

# #parsing mars data
# def parse_mars_facts():
#     mars_facts_url = 'https://space-facts.com/mars/'
#     mars_facts = pd.read_html(mars_facts_url)[0]
#     mars_facts.columns=['Description','Data']
#     mars_facts.set_index('Description',inplace = False)
#     return mars_facts

# #parsing hemisphere information 
# def hemishpere_images(browser):
#     cerberus_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
#     schiaparelli_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
#     syrtis_major_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
#     valles_marineris_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
#     hemisphere_image_urls = []  
#     #cerberus
#     browser.visit(cerberus_url)
#     time.sleep(1)
#     cerberus_html = browser.html
#     soup = bs(cerberus_html, "html.parser")
#     #image url
#     cerberus_image = soup.find('img',class_ = 'wide-image')['src']
#     cerberus_image_url = 'https://astrogeology.usgs.gov' + cerberus_image
#     #title 
#     cerberus_title = soup.find('h2', class_='title').text
#     hemisphere_image_urls.append({"title":cerberus_title, "img_url":cerberus_image_url})

#     #syrtis major
#     browser.visit(syrtis_major_url)
#     time.sleep(1)
#     syrtis_major_html = browser.html
#     soup = bs(syrtis_major_html, "html.parser")
#     #image url
#     syrtis_major_image = soup.find('img',class_ = 'wide-image')['src']
#     syrtis_major_image_url = 'https://astrogeology.usgs.gov' + syrtis_major_image
#     #title 
#     syrtis_major_title = soup.find('h2', class_='title').text
#     hemisphere_image_urls.append({"title":syrtis_major_title, "img_url":syrtis_major_image_url})

#     #Valles Marineris 
#     browser.visit(valles_marineris_url)
#     time.sleep(1)
#     valles_marineris_html = browser.html
#     soup = bs(valles_marineris_html, "html.parser")
#     #image url
#     valles_marineris_image = soup.find('img',class_ = 'wide-image')['src']
#     valles_marineris_image_url = 'https://astrogeology.usgs.gov' + valles_marineris_image
#     #title 
#     valles_marineris_title = soup.find('h2', class_='title').text
#     hemisphere_image_urls.append({"title":valles_marineris_title, "img_url":valles_marineris_image_url})

#     return hemisphere_image_urls
    
# if __name__ == "__main__":
# # if running as script, print scraped sata
#     print(scrape_info())