import clean
import simulate
import json

nameList = ["Ron","Tom","Mark","Paul","Veronica","Rediet","Shaniqua","Will",
"Herma","Sharon","Cory","Zack","David","Jessica","Jacob","Ruth","Zion","Louis",
"Rohan","Bill","Claire","Evan","Jordan","Kathy","Chaya","Sahar"]
simulate.printWeb(nameList)
studentList = clean.studentList(nameList)
# for i in 
# a={"a":"hello","hi":"missy"}
# with open("tryjson.txt","w") as f:
# 	json.dump(a,f)

studentDict={}
for i in range(len(studentList)):
	studentDict[studentList[i][0]]={"fname":studentList[i][0],"lname":studentList[i][3],
	"email":studentList[i][1],"school":studentList[i][2]}
print(studentDict)


with open("tryjson2.txt","w") as f:
	json.dump(studentDict,f)