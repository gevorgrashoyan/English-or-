import json

def displayAllSchools(schools):
	print("")
	for current_school in schools:
		for current_key in current_school:
			print(current_key, ":", current_school[current_key])


def getNumericInput(displayString):
    while(True):
        user_data = input(displayString)
        if(user_data.isnumeric()):
            user_data = int(user_data)
            return user_data
        else:
            print("Please insert a number")

def addSchool(): 
    school = {
        "SchoolName" : "",
        "num_of_studentsRightNow" : 0,
	"num_of_studentsTillNow" : 0,
        "num_of_LanguagesTaught" : 0,
        "LanguageInfo" : {
		"language_name" : "",
		"goup_info" : {
			"num_of_groups" : 0,
			"num_of_studentsInEach" : 0,
			"entire_num_of_studets" : 0 {
				"num_of_StudentsInLevel" : { 
					"A1" : 0,
					"A2" : 0,
					"B1" : 0,
					"B2" : 0,
					"C1" : 0
					"C2" : 0
			}
		}
		"num_of_teachers" : 0,
		"price_of_theCourse" : 0
	},
        "average_age" : 0,
        "Month_Data" : {
                "finish" : 0,
                "start" : 0
        } : []

    school["SchoolName"] = input("Please insert the name of the school: ")
    school["num_of_studentsRightNow"] = getNumericInput("Please insert the number of students currently studying in this school: ")
    school["num_of_studentsTillNow"] = getNumericInput("Please insert the number of students that this school has ever had: ")
    school["num_of_LanguagesTaught"] = getNumericInput("Please insert the number of languages that are being taught now in the school: ")
    school["LanguageInfo"] = 
    school["average_age"] = getNumericInput("Please insert the avarage age of school members: ")
    school["Month_Dataw"] = 

def loadExistingSchools():
    with open('schools.json') as file_data:
        print(file_data)
        schools = json.load(file_data)
        return schools

def saveToTheFile(schools):
    f = open("schools.json", "w")
    f.write(json.dumps(schools, indent=2))
    f.close()

def main():
    schools = []
  
    schools = loadExistingSchools()

    while(True):
        insert_mode = input("Do you want to start adding schools?, please answer yes or no")
        if(insert_mode == "no"):
            print("Goodbye")
            break
        else:
            school = addSchool()
            schools.append(school)

    print("Saving to the file")
    saveToTheFile(schools)
    displayAllSchools(schools)

main()
