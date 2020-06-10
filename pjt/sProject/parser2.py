import os

import django
from selenium import webdriver

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studentsProject.settings")

django.setup()

from aptmanager.models import apt


def parse_apt():
    driver = webdriver.Chrome('C:/chromedriver.exe')
    driver.implicitly_wait(1)
    driver.get('https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancListView.do')

    data_list = []
    for page in range(2, 5):
        for i in range(1, 10):
            li = driver.find_element_by_xpath('//*[@id="subContent"]/div[4]/table /tbody/tr[%s]/td[4]' % i)
            data_list.append(li.text)
        driver.find_element_by_xpath('//*[@id="paging"]/div/a[%s]' % page).click()
    return data_list

    driver.close()


if __name__ == '__main__':
    apt_data = parse_apt()
    for i in apt_data:
        apt(apt_name=i).save()
