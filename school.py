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
            print("Please insert a number only")

def check_for_school(SchoolName, schools):
    for school in schools:
        s = school["SchoolName"]
        if(SchoolName == s):
            return school

def addLanguage():
    language = {
	"language_name": "",
	"num_of_teachers": 0,
	"price_of_theCourse": 0,
	"group_info": {
		"num_of_groups": 0,
		"num_of_studentsInEach": 0,
		"entire_num_of_students": {
			"EntireNum_of_students": 0,
			"num_of_StudentsInLevel": {
				"A1": 0,
				"A2": 0,
				"B1": 0,
				"B2": 0,
				"C1": 0,
				"C2": 0
				}
			}
		},		
	"average_age": 0,
	"StartFinishNUmber": {
		"just_started": 0,
		"isaboutto_finish": 0
		}
    }
    	
    language["language_name"] = input("Please insert the name of the lanuage: ")
    language["num_of_teachers"] = getNumericInput("Please insert the number of teachers teaching this language: ")
    language["price_of_theCourse"] = getNumericInput("Please insert the price of the course: ")
    language["group_info"]["num_of_groups"] = getNumericInput("Please insert the number of groups studying the language: ")
    language["group_info"]["num_of_studentsInEach"] = getNumericInput("Please insert the number of students in each group: ")
    language["group_info"]["entire_num_of_students"]["EntireNum_of_students"] = getNumericInput("Please insert the entire number of students studying this language: ")
    language["group_info"]["entire_num_of_students"]["num_of_StudentsInLevel"]["A1"] = getNumericInput("Please insert the number of students studying A1 level: ")
    language["group_info"]["entire_num_of_students"]["num_of_StudentsInLevel"]["A2"] = getNumericInput("Please insert the number of students studying A2 level: ")
    language["group_info"]["entire_num_of_students"]["num_of_StudentsInLevel"]["B1"] = getNumericInput("Please insert the number of students studying B1 level: ")
    language["group_info"]["entire_num_of_students"]["num_of_StudentsInLevel"]["B2"] = getNumericInput("Please insert the number of students studying B2 level: ")
    language["group_info"]["entire_num_of_students"]["num_of_StudentsInLevel"]["C1"] = getNumericInput("Please insert the number of students studying C1 level: ")
    language["group_info"]["entire_num_of_students"]["num_of_StudentsInLevel"]["C2"] = getNumericInput("Please insert the number of students studying C2 level: ")
    language["average_age"] = getNumericInput("Please insert the avarage age of the students: ")
    language["StartFinishNUmber"]["just_started"] = getNumericInput("Please insert the number of students that are going to start the course: ")
    language["StartFinishNUmber"]["isaboutto_finish"] = getNumericInput("Please insert the number of students that are going to finish the course: ")
    return language
    
def addSchool():
    school = {
	"SchoolName": "",
	"num_of_studentsRightNow": 0,
	"num_of_studentsTillNow": 0,
	"num_of_LanguagesTaught": 0,
	"languages" : [],
	}
    languages = []
    
    school["SchoolName"] = input("Please insert the name of the school: ")
    school["num_of_studentsRightNow"] = getNumericInput("Please insert the number of students currently studying in this school: ")
    school["num_of_studentsTillNow"] = getNumericInput("Please insert the number of students that this school has ever had: ")
    school["num_of_LanguagesTaught"] = getNumericInput("Please insert the number of languages that are being taught now in the school: ")
    for i in range(school["num_of_LanguagesTaught"]):
        languages.append(addLanguage())
    school["languages"].append(languages)
    return school
    
def loadExistingSchools():
    with open('schools.json') as file_data:
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
        insert_mode = input("Do you want to start adding language schools?, please answer yes or no: ")
        if(insert_mode == "no"):
            SchoolName =input("Enter school name: ")
            n = check_for_school(SchoolName, schools)
        else:
            school = addSchool()
            schools.append(school)

    print("Saving to the file")
    saveToTheFile(schools)
    displayAllSchools(schools)

main()
