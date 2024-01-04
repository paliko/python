from selenium import webdriver



# Initialize the webdriver (choose the appropriate one for your browser)
driver = webdriver.Chrome()  # For Chrome

# Navigate to a website
driver.get("https://example.com")

# Find an element by its CSS selector
element = driver.find_element_by_css_selector("h1")

# Extract and print the text of the element
print("Element Text:", element.text)

# Find an input element and type text into it
input_element = driver.find_element_by_name("q")  # Replace with the actual name of the input field
input_element.send_keys("Selenium")

# Submit the form
input_element.submit()

# Wait for a few seconds (you may need to adjust this based on your network speed)
driver.implicitly_wait(5)

# Close the browser
driver.quit()
