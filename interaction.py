from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
#
# articlecount = driver.find_element_by_css_selector("#articlecount a")
# articlecount.click()
#
# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()
#
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

###############################################################################################################

driver.get("http://secure-retreat-92358.herokuapp.com/")

name = driver.find_element_by_name("fName")
name.send_keys("Nome")
name.send_keys(Keys.TAB)

name2 = driver.find_element_by_name("lName")
name2.send_keys("Sobrenome")
name2.send_keys(Keys.TAB)

email = driver.find_element_by_name("email")
email.send_keys("email@email.com.br")

button = driver.find_element_by_class_name("btn")
button.click()

# driver.quit()