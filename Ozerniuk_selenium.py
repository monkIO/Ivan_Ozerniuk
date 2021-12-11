#!/usr/bin/env python
# coding: utf-8

# In[39]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


# getting driver
s = Service('/Users/i.ozerniuk/downloads/chromedriver')
browser = webdriver.Chrome(service=s)

# logging in
browser.get('https://opensource-demo.orangehrmlive.com/')
browser.find_element(By.NAME, 'txtUsername').send_keys('Admin')
browser.find_element(By.NAME, 'txtPassword').send_keys('admin123' + Keys.ENTER)

# adding new grade
browser.get('https://opensource-demo.orangehrmlive.com/index.php/admin/viewPayGrades')
browser.find_element(By.ID, 'btnAdd').click()
browser.find_element(By.ID, 'payGrade_name').send_keys('Grade_RandomName')
browser.find_element(By.ID, 'btnSave').click()
browser.find_element(By.ID, 'btnAddCurrency').click()
browser.find_element(By.ID, 'payGradeCurrency_currencyName').send_keys('UAH - Ukraine Hryvnia' + Keys.ENTER)
browser.find_element(By.ID, 'payGradeCurrency_minSalary').send_keys('1000')
browser.find_element(By.ID, 'payGradeCurrency_maxSalary').send_keys('1000000')
browser.find_element(By.ID, 'btnSaveCurrency').click()

# checking grade visibility
browser.get('https://opensource-demo.orangehrmlive.com/index.php/admin/viewPayGrades')
rows_list = browser.find_element(By.ID, 'resultTable').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
is_found = False
row_to_delete = None
for row in rows_list:
    cols_list = list(map(lambda x: x.text, row.find_elements(By.TAG_NAME, 'td')))  
    if cols_list[1]=='Grade_RandomName' and cols_list[2]=='Ukraine Hryvnia':
        is_found = True
        row_to_delete = row
        break
        
# displaying result and deleting created grade
if is_found:
    print("The element was successfully added and displayed!")
    row_to_delete.find_element(By.TAG_NAME, 'input').click()
    browser.find_element(By.ID, 'btnDelete').click()
    browser.find_element(By.ID, 'dialogDeleteBtn').click()
else:
    print("Added element NOT FOUND on the page!")


browser.close()

