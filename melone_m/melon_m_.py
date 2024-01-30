from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

#옵션 설정
options = Options()
user = "Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/121.0.0.0" 
options.add_argument('user-agent=' + user)
# options.add_argument(f"User-Agent={user}")
# options.add_argument("User-Agent=" + user)
options.add_argument("User-Agent = Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1")
# options.add_argument("user-agent=" + user)


options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)

#크롤링 코드 작성
url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(3)

if driver.current_url != url:
    driver.get(url)

driver.find_element(By.LINK_TEXT, "닫기").click()
time.sleep(3)

driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(3)

more_btn = driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click()
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".service_list.list_music > li")
#노래 순위
#노래 제목
#가수 이름

num = 1
for i in items:
    title = i.select_one(".title.ellipsis")
    singer = i.select_one(".name.ellipsis")
    print(f"{[num]}")
    print(f"노래 제목: {title.text.strip()}")
    print(f"가수: {singer.text.strip()}")
    print()
    num += 1

driver.quit()


