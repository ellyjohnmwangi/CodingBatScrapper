import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua = UserAgent()
header = {'user-agent': ua.chrome}
page = requests.get('https://boston.craigslist.org/search/sof', headers=header)
soup = BeautifulSoup(page.content, 'lxml')
page = requests.get('https://boston.craigslist.org/search/sof', timeout=3)
tags = soup.find_all('a', class_="result-title hdrlnk")
for tag in tags:
    print(tag.get('href'))
    print(tag)
