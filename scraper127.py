# Selenium, on the other hand, is used to interact with the webpage. It is
# used for testing the functionality of a
# website (Login/Logout/etc.) but can  be also used to interact with the page
# such as clicking a button, and many other things

from selenium import webdriver

#bs4 ( BeautifulSoup ) is a python module, which is famously used for
# parsing text as HTML and then performing actions in it, such as
# finding specific HTML tags with a particular class/id, or listing out all the
# li tags inside the ul tags.
#
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("chromedriver") # (executable_path=r"")
browser.get(START_URL)
time.sleep(10) # so that website will be completely loaded
def scrape():
    headers = ["name","light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data = [] # show ul and li tags related to rows on webpage
    for i in range(0, 428): # check the updated number at bottom of webpage
        # and accordingly change value
        soup = BeautifulSoup(browser.page_source, "html.parser") #Python library for pulling data out of HTML and XML files.
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}): 
             # ul: unordered list, it will find all the ul_tags with class exoplanet.
            li_tags = ul_tag.find_all("li") # li: list, ol: ordered list
            temp_list = []
            for index, li_tag in enumerate(li_tags): 
                #Enumerate will give us both the index and the element on that index
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0]) 
                    # find the a tag and then find the inner html contents ans append the contents
                else: # directly append inner html contents to avoid the error condition when column is empty 
                        # we are using try except block.
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        # we are finding an element with xpath, and then clicking it.
        #xPath : used to navigate through elements and attributes in an XML document
    with open("scrapper_1.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()

#//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a

