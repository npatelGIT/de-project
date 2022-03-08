from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_banks?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0221ENSkillsNetwork23455645-2021-01-01'
html_data = requests.get(url).text

soup = BeautifulSoup(html_data,"html.parser")

data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

for row in soup.find_all('tbody')[3].find_all('tr'):
    col = row.find_all('td')
    if (col != []):
        bank_name = col[1].text.strip()
        market_cap = col[2].text.strip()
        data = data.append({"Name":bank_name, "Market Cap (US$ Billion)":market_cap}, ignore_index=True)

print(data.head())