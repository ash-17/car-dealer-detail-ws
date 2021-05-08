This web scraper code was created to fetch car dealer details from https://autoportal.com/ and write it into .csv file. This was related to project I was working on.
Using python requests module and beautifulsoup.



Steps to run the program:

1. run "pip install -r requirements.txt

2. run "python dealer-details.py"

3. It'll ask for entering URL. Enter in this format : "https://autoportal.com/{company_name}/car-dealers/{cityname}/"

4. The detials.csv file will not have header column. Add "DealersName, Address, Phone, Email" in first row to use as header.

Author - Ashutosh Mehta
