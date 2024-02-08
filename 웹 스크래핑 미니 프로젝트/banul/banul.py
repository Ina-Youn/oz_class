from bs4 import BeautifulSoup
from selenium import webdriver

#셀레니움에 다양한 옵션을 적용시키기 위한 패키지
from selenium.webdriver.chrome.options import Options

#크롬 드라이버 매니저를 실행시키기 위해 설치해주는 패키지
from selenium.webdriver.chrome.service import Service
#자동으로 크롬 드라이브를 최신으로 유지해주는 패키지 
from webdriver_manager.chrome import ChromeDriverManager
#클래스, 아이디, css_selector를 이용하고자 할때
from selenium.webdriver.common.by import By
#키보드 입력
from selenium.webdriver.common.keys import Keys

import time

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

options_ = Options()
options_.add_argument(f"User-Agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])


#크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)

url = "https://www.banul.co.kr/"
driver.get(url)
time.sleep(0.5)

# 팝업창 닫기 버튼 클릭
driver.find_element(By.CSS_SELECTOR, ".btn-close").click()
time.sleep(3)

# 상단 카테고리 중 '실' 버튼 선택
driver.find_element(By.LINK_TEXT, "실").click()
time.sleep(0.5)

# 1~4페이지 까지 제품 정보 스크래핑
for i in range(1,5):
    url = f'https://www.banul.co.kr/shop/shopbrand.html?type=Y&xcode=107&sort=&page={i}'
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    time.sleep(5)

    items = soup.select(".item-list > .info")

    product_list = []
    for i in items:
        product = i.select_one(".pr_name").text
        price = i.select_one(".pr_price > strong").text
        review = str(str(i.select_one(".pr_review")).split(' : ')[-1]).split('<')[0]
        if review == None:
            review = 0

item = [product, price, review]
product_list.append(item)

driver.quit()

import pymysql

connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '123456789',
    db = 'banul',
    charset = 'utf8mb4'
)

connection.cursor()

def execute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args or())
        if query.strip().upper().startswith('SELECT'):
            return cursor.fetchall()
        else:
            connection.commit()

for i in product_list:
    execute_query(connection, "INSERT INTO banul (product, price, review) VALUES (%s, %s, %s)", (i[0],i[1],i[2]))
