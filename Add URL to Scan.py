# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import json
import urllib2
from bs4 import BeautifulSoup

# <codecell>

##Grabs the following data elements from url:
##Name, App Category, Company

# <codecell>

def add_url(url_string):
    response = urllib2.urlopen(url_string)
    html = response.read()
    response.close()
    
    soup = BeautifulSoup(html)
    
    name = soup.find("div", class_="document-title").contents[1].contents[0]
    company = soup.find("a", class_="document-subtitle primary").contents[1].contents[0]
    category = soup.find("span", itemprop="genre").contents[0]
    
    url_dict = {}
    url_dict["name"] = name
    url_dict["company"] = company
    url_dict["category"] = category
    url_dict["url"] = url_string
    
    with open("gp_urls.txt", "rb") as json_f:
        url_list = json.load(json_f)
        
    url_list.append(url_dict)
        
    with open("gp_urls.txt", "wb") as json_f:
        json.dump( url_list, json_f)  

# <codecell>

add_url("https://play.google.com/store/apps/details?id=com.antivirus")

# <codecell>


