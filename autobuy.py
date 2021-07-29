from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# 買Momo網的Switch作為範例

# 設定webdriver環境
driver = webdriver.Chrome('/Users/Jun/Desktop/chromedriver')
driver.implicitly_wait(50)
driver.get('https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=8767194&Area=search&mdiv=403&oid=1_1&cid=index&kw=switch%E9%AD%94%E7%89%A9%E7%8D%B5%E4%BA%BA')

# 點擊購買按鈕跳轉到登入頁面
driver.find_element_by_css_selector('.buynow').click()
time.sleep(3)    
driver.find_element_by_id('memId').send_keys("xxxxxx") #account
driver.find_element_by_id('memId').send_keys(Keys.TAB)
pwd = driver.find_element_by_id('passwd')
pwd.send_keys("xxxxx") #password

# 跳轉頁面至結帳區
driver.find_element_by_css_selector('.loginBtn').click()
time.sleep(3)
driver.find_element_by_css_selector('.checkoutBtn').click()

#選擇付款方式
driver.find_element_by_css_selector('#linepay15').click()

#結帳
driver.find_element_by_css_selector('#orderSave') #需要結帳的話加入.click() 
