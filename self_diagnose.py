from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('./chromedriver.exe')

driver.get("https://eduro.jne.go.kr/stv_cvd_co00_010.do")

driver.implicitly_wait(3)

driver.find_element_by_id("pName").send_keys("윤재진")
driver.find_element_by_id("qstnCrtfcNo").send_keys("9LSWVY")

driver.find_element_by_id("btnConfirm").click()


selectGrade = Select(driver.find_element_by_id("srchGrade"))
selectGrade.select_by_visible_text("1학년")


selectClass = Select(driver.find_element_by_id("srchClassCode"))
selectClass.select_by_visible_text("7차일반 / 2반")

driver.find_element_by_id('btnDtlSearch').click()