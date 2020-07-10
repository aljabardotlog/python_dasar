from bs4 import BeautifulSoup
import requests

def getnews():
    res=requests.get('https://makassar.terkini.id/')
    soup=BeautifulSoup(res.text, 'lxml')

    news_box=soup.find('div',{'class':'td-listview--title'})
    all_news=news_box.find_all('a')

    for news in all_news:
        link=str(news.prettify)

    news_a = link.split("<a href=")
    news_b = news_a[1]
    news_c = news_b.split("\"")
    newsn = news_c[1]

    return newsn

print (getnews());