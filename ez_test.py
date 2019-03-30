import school

import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.lstreports.com/compare/" + "liberty" + "/")
soup = BeautifulSoup(page.content, 'html.parser')
othervals = []
othervals.append(soup.find_all('span', class_='num')[5].get_text())
othervals.append(soup.find_all('span', class_='num')[2].get_text())
print(str(soup.find_all('div', class_='big_num') + othervals))