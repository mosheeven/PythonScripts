import requests
from bs4 import BeautifulSoup

# Get the date
info = requests.get('https://magicseaweed.com/Dromi-Herzlyia-Marina-Surf-Report/4744/')

# Parse to html
soup = BeautifulSoup(info.text, 'html.parser')

# Get the data from tbody
for tbody in soup.find_all('tbody'):
    day = tbody.find_all('h6')[0].text.strip()

    print(day)

