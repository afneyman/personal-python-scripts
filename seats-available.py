<<<<<<< HEAD
import config
from selenium import webdriver
=======
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
>>>>>>> f73b2d902a82763e102d6fcb2d64fc1c66146e56
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from twilio.rest import Client

<<<<<<< HEAD

# the following line needs your Twilio Account SID and Auth Token
client = Client(config.sid, config.token)
=======
# the following line needs your Twilio Account SID and Auth Token
client = Client("ACd528899d020e1f90c48c4698a3a3327c", "65108d97a895ad092ed0ef1a7d989f5a")
>>>>>>> f73b2d902a82763e102d6fcb2d64fc1c66146e56


desired_classes = ["eecs 345", "eecs 340", "math 307"]
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 5)


def wait_until_loads(id):
    wait = WebDriverWait(browser, 5)
    return wait.until(EC.element_to_be_clickable((By.ID, id)))


def check_loading():
    loadingid = 'WAIT_win1'
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located((By.ID, loadingid)))
    while browser.find_element_by_id(loadingid).is_displayed():
        # print('waiting')
        time.sleep(1)


def click_spring():
    sid = 'SSR_CSTRMCUR_GRD$0_row_1'
    check_loading()
    element = wait.until(EC.element_to_be_clickable((By.ID, sid)))
    # if you dont sleep an error will be caused
    element.click()


def setup():
    url = 'https://sisguest.case.edu/psc/P92SCWR_1/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL?Action=U&MD=Y&GMenu' \
          '=SSR_STUDENT_FL&GComp=SSR_START_PAGE_FL&GPage=SSR_START_PAGE_FL&1&scname=CS_SSR_MANAGE_CLASSES_NAV&ICAJAXTrf' \
          '=true'
    browser.get(url)
    click_spring()


# submitting the class search
def submit():
    sbid = 'CW_CLSRCH_WRK_SSR_PB_SEARCH'
    search_button = wait_until_loads(sbid)
    search_button.click()


# inputting thze class name
def search_for_class(name):
    searchID = 'CW_CLSRCH_WRK2_PTUN_KEYWORD'
    search = wait_until_loads(searchID)
    search.clear()
    search.send_keys(name)
    submit()
    return seats_available(name)


def seats_available(name):
    id = 'win1divCW_RSLT_NAV_WRK_HTMLAREA7$0'
    check_loading()
    el = wait_until_loads(id)
    return name + " " + el.text


# el = wait_until_loads('win1div$ICField$196$$0')
# val = int(el.text[27:29])
# print(val > 80)


setup()
text_string = []
splitter = '\n'
text_string.append(search_for_class('EECS 325'))
text_string.append(search_for_class('EECS 345'))
text_string.append(search_for_class('EECS 340'))
text_string.append(search_for_class('MATH 307'))

text = splitter.join(text_string)

<<<<<<< HEAD
client.messages.create(to=config.my_number,
                       from_=config.twilio_number,
                       body=text)

browser.quit()
=======
client.messages.create(to="+12165341514",
                       from_="+13172155488",
                       body=text)
>>>>>>> f73b2d902a82763e102d6fcb2d64fc1c66146e56
