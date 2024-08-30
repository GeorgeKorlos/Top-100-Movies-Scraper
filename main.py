import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

movies = soup.find_all(name='h3', class_='title')
titles = [movie.getText() for movie in movies]
titles = titles[::-1]

with open("movies.txt", 'w') as file:
    for title in titles: 
        file.write(f"{title}\n")