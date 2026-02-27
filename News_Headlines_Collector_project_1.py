import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.bbc.com/news"
response=requests.get(url)
soup=BeautifulSoup(response.text, "html.parser")

data=[]

article=soup.find_all("a", href=True)

for article in article :
    title=article.text.strip()
    link=article["href"]

    if title and "/news" in link:
        if link.startswith("/"):
            link=link = "https://www.bbc.com" + link
        data.append([title, "N/A", link])

df=pd.DataFrame(data, columns=["Title", "Date", "Link"])
df.drop_duplicates(inplace=True)
df.to_csv("bbc_headlines.csv", index=False)
print("Scraping Completed Successfully")