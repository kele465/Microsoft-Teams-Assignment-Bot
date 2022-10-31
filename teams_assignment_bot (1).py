#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import random
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# In[ ]:


email = ''
password = ''


# In[2]:


executable_path="chromedriver.exe"
driver = webdriver.Chrome(executable_path)

driver.get("https://login.microsoftonline.com/common/oauth2/v2.0/authorize?response_type=id_token&scope=openid%20profile&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=eyJpZCI6ImFkMGIyOTJjLTQyNGItNDI5YS04NjVlLWJkNzcxNDMwMmVhZSIsInRzIjoxNjY3MTY4MTEwLCJtZXRob2QiOiJyZWRpcmVjdEludGVyYWN0aW9uIn0%3D&nonce=da982189-a6be-4a2a-8cf9-a2158b5f95b7&client_info=1&x-client-SKU=MSAL.JS&x-client-Ver=1.3.4&client-request-id=0b4659df-0d37-42d1-94cf-9d9017f331f3&response_mode=fragment")
time.sleep(5)


# In[3]:


email = driver.find_element(By.CSS_SELECTOR, "input[name='loginfmt']")
email.send_keys(email)
time.sleep(2)


# In[4]:


email_submit = driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(5)


# In[5]:


password = driver.find_element(By.CSS_SELECTOR, "input[name='passwd']")
password.send_keys(password)
time.sleep(2)


# In[ ]:


password_submit = driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(2)


# In[ ]:


stay_sign = driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()
time.sleep(2)


# In[ ]:


select_account = driver.find_element(By.CLASS_NAME, "table").click()
time.sleep(2)


# In[ ]:


assignment = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Assignments Toolbar']").click()
time.sleep(2)


# In[ ]:


# select_assignment = driver.find_element(By.XPATH, '//*[@id="list-view-current-day"]/div/div').click()
# time.sleep(2)

click_assignment = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div')))
click_assignment.click()



# In[ ]:


# download_assignment = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="assignmentViewerVisibilityContainer"]/div[2]/div/div[1]/div[3]/div/div/div/div/div/button[2]/span/svg')))
# download_assignment.click()


# In[ ]:




