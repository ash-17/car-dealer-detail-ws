#importing packages
import requests
from bs4 import BeautifulSoup
import re
import csv

#request main site url
url = input("Enter the url in format \"https://autoportal.com/mahindra/car-dealers/cityname/\" \n")

def req():
    
    for i in range(1, 100):
        link_list = []
        url_list = []
        URL = url + 'page/' + str(i) + '/'
        page = requests.get(URL)
        if page.status_code == 404:
            break
        else:
            #parsing the url
            soup = BeautifulSoup(page.content, 'html.parser')
            dealers_list = soup.find_all('div', class_='item')

            #getting data of all the dealers
            for i in dealers_list:
                link_list.append(i.find('a', href = True))

#get all the links for dealers
            for i in link_list:
                try:
                    a = i['href']
                    url_list.append(a)
                except TypeError:
                    continue
            get_links(url_list)

data_list = []
#writing data to csv
def extract_data(dealers_name, dealers_data, soup1):
    def send_address():
        try:
            address = soup1.find('div', class_='clearfix').find('p').text
            return address
        except AttributeError:
            return ('NA')

    def send_phone():
        try:
            phone = soup1.find('span', class_='cell-md-none').text
            return phone
        except AttributeError:
            return ('NA')
    def send_email():
        try:
            email = soup1.find('span', class_='fa-envelope').parent.text
            return email
        except AttributeError:
            return ('NA')
    
    address = send_address()
    phone = send_phone()
    email = send_email()
    writeData(dealers_name, address, phone, email)
            

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
def get_links(url_list):
    for i in url_list:
  
        page = requests.get('https://autoportal.com' + i)
        soup1 = BeautifulSoup(page.content, 'html.parser')

        try:
            dealers_name = soup1.find('h2', class_='h2').text
            dealers_data = soup1.find('div', class_='dealers')

            extract_data(dealers_name, dealers_data, soup1)
        except AttributeError:
            continue


req()