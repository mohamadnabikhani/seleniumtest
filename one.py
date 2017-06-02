from selenium import webdriver



profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type",0)
profile.update_preferences()

driver = webdriver.Firefox(firefox_profile=profile)



driver.get('http://courses.iust.ac.ir/')

driver.close()
