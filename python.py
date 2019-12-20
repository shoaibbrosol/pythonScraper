from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
resp = requests.get(url)
html_soup = BeautifulSoup(resp.content, 'html.parser')

links = [a.attrs.get('href') for a in html_soup.select('td.titleColumn a')]

# Lists to store the scraped data in
total_ratings = []
ratings = []
Budget  = []
Gross  = []
names = []

for ul in links:
 res = requests.get("https://www.imdb.com"+ul)
soup = BeautifulSoup(res.content, 'html.parser')
names.append(soup.find('div',class_='title_wrapper').h1.text)


test_df = pd.DataFrame({'movie': names,

})
print(test_df)
#test_df.to_csv(r'C:/Users/shoai/OneDrive/Desktop/imdbData.csv')
#test_df