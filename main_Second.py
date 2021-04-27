from selenium import webdriver
import time
import schedule
import logging

logging.basicConfig()
schedule_logger = logging.getLogger('main')
schedule_logger.setLevel(level=logging.DEBUG)

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
driver = webdriver.Chrome(r'C:\Users\Ilya\PycharmProjects\University_BOT\Chrome\chromedriver.exe', options=options)


# ДРУГИЙ ТИЖДЕНЬ

# Понеділок
def second_first_lesson_monday():
    try:
        driver.get(url = 'https://meet.google.com/lookup/gy7njx5dia?authuser=1&hs=179') # ОАІ
        time.sleep(3)
        off_micro = driver.find_element_by_xpath('//div[@class="U26fgb JRY2Pb mUbCce kpROve uJNmj QmxbVb HNeRed"]').click()
        time.sleep(4)
        off_cam = driver.find_elements_by_xpath('//span[@class="DPvwYc JnDFsc dMzo5"]')
        off_cam[1].click()
        time.sleep(4)
        press_coninue = driver.find_element_by_xpath('//span[@class="NPEfkd RveJvd snByac"]').click()
        time.sleep(4800)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
schedule.every().monday.at("09:33").do(second_first_lesson_monday)


def second_second_lesson_monday():
    try:
        driver.get(url = 'https://meet.google.com/urb-rjsp-wqm' ) # IT
        time.sleep(3)
        off_micro = driver.find_element_by_xpath('//div[@class="U26fgb JRY2Pb mUbCce kpROve uJNmj QmxbVb HNeRed"]').click()
        time.sleep(4)
        off_cam = driver.find_elements_by_xpath('//span[@class="DPvwYc JnDFsc dMzo5"]')
        off_cam[1].click()
        time.sleep(4)
        press_coninue = driver.find_element_by_xpath('//span[@class="NPEfkd RveJvd snByac"]').click()
        time.sleep(4800)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
schedule.every().monday.at("12:55").do(second_second_lesson_monday)

#Вівторок

def second_first_lesson_tuesday():
    try:
        driver.get(url = 'https://meet.google.com/lookup/hvug6sxjey?authuser=1&hs=179' ) # Фізика
        time.sleep(3)
        off_micro = driver.find_element_by_xpath('//div[@class="U26fgb JRY2Pb mUbCce kpROve uJNmj QmxbVb HNeRed"]').click()
        time.sleep(4)
        off_cam = driver.find_elements_by_xpath('//span[@class="DPvwYc JnDFsc dMzo5"]')
        off_cam[1].click()
        time.sleep(4)
        press_coninue = driver.find_element_by_xpath('//span[@class="NPEfkd RveJvd snByac"]').click()
        time.sleep(4800)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
schedule.every().tuesday.at("07:50").do(second_first_lesson_tuesday)

def second_second_lesson_tuesday():
    try:
        driver.get(url = 'https://meet.google.com/lookup/azjdvfzi4d?authuser=1&hs=179') # Математика
        time.sleep(3)
        off_micro = driver.find_element_by_xpath('//div[@class="U26fgb JRY2Pb mUbCce kpROve uJNmj QmxbVb HNeRed"]').click()
        time.sleep(4)
        off_cam = driver.find_elements_by_xpath('//span[@class="DPvwYc JnDFsc dMzo5"]')
        off_cam[1].click()
        time.sleep(4)
        press_coninue = driver.find_element_by_xpath('//span[@class="NPEfkd RveJvd snByac"]').click()
        time.sleep(4800)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


schedule.every().tuesday.at("09:35").do(second_second_lesson_tuesday)


# Середа

def second_first_lesson_wednesday():
    try:
        driver.get(url = 'https://meet.google.com/urb-rjsp-wqm' )
        time.sleep(3)
        off_micro = driver.find_element_by_xpath('//div[@class="U26fgb JRY2Pb mUbCce kpROve uJNmj QmxbVb HNeRed"]').click()
        time.sleep(4)
        off_cam = driver.find_elements_by_xpath('//span[@class="DPvwYc JnDFsc dMzo5"]')
        off_cam[1].click()
        time.sleep(4)
        press_coninue = driver.find_element_by_xpath('//span[@class="NPEfkd RveJvd snByac"]').click()
        time.sleep(4800)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
schedule.every().wednesday.at("07:50").do(second_first_lesson_wednesday)




def second_second_lesson_wednesday():
    try:
        driver.get(url= 'https://meet.google.com/lookup/hvug6sxjey?authuser=1&hs=179')
        time.sleep(3)
        off_micro = driver.find_element_by_xpath('//div[@class="U26fgb JRY2Pb mUbCce kpROve uJNmj QmxbVb HNeRed"]').click()
        time.sleep(4)
        off_cam = driver.find_elements_by_xpath('//span[@class="DPvwYc JnDFsc dMzo5"]')
        off_cam[1].click()
        time.sleep(4)
        press_coninue = driver.find_element_by_xpath('//span[@class="NPEfkd RveJvd snByac"]').click()
        time.sleep(4800)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
schedule.every().wednesday.at("09:35").do(second_second_lesson_wednesday)

def second_third_lesson_wednesday():
    try:
        driver.get(url='https://meet.google.com/lookup/e6kettrs2b?authuser=1&hs=179')
        time.sleep(3)
        off_micro = driver.find_element_by_xpath('//div[@class="U26fgb JRY2Pb mUbCce kpROve uJNmj QmxbVb HNeRed"]').click()
        time.sleep(4)
        off_cam = driver.find_elements_by_xpath('//span[@class="DPvwYc JnDFsc dMzo5"]')
        off_cam[1].click()
        time.sleep(4)
        press_coninue = driver.find_element_by_xpath('//span[@class="NPEfkd RveJvd snByac"]').click()
        time.sleep(4800)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


schedule.every().wednesday.at("11:15").do(second_third_lesson_wednesday)


# Четверг


def second_first_lesson_thursday():
    try:
        driver.get(url='') # English
        time.sleep(3)
        off_micro = driver.find_element_by_xpath('//div[@class="U26fgb JRY2Pb mUbCce kpROve uJNmj QmxbVb HNeRed"]').click()
        time.sleep(4)
        off_cam = driver.find_elements_by_xpath('//span[@class="DPvwYc JnDFsc dMzo5"]')
        off_cam[1].click()
        time.sleep(4)
        press_coninue = driver.find_element_by_xpath('//span[@class="NPEfkd RveJvd snByac"]').click()
        time.sleep(4800)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


schedule.every().thursday.at("12:55").do(second_first_lesson_thursday)

# Пятница

def second_first_lesson_friday():
    try:
        driver.get(url='https://meet.google.com/urb-rjsp-wqm') # IT
        time.sleep(3)
        off_micro = driver.find_element_by_xpath('//div[@class="U26fgb JRY2Pb mUbCce kpROve uJNmj QmxbVb HNeRed"]').click()
        time.sleep(4)
        off_cam = driver.find_elements_by_xpath('//span[@class="DPvwYc JnDFsc dMzo5"]')
        off_cam[1].click()
        time.sleep(4)
        press_coninue = driver.find_element_by_xpath('//span[@class="NPEfkd RveJvd snByac"]').click()
        time.sleep(4800)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

schedule.every().friday.at("07:55").do(second_first_lesson_friday)


while True:
    schedule.run_pending()
    time.sleep(1)