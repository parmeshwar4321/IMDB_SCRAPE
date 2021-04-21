from imdbmovie_scrap_task1 import *
from pprint import pprint


def movis(a):
    realeas_yr=[]
    for i in a:
        if i['years'] not in realeas_yr:
            realeas_yr.append(i['years'])
    realeas_yr=sorted(realeas_yr)
    movie_dict={i:[] for i in realeas_yr}
    for i in a:
        yr=i['years']
        for x in movie_dict:
            if str(x)==str(yr):
                movie_dict[x].append(i)
    return movie_dict
c=movis(task1)
# pprint(c)
# f=open('task2.json','w')
# json.dump(c,f,indent=4)
# f.close()

    