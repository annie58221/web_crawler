import requests

resp = requests.get("https://www.dcard.tw/f/relationship")
posts = resp.json()

for post in posts:
    print("🎯 標題：", post["title"])
    print("🧵 內文預覽：", post["excerpt"])
    print("🔗 URL：", f"https://www.dcard.tw/f/{post['forumAlias']}/p/{post['id']}")
    print("-" * 50)
