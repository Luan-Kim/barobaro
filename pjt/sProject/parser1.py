import os

import django
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studentsProject.settings")

django.setup()

from barobaro.models import japanese_food, korean_food, chinese_food


def kor_parse_store():
    driver = webdriver.Chrome("C:/chromedriver.exe")

    driver.get("https://map.kakao.com/")
    driver.implicitly_wait(5)

    element = "대전 한식"
    search_box = driver.find_element_by_id("search.keyword.query")
    search_box.send_keys(element)
    search_box.send_keys(Keys.ENTER)

    data_list = []
    for i in range(1, 12):
        if i != 4:
            store = driver.find_element_by_xpath(
                '// *[ @id="info.search.place.list"] / li[%s] / div[3] / strong / a[2]' % i)
            data_list.append(store.text)

    data_list = list(set(data_list))

    return data_list

    driver.close()


def jp_parse_store():
    driver = webdriver.Chrome("C:/chromedriver.exe")

    driver.get("https://map.kakao.com/")
    driver.implicitly_wait(5)

    element = "대전 일식"
    search_box = driver.find_element_by_id("search.keyword.query")
    search_box.send_keys(element)
    search_box.send_keys(Keys.ENTER)

    data_list = []
    for i in range(1, 12):
        if i != 4:
            store = driver.find_element_by_xpath(
                '// *[ @id="info.search.place.list"] / li[%s] / div[3] / strong / a[2]' % i)
            data_list.append(store.text)

    data_list = list(set(data_list))

    return data_list

    driver.close()


def cn_parse_store():
    driver = webdriver.Chrome("C:/chromedriver.exe")

    driver.get("https://map.kakao.com/")
    driver.implicitly_wait(5)

    element = "대전 중식"
    search_box = driver.find_element_by_id("search.keyword.query")
    search_box.send_keys(element)
    search_box.send_keys(Keys.ENTER)

    data_list = []
    for i in range(1, 12):
        if i != 4:
            store = driver.find_element_by_xpath(
                '// *[ @id="info.search.place.list"] / li[%s] / div[3] / strong / a[2]' % i)
            data_list.append(store.text)

    data_list = list(set(data_list))

    return data_list

    driver.close()


if __name__ == '__main__':
    store_data = cn_parse_store()
    for i in store_data:
        chinese_food(Restaurant_name=i).save()
