import win32api, win32con
import win32com.client
import config
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from tqdm import tqdm

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv/xls")
driver = webdriver.Firefox(firefox_profile=fp)

shell = win32com.client.Dispatch("WScript.Shell")

with open('Book1.txt','r') as f:
	list_of_dates = [i.replace('\n','') for i in f.readlines()]

parsed_list_of_dates = []
dict_of_dates = {}
timesrun = 0
def dict_builder():
	for date in list_of_dates:
		counter = list_of_dates.index(date)
		start = list_of_dates[counter]
		try:
			end = list_of_dates[counter + 1]
			dict_of_dates[start]=end
		except IndexError:
			continue

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def login():
    #Get config info
    url = config.get_url()
    username = config.get_user()
    password = config.get_password()

	driver.get(url)
	username = driver.find_element_by_id('LoginCtrl_txtLoginUsername')
	username.send_keys(username)
	password = driver.find_element_by_id('LoginCtrl_txtPassword')
	password.send_keys(password)
	login = driver.find_element_by_id('LoginCtrl_btnLogin').click()

def wait():
	search_hover = driver.find_element_by_xpath('//*[@id="ctl05_6"]')
	actions = ActionChains(driver)
	actions.move_to_element(search_hover).perform()
	sleep(3)
	driver.find_element_by_xpath('//*[@id="ctl05_26"]/tbody/tr/td[1]').click()
	sleep(2)
	click(347,409)
	sleep(2)
	click(467,248)
	sleep(1)
	shell.SendKeys("{DOWN}")
	shell.SendKeys("{DOWN}")
	shell.SendKeys("{DOWN}")
	shell.SendKeys("{DOWN}")
	shell.SendKeys("{DOWN}")
	for k,v in tqdm(dict_of_dates.iteritems()):
		click(459,327)
		shell.SendKeys("%s" % k)
		click(642,326)
		shell.SendKeys("%s" % v)
		click(558,370)
		sleep(2)
		click(758,423)
		sleep(5)
		if timesrun == 0:
			shell.SendKeys("{DOWN}")
			shell.SendKeys("{ENTER}")
		else:
			shell.SendKeys("{ENTER}")
		click(516,465)
		timesrun = timesrun + 1
		sleep(5)

def date_input(start_date,end_date):
	min_date = driver.find_element_by_xpath(
            '//*[@id="dvSearchParams"]/div/center/table/tbody/tr[3]/td[2]/nobr/input[1]'
        )
	min_date.send_keys(start_date)
	max_date = driver.find_element_by_xpath(
            '//*[@id="dvSearchParams"]/div/center/table/tbody/tr[3]/td[2]/nobr/input[2]'
        )
	max_date.send_keys(end_date)
	download_button = driver.find_element_by_xpath(
        '//*[@id="dvButtons"]/center/table/tbody/tr[1]/td[5]/input').click()
	sleep(3)

def downloader():
	for key in dict_of_dates:
		date_input(key,dict_of_dates[key])

if __init__ == '__main__':
    try:
    	dict_builder()
    	login()
    	wait()
    except Exception as e:
    	error_log = open('error_log.txt','w')
    	error_log.write(
                'Script failed on iteration %s with error %s' % (timesrun, e)
            )
