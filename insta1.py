from selenium import webdriver 
import time 

username1 = "Anujmor17" 
password1 = "yourpassword" 


# starts a new chrome session 
chrome = webdriver.Chrome("C:\Program Files\Chrome Driver\chromedriver.exe")
time.sleep(1)

#maximize the window size  
chrome.maximize_window()

#navigate to the url
chrome.get("https://www.instagram.com/")
time.sleep(4)

# finds the username box 
usern = chrome.find_element_by_name("username")     
# sends the entered username 
usern.send_keys(username1)    
  
# finds the password box 
passw = chrome.find_element_by_name("password")     
  
# sends the entered password 
passw.send_keys(password1)

time.sleep(2) 
  
# finds the login button 
log1 = chrome.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")     
log1.click()   # clicks the login button 
time.sleep(5) 

# finds the not now savelogin info button
notnowinfo= chrome.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")     
notnowinfo.click()   # clicks the not now button
time.sleep(5) 
                                                                                    
# finds the not now turn on notification button
notnownotification= chrome.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")     
notnownotification.click()   # clicks the not now button
time.sleep(5) 

#scrolling
chrome.execute_script("window.scrollBy(0,300)", "")
time.sleep(2) 
chrome.execute_script("window.scrollBy(0,300)", "")
time.sleep(2)
chrome.execute_script("window.scrollBy(0,300)", "")
time.sleep(2)
chrome.execute_script("window.scrollBy(0,300)", "")
time.sleep(2)
chrome.execute_script("window.scrollBy(0,300)", "")
time.sleep(2)
chrome.execute_script("window.scrollBy(0,300)", "")
time.sleep(2) 
chrome.execute_script("window.scrollBy(0,300)", "")
time.sleep(2)
chrome.execute_script("window.scrollBy(0,300)", "")
time.sleep(2)
chrome.execute_script("window.scrollBy(0,300)", "")
time.sleep(2)
chrome.execute_script("window.scrollBy(0,300)", "")
time.sleep(2)








