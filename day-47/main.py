from bs4 import BeautifulSoup
import requests
import lxml

BASE_URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"


headers = { 'Accept-Language' : "en-US,en;q=0.9,am;q=0.8,om;q=0.7,ti;q=0.6",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
            'sec-ch-ua':'"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
            "Accept-Encoding":"gzip, deflate, br"
            }


response = requests.get(BASE_URL, headers=headers)
data = response.text

soup = BeautifulSoup(data, "lxml")
price = soup.find(name='span', class_="a-offscreen" )

print(price)
