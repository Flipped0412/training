import requests
import json

BASE = "http://www.aladin.co.kr/ttb/api/ItemList.aspx"
params = {
    "ttbkey": "ttbjunjjang04121326001",
    "QueryType": "ItemNewSpecial",   # 주목할 만한 신간
    "MaxResults": 50,                # 최대 50
    "start": 1,
    "SearchTarget": "Book",          # 도서 한정
    "output": "js",                  # JSON 응답
    "Version": "20131101"
}

res = requests.get(BASE, params=params)
res.raise_for_status()
payload = res.json()                     # {"item": [...]} 형태

items = payload.get("item", [])
result = []
for it in items:
    # 알라딘 응답 필드명 매핑 (매뉴얼 기준)
    title = it.get("title")
    author = it.get("author")
    pubdate = it.get("pubDate") or it.get("pubdate")  # 응답 변형 대비
    isbn13 = it.get("isbn13")
    isbn10 = it.get("isbn")

    result.append({
        "책 제목": title,
        "저자": author,
        "출간일": pubdate,                   # 예: "2025-09-10" 또는 "2025-09-10T00:00:00"
        "국제 표준 도서 번호": isbn13 or isbn10
    })

print(json.dumps(result, ensure_ascii=False, indent=2))
