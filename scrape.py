import requests
from bs4 import BeautifulSoup
import pandas as pd

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
company_name=[]
rating=[]
reviews=[]
salary=[]
interviews=[]
jobs=[]
photos=[]
for page in range(1,201):
  company= requests.get(f'https://www.ambitionbox.com/list-of-companies?page={page}',headers=headers).text
  soup=BeautifulSoup(company,'lxml')
  # cards
  cards=soup.find_all('div',class_='companyCardWrapper')
  
  for card in cards:
    company_name.append(card.find('h2').text.strip())
    rating.append(card.find('span',class_='companyCardWrapper__companyRatingValue').text)
    reviews.append(card.find_all('span',class_='companyCardWrapper__ActionCount')[0].text)
    salary.append(card.find_all('span',class_='companyCardWrapper__ActionCount')[1].text)
    interviews.append(card.find_all('span',class_='companyCardWrapper__ActionCount')[2].text)
    jobs.append(card.find_all('span',class_='companyCardWrapper__ActionCount')[3].text)
    photos.append(card.find_all('span',class_='companyCardWrapper__ActionCount')[5].text)

data={
    'company_name':company_name,
    'rating':rating,
    'reviews':reviews,
    'salary':salary,
    'n_interviews':interviews,
    'n_jobs':jobs,
    'n_photos':photos
}
df= pd.DataFrame(data)

print(df)