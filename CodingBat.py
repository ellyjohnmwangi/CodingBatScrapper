import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
header = {'user-agent': ua.chrome}
main_url = "https://codingbat.com/java"
page = requests.get(main_url, headers=header)
# page2 = requests.get('https://codingbat.com/java/Warmup-1', headers=header)
soup = BeautifulSoup(page.content, 'lxml')

base_url = 'https://codingbat.com'
all_links = [base_url + div.a['href'] for div in soup.find_all('div', class_="summ")]
# print(all_links)

for link in all_links:
    inner_page = requests.get(link, headers={'user-agent': ua.chrome})
    inner_soup = BeautifulSoup(inner_page.content, 'lxml')
    div = inner_soup.find('div', class_="tabc")
    inner_links = [base_url + td.a['href'] for td in div.table.find_all('td')]
    # print(inner_links)
    for inner_link in inner_links:
        last_page = requests.get(inner_link)
        last_soup = BeautifulSoup(last_page.content, 'lxml')
        div = last_soup.find('div', attrs={'class': "indent"})
        problem_statement = div.table.div.string
        siblings = div.table.div.next_siblings
        examples = [sibling for sibling in siblings if sibling.string is not None]
        print(problem_statement, '\n')
        for example in examples:
            print(example)
        for sibling in siblings:
            if sibling.string is not None:
                print(sibling)
        print('\n\n\n')
