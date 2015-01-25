# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import urllib2
import csv
from bs4 import BeautifulSoup
import datetime
import time
import re
import json

# <codecell>

with open(r"C:\Users\Schuster\Google Drive\Google_Play_Reviews\gp_urls.txt", 'rb') as json_f:
    google_play_list = json.load(json_f)

output_file = "C:\Users\Schuster\Google Drive\Google_Play_Reviews\Google Play Reviews Tracking.csv"

# <codecell>

now = datetime.datetime.now()
date = "%s/%s/%s" %(now.month, now.day, now.year)
time_est = "%s:%s" %(now.hour, now.minute)

rating_span_class = "rating-bar-container " 
star_nums = ["five", "four", "three", "two", "one"]

for obj in google_play_list:
    name = obj["name"]
    url = obj["url"]
    category = obj["category"]
    company = obj["company"]
    
    response = urllib2.urlopen(url)
    html = response.read()
    response.close()
    
    soup = BeautifulSoup(html)
    total_reviews = soup.find("span", class_="reviews-num").contents[0]
    total_reviews = re.sub(',', '', total_reviews)
    
    stars = {}
    
    for rating in star_nums:
        next_rating = rating_span_class + rating
        n_stars = soup.find("div", class_= rating_span_class + rating)
        n_star_reviews = n_stars.find("span", class_="bar-number").contents[0]
        stars[rating] = n_star_reviews
        
    with open(output_file, 'ab') as csv_f:
        f_writer = csv.writer(csv_f, delimiter=',')
        f_writer.writerow([date, time_est, name, company, category, url, total_reviews, stars['five'], stars['four'], stars['three'], stars['two'], stars['one']])
   
    time.sleep(.5)

