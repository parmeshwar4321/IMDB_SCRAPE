import json
from imdbmovie_scrap_task1 import *
def id_of_links(files):
    for i in files:
        a=i['links']
        filename=a[28:-1]
        f=open(filename+'.json','w')
        json.dump(i,f)
        f.close()
a=id_of_links(task1)

# print(a)