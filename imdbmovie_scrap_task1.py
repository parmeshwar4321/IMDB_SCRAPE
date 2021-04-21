from bs4 import BeautifulSoup
import requests,json,pprint
import pandas as pd
# from IPython.display import display
def scrap_top_list():
    url ="https://www.imdb.com/india/top-rated-indian-movies/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text,"html.parser")
    data = soup.find("tbody",class_="lister-list").findAll("tr")
    movies , rateing , years , position ,links= [],[],[],[],[]
    for movie in data:
        movies.append(movie.find("td",class_="titleColumn").find("a").get_text())
        rate = (movie.find("td",class_="ratingColumn imdbRating").text)
        rateing.append(float(rate.strip()))
        years.append(int(movie.find("span",class_="secondaryInfo").text[1:5]))
        position.append(int(movie.text.strip().split('.')[0]))
        links.append('https://www.imdb.com/'+movie.find('a').get('href'))
    return page_info(movies,rateing,years,position,links)
def page_info(movies,rateing,years,position,links):
    d={}
    top_250_movieas = []
    for i,j,k,l,m in zip(movies,rateing,links,years,position):
        d['name'] = i
        d['rating'] = j
        d['links'] = k
        d['years'] = l
        d['postion'] = m
        top_250_movieas.append(d.copy())
    f=open('first_task.json','w')
    json.dump(top_250_movieas,f,indent=4)
    f.close()
    return top_250_movieas
task1=scrap_top_list()
# df=pd.DataFrame(task1)
# display(df,sorted)
# print(task1)









