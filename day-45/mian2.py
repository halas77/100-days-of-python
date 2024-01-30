from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
data = response.text

soup = BeautifulSoup(data, 'html.parser')

title = soup.select_one(selector=".titleline a").getText()
link = soup.select_one(selector=".titleline a").get("href")
link = soup.find(name="span", class_="score").getText()

print(link)




