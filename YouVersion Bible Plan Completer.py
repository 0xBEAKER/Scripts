# This script automates the process of completing a range of days on a YouVersion bible reading plan
# Date: 31 Jan 23

from selenium import webdriver
from selenium.webdriver.common.by import By

# User defined variables
start_day = 229 # First day of plan to mark complete
stop_day = 284 # Last day of plan to mark complete
reading_plan_url = "https://my.bible.com/users/username/reading-plans/12345-reading-plan-name/subscription/123456789/day/"

# Start the web drive
driver = webdriver.Firefox()

# Go to the website
driver.get("https://www.bible.com/sign-in")

# Login
username = driver.find_element(By.ID, "signin-username")
username.send_keys("username")
password = driver.find_element(By.ID, "signin-password")
password.send_keys("password")
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/article/div/div/form[3]/p[5]/button").click()

# Loop from start_day to stop_day
for day in range(start_day, stop_day):

    # Go to the reading plan page
    url = reading_plan_url + str(day)
    print (url)
    driver.get(url)
    driver.get(url)
    bullets = driver.find_elements(By.XPATH, "/html/body/div[2]/div/div/div/div[4]/div[3]/div/ul")

    i = 2
    for b in bullets:
        print (b.text)
        i += b.text.count('\n')

    print (i)

    for x in range(1,i):
        xpath = "/html/body/div[2]/div/div/div/div[4]/div[3]/div/ul/li[" + str(x) +"]/a[1]"
        print (xpath)
        checkbox = driver.find_element(By.XPATH, xpath).click()