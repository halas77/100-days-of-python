from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

data = response.text

soup = BeautifulSoup(data, "html.parser")

movie_titles = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")


# formated = [title.getText().split()[1] for title in movie_titles] 
# print(formated)


with open("./day-45//movies.txt", 'w') as file:
    for title in movie_titles[::-1]:

        file.write(title.getText())

        file.write("\n")