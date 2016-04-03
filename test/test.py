#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
import sys
import time

url = "file://%s" % (os.path.join(os.getcwd(), sys.argv[1]))

driver = webdriver.Firefox()
driver.get(url)

time.sleep(10)

textarea = driver.find_element_by_id('info')
logs = textarea.get_attribute('innerHTML')

print "logs = %s" % logs

driver.close()
