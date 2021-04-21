from task5 import*
def analyse_directors(direct):
    a,b,c=0,0,0
    for i in direct:
        for j in i['director']:
            if j=='Hrishikesh Mukherjee':
                a+=1
            elif j=='Satyajit Ray':
                b+=1
            elif j=='Rajkumar Hirani':
                c+=1
    f={'Hrishikesh Mukherjee':a,'Satyajit Ray':b,'Rajkumar Hirani':c}
    return f
m=analyse_directors(ten_movies)
print(m)
f=open('task_7.json','w')
json.dump(m,f,indent=4)
f.close()