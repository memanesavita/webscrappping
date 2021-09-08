# from task1 import scrape_top_list
# import requests
# from task2 import scrape_top_list_1
# import json
# dec_arg=scrape_top_list()
# scrapped_data=scrape_top_list()
# movie_by_year=scrape_top_list_1(scrapped_data)
# print(movie_by_year)
# def group_by_decade(movies):
#     moviedec={}
#     list1=[]
#     for index in movies:
#         mod=index["Year"]%10
#         decade=index["Year"]-mod
#         if decade not in list1:
#             list1.append(decade)
#     list1.sort()
#     for i in list1:
#         moviedec[i]=[]
#     for i in moviedec:
#         dec10=i+9
#         for x in movies:
#             if int(x["Year"])<=dec10 and int(x["Year"])>=i:
#                 for v in movies:
#                     moviedec[i].append(v)
#         with open("task_3.json","w")as file:
#             json.dump(moviedec,file,indent=4)
#     return(moviedec)
# (group_by_decade(dec_arg))    
#  scrape_top_list_2(movie_by_year)



from task1 import scrape_top_list
from task2 import scrape_top_list_1
import json

scrapped_data=scrape_top_list()
movie_bye_year=scrape_top_list_1(scrapped_data)
def scrape_top_list_2(movie):
    moviedec={}
    list1=[]
    for year in movie:
        mod=year%10
        decade=year-mod
        if decade not in list1:
            list.append(decade)
    list1.sort()
    for i in list1:
        dec10=i+9
        for x in movie:
            if x<=dec10 and x>=i:
                for v in movie[x]:
                    moviedec[i].append(v)
        with open("task_3.json","w") as file:
            json.dump(moviedec,file,indent=4)
            return moviedec
    scrape_top_list_2(movie_bye_year)


















