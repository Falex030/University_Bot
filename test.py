from selenium import webdriver
import time
import schedule

# give options
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("user-data-dir=./chromeprofile")
options.add_argument('--disable-extensions')
#options.add_argument("--incognito")
options.add_argument("--disable-plugins-discovery")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(r'C:\Users\Ilya\PycharmProjects\University_BOT\Chrome\chromedriver.exe',options=options)

url = 'https://meet.google.com/lookup/gy7njx5dia?authuser=1&hs=179'


''' first_second_lesson_monday
first - Номер тижня
second - пара по счоту

'''


first_monday = {
    'IT': 'https://meet.google.com/urb-rjsp-wqm',
    'Urkaine_Language': 'https://meet.google.com/lookup/axjfog62dw?authuser=1&hs=179'
}


def second_first_lesson_wednesday():
    try:
        driver.get(url='https://meet.google.com/urb-rjsp-wqm')
        time.sleep(20)
        time.sleep(3)
        off_micro = driver.find_element_by_xpath(
            '//div[@class="U26fgb JRY2Pb mUbCce kpROve uJNmj QmxbVb HNeRed"]').click()
        time.sleep(4)
        off_cam = driver.find_elements_by_xpath('//span[@class="DPvwYc JnDFsc dMzo5"]')
        off_cam[1].click()
        time.sleep(4)
        press_coninue = driver.find_element_by_xpath('//span[@class="NPEfkd RveJvd snByac"]').click()
        time.sleep(60)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


schedule.every().day.at("18:26").do(second_first_lesson_wednesday)


def second_second_lesson_wednesday():
    try:
        driver.get(url='https://meet.google.com/lookup/hvug6sxjey?authuser=1&hs=179')
        time.sleep(20)
        time.sleep(3)
        off_micro = driver.find_element_by_xpath(
            '//div[@class="U26fgb JRY2Pb mUbCce kpROve uJNmj QmxbVb HNeRed"]').click()
        time.sleep(4)
        off_cam = driver.find_elements_by_xpath('//span[@class="DPvwYc JnDFsc dMzo5"]')
        off_cam[1].click()
        time.sleep(4)
        press_coninue = driver.find_element_by_xpath('//span[@class="NPEfkd RveJvd snByac"]').click()
        time.sleep(40)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        time.sleep(20)
        driver.quit()


schedule.every().day.at("13:55").do(second_second_lesson_wednesday)


def second_third_lesson_wednesday():
    try:
        driver.get(url='https://meet.google.com/lookup/e6kettrs2b?authuser=1&hs=179')
        time.sleep(3)
        off_micro = driver.find_element_by_xpath(
            '//div[@class="U26fgb JRY2Pb mUbCce kpROve uJNmj QmxbVb HNeRed"]').click()
        time.sleep(4)
        off_cam = driver.find_elements_by_xpath('//span[@class="DPvwYc JnDFsc dMzo5"]')
        off_cam[1].click()
        time.sleep(4)
        press_coninue = driver.find_element_by_xpath('//span[@class="NPEfkd RveJvd snByac"]').click()
        time.sleep(30)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


schedule.every().day.at("14:39").do(second_third_lesson_wednesday)

while True:
    schedule.run_pending()
    time.sleep(1)
