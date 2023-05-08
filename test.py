import requests
from bs4 import BeautifulSoup

# send a request to the website and retrieve its HTML content
url = 'https://tacoinfo.netlify.app/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# find all the taco elements on the page
taco_elements = soup.find_all('div', class_='taco')

# loop through the taco elements and extract their information
taco_data = []
for taco_element in taco_elements:
    name = taco_element.find('h2').text
    description = taco_element.find('p').text
    price = taco_element.find('span', class_='price').text
    taco_data.append({'name': name, 'description': description, 'price': price})

# print the extracted taco data
print(taco_data)
