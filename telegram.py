import requests
import os #operation system에 접근

token = os.getenv("TELEGRAM_TOKEN")

url = f"https://api.telegram.org/bot{token}/getUpdates"

# 1. 요청을 보낸 결과를 response 변수에 저장을 한다.
response = requests.get(url)

# 2. json 형식으로 바꾼다.
# 지금은 dictionary와 list 섞여 있는 것과 같다고 생각하자.
updates = response.json()

# 3. user의 id를 찾는다.
user_id = updates["result"][0]["message"]["from"]["id"]

# 4. 메시지를 설정한다.
msg = "haoaoaoaoaoaoa?"
url = f"https://api.telegram.org/bot{token}/sendMessage?text={msg}&chat_id={user_id}"

# 5. 메시지를 보낸다.
requests.get(url)
