from selenium import webdriver
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import sys
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
import os

username = 'venoxforo@gmail.com'
    
password ='EHr3mPDZL'

number = sys.argv[1]

delay = 2;

CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')


options = uc.ChromeOptions()
options.binary_location = GOOGLE_CHROME_BIN
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
#options.headless = True

driver = uc.Chrome(executable_path=CHROMEDRIVER_PATH ,options=options)


driver.delete_all_cookies()
driver.get('https://accounts.google.com/ServiceLogin/identifier?elo=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
sleep(3)

driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)

driver.find_element_by_xpath('//*[@id="identifierNext"]').click()

sleep(2)

driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
sleep(2)
driver.get('https://voice.google.com/u/0/calls')
driver.find_element_by_id("il1").send_keys(number)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/ng-transclude/gv-make-call-panel-ng2/div/div[1]/button").click()
sleep(delay)
driver.execute_script('document.getElementsByClassName("gmat-button call-end-button mat-focus-indicator mat-icon-button mat-button-base")[0].click()')
sleep(1)
driver.get('https://voice.google.com/u/0/calls')
driver.find_element_by_id("il1").send_keys(number)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/ng-transclude/gv-make-call-panel-ng2/div/div[1]/button").click()
sleep(delay)
driver.execute_script('document.getElementsByClassName("gmat-button call-end-button mat-focus-indicator mat-icon-button mat-button-base")[0].click()')
sleep(1)
driver.get('https://voice.google.com/u/0/calls')
driver.find_element_by_id("il1").send_keys(number)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/ng-transclude/gv-make-call-panel-ng2/div/div[1]/button").click()
sleep(delay)
driver.execute_script('document.getElementsByClassName("gmat-button call-end-button mat-focus-indicator mat-icon-button mat-button-base")[0].click()')
sleep(1)
driver.get('https://voice.google.com/u/0/calls')
driver.find_element_by_id("il1").send_keys(number)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/ng-transclude/gv-make-call-panel-ng2/div/div[1]/button").click()
sleep(delay)
driver.execute_script('document.getElementsByClassName("gmat-button call-end-button mat-focus-indicator mat-icon-button mat-button-base")[0].click()')
sleep(1)
driver.get('https://voice.google.com/u/0/calls')
driver.find_element_by_id("il1").send_keys(number)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/ng-transclude/gv-make-call-panel-ng2/div/div[1]/button").click()
sleep(delay)
driver.execute_script('document.getElementsByClassName("gmat-button call-end-button mat-focus-indicator mat-icon-button mat-button-base")[0].click()')
sleep(1)
driver.get('https://voice.google.com/u/0/calls')
driver.find_element_by_id("il1").send_keys(number)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/ng-transclude/gv-make-call-panel-ng2/div/div[1]/button").click()
sleep(delay)
driver.execute_script('document.getElementsByClassName("gmat-button call-end-button mat-focus-indicator mat-icon-button mat-button-base")[0].click()')
sleep(1)
driver.get('https://voice.google.com/u/0/calls')
driver.find_element_by_id("il1").send_keys(number)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/ng-transclude/gv-make-call-panel-ng2/div/div[1]/button").click()
sleep(delay)
driver.execute_script('document.getElementsByClassName("gmat-button call-end-button mat-focus-indicator mat-icon-button mat-button-base")[0].click()')
sleep(1)
driver.get('https://voice.google.com/u/0/calls')
driver.find_element_by_id("il1").send_keys(number)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/ng-transclude/gv-make-call-panel-ng2/div/div[1]/button").click()
sleep(delay)
driver.execute_script('document.getElementsByClassName("gmat-button call-end-button mat-focus-indicator mat-icon-button mat-button-base")[0].click()')
sleep(1)
driver.get('https://voice.google.com/u/0/calls')
driver.find_element_by_id("il1").send_keys(number)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/ng-transclude/gv-make-call-panel-ng2/div/div[1]/button").click()
sleep(delay)
driver.execute_script('document.getElementsByClassName("gmat-button call-end-button mat-focus-indicator mat-icon-button mat-button-base")[0].click()')
sleep(1)
driver.get('https://voice.google.com/u/0/calls')
driver.find_element_by_id("il1").send_keys(number)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/ng-transclude/gv-make-call-panel-ng2/div/div[1]/button").click()
sleep(delay)
driver.execute_script('document.getElementsByClassName("gmat-button call-end-button mat-focus-indicator mat-icon-button mat-button-base")[0].click()')
sleep(1)
driver.get('https://voice.google.com/u/0/calls')
driver.find_element_by_id("il1").send_keys(number)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/ng-transclude/gv-make-call-panel-ng2/div/div[1]/button").click()
sleep(delay)
driver.execute_script('document.getElementsByClassName("gmat-button call-end-button mat-focus-indicator mat-icon-button mat-button-base")[0].click()')
sleep(1)
driver.get('https://voice.google.com/u/0/calls')
driver.find_element_by_id("il1").send_keys(number)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/ng-transclude/gv-make-call-panel-ng2/div/div[1]/button").click()
sleep(delay)
driver.execute_script('document.getElementsByClassName("gmat-button call-end-button mat-focus-indicator mat-icon-button mat-button-base")[0].click()')
sleep(1)
driver.get('https://voice.google.com/u/0/calls')
driver.find_element_by_id("il1").send_keys(number)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/ng-transclude/gv-make-call-panel-ng2/div/div[1]/button").click()
sleep(delay)
driver.execute_script('document.getElementsByClassName("gmat-button call-end-button mat-focus-indicator mat-icon-button mat-button-base")[0].click()')
sleep(1)
driver.get('https://voice.google.com/u/0/calls')
driver.find_element_by_id("il1").send_keys(number)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/gv-call-sidebar/div/gv-in-call/ng-transclude/gv-make-call-panel-ng2/div/div[1]/button").click()
sleep(delay)
driver.execute_script('document.getElementsByClassName("gmat-button call-end-button mat-focus-indicator mat-icon-button mat-button-base")[0].click()')
sleep(1)
