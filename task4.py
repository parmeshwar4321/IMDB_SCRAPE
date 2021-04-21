import json,requests
from pprint import pprint
from bs4 import BeautifulSoup
from imdbmovie_scrap_task1 import *
def scrape_movie_details(a):
    for j in task1:
        urls=j['links']
        res=requests.get(urls)
        soup=BeautifulSoup(res.text,'html.parser')
        main=soup.find('div',class_="title-overview")
        sub=main.find(id="title-overview-widget").find(class_='subtext')
        directors=[main.find(class_="credit_summary_item").text[11:].strip()]
        genre=[]
        for h in sub.find_all('a'):
            a=h.text
            if a.isalpha():
                genre.append(h.text)
        country=sub.find_all('a')[-1].get_text().strip().split()[3][1:6]
        poster="https://www.imdb.com"+main.find(class_="poster").find('a').get('href')
        bio=main.find(class_="summary_text").text.strip()
        lang=soup.find(class_="article",id="titleDetails").find_all('div')
        for i in lang:
            la=i.find_all('h4')
            for k in la:
                if "Language:" in k:
                    aa=i.find_all('a')
                    languag=[language.get_text()for language in aa]
        time=sub.find('time').text.strip()
        runtimes=int(time[0])*60
        if 'min' in time:
            runtimes+=int(time[3:].strip('min'))
        d={'name':j['name'],'director':directors,'country':country,'language':languag,'postar_img_url':poster,'bio':bio,'runtime':runtimes,'genre':genre}
        return d
        f=open('task_4.json','a')
        json.dump(d,f,indent=4)
        f.close()
print(scrape_movie_details(task1))

