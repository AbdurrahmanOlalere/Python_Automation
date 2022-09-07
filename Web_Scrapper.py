import requests
import re

#data request from url, maybe later tey to pull url's from another file might
# later try to pull data from weather site from a list of sunset's and sunrises in a year
data = requests.get('https://engineering.tamu.edu/etid/id/index.html')

phones = re.findall(r"^\\+?[1-9][0-9]{7,14}$", data.text)#regex that finds northamerican phone numbers
emails = re.findall(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.pyh[A-Z|a-z]{2,})+', data.text)#regex that find valid phone numbers

print(phones, emails)