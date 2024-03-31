import feedparser, datetime
import ssl

# SSL 인증서 검증 무시
ssl._create_default_https_context = ssl._create_unverified_context

tistory_uri="https://yeni-devnote.tistory.com/" 
feed = feedparser.parse(tistory_uri+"/rss")

markdown_text = """
### Hi there 👋   

### 📖   Interest   
     - FrontEnd
     - BackEnd
     - ...  


### 📕 Latest Blog Posts   

""" # list of blog posts will be appended here

lst = []


for i in feed['entries'][:3]:
#     dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
#     markdown_text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
#     markdown_text += f"{i['title']} {i['link']} <br>\n"
    markdown_text += f"<a href =\"{i['link']}\"> {i['title']} </a> <br>"


    print(i['link'], i['title'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()