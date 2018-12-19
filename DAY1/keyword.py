import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"

response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')
keyword = soup.select('.ah_roll')
keyword.selet('.ah_k')