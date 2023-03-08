from selenium import webdriver
from ID import Conf
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

ID=Conf["id"]
PWD=Conf["passwd"]
GRD=Conf["grd"]
CLS=Conf["cls"]
NUM=Conf["num"]

driver = webdriver.Firefox()
alrt = Alert(driver)
driver.get('https://www.dbdbschool.kr/member/login/sn/718')
driver.execute_script("document.getElementsByName('login_stu_name')[0].value=\'"+ ID +"\'")
driver.execute_script("document.getElementsByName('login_stu_passwd')[0].value=\'"+ PWD +"\'")
driver.execute_script("document.getElementsByName('login_stu_grade')[0].value=\'"+ GRD +"\'")
driver.execute_script("document.getElementsByName('login_stu_class')[0].value=\'"+ CLS +"\'")
driver.execute_script("document.getElementsByName('login_stu_bunho')[0].value=\'"+ NUM +"\'")
Login = driver.find_element(By.XPATH,"/html/body/form/div[2]/div/div[4]/p/input")
driver.execute_script("arguments[0].click();", Login)
time.sleep(0.9)
Tab = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/ul/li[2]/a")
driver.execute_script("arguments[0].click();", Tab)
time.sleep(0.9)
Sel1 = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[1]/table/tbody/tr[49]/td[2]/button")
driver.execute_script("arguments[0].click();", Sel1)
alrt.accept()
time.sleep(0.9)
Sel2 = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[1]/table/tbody/tr[51]/td[2]/button")
driver.execute_script("arguments[0].click();", Sel2)
alrt.accept()
time.sleep(0.9)
Sel2 = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[1]/table/tbody/tr[52]/td[2]/button")
driver.execute_script("arguments[0].click();", Sel2)
alrt.accept()
time.sleep(0.9)
Johwe = driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]/div/div/ul/li[2]/a")
driver.execute_script("arguments[0].click();", Johwe)
time.sleep(5)
driver.save_screenshot('Com.png')