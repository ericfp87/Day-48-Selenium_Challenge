from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
date = driver.find_elements_by_css_selector(".event-widget time")
names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(date)):
    events[n] = {
        "time": date[n].text,
        "name": names[n].text,
    }

print(events)







driver.quit()