import requests
from bs4 import BeautifulSoup
import json
# import pprint


def scrape_top_list():
    url = "https://www.imdb.com/india/top-rated-indian-movies/"
    page = requests.get(url)
    htmlc=page.content
    soup = BeautifulSoup(htmlc,"html.parser")
    # print(soup)
    div=soup.find("div",class_="lister")
    s=div.find("tbody",class_="lister-list")
    name=s.find_all("tr")
    top_movie=[]
    searial_number=1
    for i in name:
        details={}
        movie_name=i.find("td",class_="titleColumn").a.get_text()
        year=i.find("td",class_="titleColumn").span.get_text()
        rating=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        url=i.find("td",class_="titleColumn").a["href"]
        movie_url="https://www.imdb.com"+url
        details={"Position":searial_number,"Name":movie_name,"Year":int(year[1:5]),"Rating":float(rating),"URL":movie_url}
        searial_number+=1
        top_movie.append(details.copy())
        with open("task_1.json","w") as file:
            json.dump(top_movie,file,indent=2)
    return top_movie
scrape_top_list()