import requests
from bs4 import BeautifulSoup


url = "https://www.naver.com"

# 1. 원하는 사이트에 요청을 보낸다.
# 그리고, 그 결가를 response에 저장한다.
response = requests.get(url)


# 2. 원하는 정보를 찾는다.
soup = BeautifulSoup(response.text,'html.parser')

# 3. Select는 Css의 선택(selector)을 통해 찾을 수 있다.
# #KOSPI_now : id가 KOSPI_now인 것을 뜻함.
# .up : class가 up인 것을 뜻함.
# css에서 id는 문서에서 하나, class는 여러개가 있을 수 있다.
naver = soup.select('.ah_roll')
sets = naver[0].select('.ah_k')
for tag in sets:
    print(tag.text)

