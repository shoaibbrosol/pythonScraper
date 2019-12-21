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
budget  = []
gross  = []
names = []
genre = []

for ul in links:
	res = requests.get("https://www.imdb.com"+ul)
	soup = BeautifulSoup(res.content, 'html.parser')
	names.append(soup.find('div',class_='title_wrapper').h1.text)
	ratings.append(soup.find('div',class_='ratingValue').strong.span.text)
	total_ratings.append(soup.find('span',itemprop='bestRating').text)
	gr=soup.find_all('div',class_='see-more inline canwrap')
	genre.append(gr[1].a.text)
	bu=soup.find_all('div',class_='txt-block')
	b=bu[9].get_text(strip=True)
	b1 = b.replace('Budget:','')
	b2 = b1.replace('(estimated)','')
	b3 = b2.replace('Gross USA:','')
	b4 = b3.replace('Opening Weekend USA:','')
	budget.append(b4.replace(',11 January 2004',''))
	g = bu[11].get_text(strip=True)
	g1 = g.replace('Gross USA:','')
	g2 = g1.replace('Production Co:Vinod Chopra ProductionsSee more»','0')
	g3 = g2.replace('Production Co:Orion-Nova ProductionsSee more»','0')
	gross.append(g3.replace('Cumulative Worldwide Gross:',''))


test_df = pd.DataFrame({'movie': names,
'ratings': ratings,
'total_ratings': total_ratings,
'genre': genre,
'budget':budget,
'gross': gross
})
print(test_df)
test_df.to_csv(r'C:/Users/shoai/OneDrive/Desktop/imdbData.csv')
#test_df
