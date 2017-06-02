import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):

		self.profile = webdriver.FirefoxProfile()
		self.profile.set_preference("network.proxy.type",0)
		self.profile.update_preferences()
		self.browser = webdriver.Firefox(firefox_profile=self.profile)
		self.addCleanup(self.browser.quit)

    def testPageTitle(self):

		self.browser.get('http://www.google.com')
		self.assertIn('Google', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)