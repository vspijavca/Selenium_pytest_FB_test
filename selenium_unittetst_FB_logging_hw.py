from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

path = r'C:\Users\Slava\PycharmProjects\ls2_hw\chromedriver'
page = r'https:\\facebook.com'

class FacebookSignUp(unittest.TestCase):

	def setUp(self):
		print('Initializing ...')
		self.driver = webdriver.Chrome(path)
		self.driver.get(page)
	def test_if_logg_in_succesful(self):
		email = self.driver.find_element_by_id('email')
		email.send_keys('testinginbox1@gmail.com')
		time.sleep(3)
		password = self.driver.find_element_by_id('pass')
		password.send_keys('inboxtesting')
		password.send_keys(Keys.RETURN)
		time.sleep(3)
		q = self.driver.find_element_by_xpath('//input[@type="search"]')
		q.send_keys('Ion')
		q.send_keys(Keys.RETURN)
		time.sleep(6)

	def tearDown(self):
	    # close the driver objest
	    print('\nClean the resources for the test')
	    self.driver.close()
