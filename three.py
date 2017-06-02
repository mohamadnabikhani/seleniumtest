from selenium import webdriver
from selenium.webdriver.common.keys import Keys


profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type",0)
profile.update_preferences()

browser = webdriver.Firefox(firefox_profile=profile)

browser.get('http://www.google.com')
assert 'Google' in browser.title

elem = browser.find_element_by_name('q')  # Find the search box
elem.send_keys('selenium' + Keys.RETURN)

browser.quit()

