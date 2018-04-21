from bs4 import BeautifulSoup

def studentList(nameList):
	directory = []
	for name in nameList:
		file = "C:/Users/brukb/Desktop/Second Semester/Python/virtualenv_2/scraping/"+name+".txt"
		with open(file, "r") as f:
		    src = f.read()
		soup = BeautifulSoup(src, 'html.parser')

		mytable = soup.find('div',class_="table_results")
		unis = soup.find_all('a',class_="mailto")
		# for i in range(len(unis)):
		# 	unstripped = str(unis[i])
		# 	stripped = unstripped.split("\">")[1].strip("</a>")
		tableBody = mytable.table.tbody
		rows = tableBody.find_all("tr")
		for i in range(len(rows)):
			person = []
			if i==0:
				continue
			# print(i)
			school = str(rows[i].find('div'))
			print(school)
			try: 
				school_stripped = school.split("<br/>")[1].strip("</div>'")
			except:
				school_stripped = "None"
			dept = rows[i].find('div',class_="tpad10")
			dept = str(dept)
			##print(dept)
			dept_split = dept.split(">")
			if len(dept_split)==6:
				dept = dept_split[4].strip("</div>")
			elif len(dept_split)==8:
				dept = dept_split[5].strip("</div>").strip("</a")
				
			tdd = str(rows[i].td)
			splitText = tdd.split(">")
			pretty = splitText[2].strip("</a")
			##print(pretty + ":     "+dept)
			# unstripped = str(unis[i-1])
			uni = str(rows[i].find("a",class_="mailto"))
			if uni=="None":
				stripped_uni="None"
			else:
				stripped_uni= uni.split("\">")[1].strip("</a>")
			# print(uni)
			# print("Uni length:",len(uni))	
			
			person.append(pretty)
			##person.append(dept)
			person.append(stripped_uni)
			person.append(school_stripped)
			directory.append(person)
			##print(person)
	by_school_directory = []
	for i in range(len(directory)):
		if directory[i][2] in ['Student, COLUMBIA COLLEGE','Student, FU FOUNDATN SCHL OF ENGINEERING &amp; APPLIED SCIENCE:UGRAD']:
			by_school_directory.append(directory[i])
	for i in by_school_directory:
		lname = i[0].split(",")[0]
		fname = i[0].split(",")[1].strip().split(" ")[0]
		i[0]=fname
		i.append(lname)
	
	##print(by_school_directory)
	return by_school_directory


