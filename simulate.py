from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def printWeb(nameList):
	driver = webdriver.Firefox(executable_path=r'C:\Users\brukb\Desktop\Second Semester\Python\virtualenv_2\geckodriver\geckodriver.exe')
	driver.get("https://directory.columbia.edu/people/search")
	assert "Columbia University" in driver.title
	for name in nameList:
		elem = driver.find_element_by_name("filter.searchTerm")
		elem.clear()
		elem.send_keys(name)
		search = driver.find_element_by_class_name("button2")
		text = search.text
		search.click()
		back1 = driver.find_elements_by_class_name("tpad10")
		back2 = driver.find_element_by_tag_name('html')
		print(len(back1))
		file = "C:/Users/brukb/Desktop/Second Semester/Python/virtualenv_2/scraping/"+name+".txt"
		with open(file, "w") as f:
			f.write(driver.page_source)
