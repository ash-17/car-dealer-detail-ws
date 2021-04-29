#importing packages
import requests
from bs4 import BeautifulSoup
import re
import csv

#request main site url
URL = 'https://autoportal.com/mahindra/car-dealers/bangalore/page/2/'
page = requests.get(URL)

#parsing the url
soup = BeautifulSoup(page.content, 'html.parser')
dealers_list = soup.find_all('div', class_='item')

link_list = []
url_list = []
#getting data of all the dealers
for i in dealers_list:
    link_list.append(i.find('a', href = True))

#get all the links for dealers
for i in link_list:
    try:
        if re.search('/mahindra/car-dealers/bangalore/*', i['href']):
            url_list.append(i['href'])
    except TypeError:
       continue

data_list = []
#writing data to csv
def extract_data(dealers_name, dealers_data, soup1):
    try:
        address = soup1.find('div', class_='clearfix').find('p').text
        phone = soup1.find('span', class_='cell-md-none').text
        email = soup1.find('span', class_='fa-envelope').parent.text
        writeData(dealers_name, address, phone, email)

    except AttributeError:
        try:
            

        

def writeData(dealers_name, address, phone, email):
    data = [{'DealersName': dealers_name, 'Address': address, 'Phone': phone, 'Email': email}]
    # field names 
    fields = ['DealersName', 'Address', 'Phone', 'Email'] 
    
    # name of csv file 
    filename = "details.csv"
    
    # writing to csv file 
    with open(filename, 'a') as csvfile: 
        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
        
        # writing headers (field names)
        #writer.writeheader() 
        
        # writing data rows 
        writer.writerows(data)

#getting data from individual links
for i in url_list:
  
    page = requests.get('https://autoportal.com' + i)
    soup1 = BeautifulSoup(page.content, 'html.parser')

    dealers_name = soup1.find('h2', class_='h2').text
    dealers_data = soup1.find('div', class_='dealers')

    extract_data(dealers_name, dealers_data, soup1)


