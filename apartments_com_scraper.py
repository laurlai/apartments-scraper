# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:43:23 2018

@author: laura
"""

from bs4 import BeautifulSoup as bs
import json
import pandas as pd
import re
import requests

### Apartments URLs
# TODO: Store in DB
url = 'https://www.apartments.com/mount-vernon-plaza-washington-dc/m4229lh/'
url2 = 'https://www.apartments.com/mass-court-washington-dc/ghlk6jw/'

all_urls = [url, url2]

### Get the data
# Headers passed by browser, makes the request work
req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

r = requests.get(url2, headers=req_headers)
r.status_code

### Functions
def make_fee_dict(raw_text):
    clean_split = [x for x in raw_text.split('\n\n') if re.search('\$', x)]
    clean_dict = {}
    for item in clean_split:
        stripped = item.strip()
        stripped = re.split('\n', stripped)
        clean_dict[stripped[0]] = stripped[1]
    return clean_dict

'''
Let's make some soup
'''     
# Create soup object from request
soup = bs(r.content, 'html.parser')
# Name of Apartment
apt_name = soup.find(class_='propertyName').get_text().strip()

''' 
Collect Data of Interest
- Recurring Expenses
- One-Time Expenses
- Amenities
'''
# Gather Amenities
amenities = soup.find(id='amenitiesSection').get_text()

# Gather Fees
fees = soup.find(id='feesSection')

# List of recurring fees
recurring = fees.find(class_='monthlyFees').get_text()
recurring_dict = make_fee_dict(recurring)

# List of one time fees
onetime = fees.find(class_='oneTimeFees').get_text()
onetime_dict = make_fee_dict(onetime)

'''
Putting it all together (JSONify)
'''
result_dict = {'property-name': apt_name,
          'one-time-expenses': onetime_dict,
          'recurring-expenses': recurring_dict
          }

result = json.dumps(result_dict, indent=2)

'''
Print the results to console
'''
print(result)

