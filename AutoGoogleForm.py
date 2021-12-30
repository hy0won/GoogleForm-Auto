from selenium import webdriver
import random

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

name = "NAME"
address = "ADDRESS"
num = "NUMBER"

browser=webdriver.Chrome(executable_path="D:\\Rproject\\chromedriver.exe", options=options)
browser.get("https://docs.google.com/forms/d/e/1FAIpQLSfgyq2PwHo8Kl1mZxdqxYGEgj8FDVfeKoulFX6SA7FDZVZCkA/viewform")

#텍스트 박스
textbox1 = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
textbox1.send_keys(name)

textbox2 = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
textbox2.send_keys(address)

textbox3 = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
textbox3.send_keys(num)

#라디오박스
radiobox = browser.find_element_by_xpath('//*[@id="i17"]')
radiobox.click()
#체크박스
checkbox = browser.find_element_by_xpath('//*[@id="i37"]')
checkbox.click()
#제출하기
submit = browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
submit.click()
