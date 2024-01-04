from selenium import webdriver

firefox_binary = '/home/paulie/projects/python/selenium/setup'
options = webdriver.FirefoxOptions()
options.binary_location = firefox_binary

driver = webdriver.Firefox(executable_path="/home/paulie/projects/python/selenium/setup", firefox_options=options)
