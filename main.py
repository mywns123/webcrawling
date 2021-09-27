import time
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# req = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
# html = req.text
# soup = BeautifulSoup(html, 'html.parser')

# result = soup.find_all('td', 'title')
# movie_rank = []
# for i in range(len(result)):
#     print("{:2}위 : {}".format(i + 1, result[i].get_text().strip()))
# movie_rank.append(i.find('a')['title'])

test = input('검색할 이름을 입력하세요 : ')

path = 'C:/chromedriver/chromedriver'
driver = webdriver.Chrome(path)
driver.get('https://www.youtube.com')

time.sleep(1)

element = driver.find_element_by_name("search_query")
# element = driver.find_element_by_id("search")
element.send_keys(test, Keys.ENTER)

# time.sleep(1)

# image_link = driver.find_element_by_link_text("이미지")
# image_link.click()
#
# time.sleep(1)
#
# # 네이버용
# image_tag = driver.find_elements_by_tag_name('section> div> div> div> div> div> div> a> img')

# 구글용
# image_tag = driver.find_elements_by_tag_name('span > div > div > div > a > div > img')
# image_tag = driver.find_elements_by_class_name('Q4LuWd')

# time.sleep(1)
#
# image_list = []
#
#
# for i in range(len(image_tag)):
#     image_list.append(image_tag[i].get_attribute('src'))
# print(image_list)
#
# for i, link in enumerate(image_list):
#     urlretrieve(link, './images/{}{}.jpg'.format(test, i+1))
