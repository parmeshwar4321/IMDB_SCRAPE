from  task5 import *
from pprint import pprint
import json
def analyse_movie_lang(n):
    a,b,c,d,e=0,0,0,0,0
    for i in n:
        for j in i['language']:
            if j=='Bengali':
                a+=1
            elif j=='Hindi':
                b+=1

            elif j=='Tamil':
                c+=1

            elif j=='Malayalam':
                d+=1

            elif j=='Marathi':
                e+=1
    f={'Bengali':a,'hindi':b,'Tamil':c,'Malayalam':d,'Marathi':e}
    return f
pprint(analyse_movie_lang(ten_movies))
# f=open('task_6.json','w')
# json.dump(m,f,indent=4)
# f.close()