import requests
from bs4 import BeautifulSoup
import json

blog_id = 'tiger_bubu'
category_no = '6'

url = f"https://blog.naver.com/PostList.nhn?blogId={blog_id}&categoryNo={category_no}"
headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

posts = []
for a in soup.select("a.link_title"):
    title = a.get_text(strip=True)
    href = a['href']
    link = f"https://blog.naver.com{href}"
    posts.append({"title": title, "link": link})

with open("category6.json", "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)
