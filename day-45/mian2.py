from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
data = response.text

soup = BeautifulSoup(data, 'html.parser')

all_votes = soup.find_all(name="span", class_="score")
titles = soup.select(selector=".titleline a")
links = soup.select(selector=".titleline a")

vote = [int(link.getText().split()[0]) for link in all_votes]
formated_title = [title.getText() for title in titles]
formated_link = [link.get("href") for link in links]

max_value = max(vote)
max_index = vote.index(max_value)


print(formated_title[max_index])
print(formated_link[max_index])
print(max_value)
print(max_index)

