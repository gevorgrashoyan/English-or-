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
        if(SchoolName == school["SchoolName"]):
            return school
    return None

def addLanguage(LanguageName):
    language = {
        "language_name": "",
        "num_of_teachers": 0,
        "price_of_theCourse": 0,
        "num_of_groups": 0,
        "num_of_studentsInEach": 0,
        "entire_num_of_students": 0,
        "group_info" : {
                                "A1": 0,
                                "A2": 0,
                                "B1": 0,
                                "B2": 0,
                                "C1": 0,
                                "C2": 0
        }
    }
    	
    language["language_name"] = LanguageName
    language["num_of_teachers"] = getNumericInput("Please enter the number of teachers teaching this language: ")
    language["price_of_theCourse"] = getNumericInput("Please enter the price of the course: ")
    language["num_of_groups"] = getNumericInput("Please enter the number of groups studying the language: ")
    language["num_of_studentsInEach"] = getNumericInput("Please enter the number of students in each group: ")
    language["entire_num_of_students"] = getNumericInput("Please enter the entire number of students studying this language: ")
    language["group_info"]["A1"] = getNumericInput("Please enter the number of students studying A1 level: ")
    language["group_info"]["A2"] = getNumericInput("Please enter the number of students studying A2 level: ")
    language["group_info"]["B1"] = getNumericInput("Please enter the number of students studying B1 level: ")
    language["group_info"]["B2"] = getNumericInput("Please enter the number of students studying B2 level: ")
    language["group_info"]["C1"] = getNumericInput("Please enter the number of students studying C1 level: ")
    language["group_info"]["C2"] = getNumericInput("Please enter the number of students studying C2 level: ")
    return language
    
def addSchool(SchoolName):
    school = {
	"SchoolName": "",
	"num_of_studentsRightNow": 0,
	"num_of_studentsTillNow": 0,
	"num_of_LanguagesTaught": 0,
	"languages" : [],
	}
    languages = []
    
    school["SchoolName"] = SchoolName
    school["num_of_studentsRightNow"] = getNumericInput("Please enter the number of students currently studying in this school: ")
    school["num_of_studentsTillNow"] = getNumericInput("Please enter the number of students that this school has ever had: ")
    school["num_of_LanguagesTaught"] = getNumericInput("Please enter the number of languages that are being taught now in the school: ")
    for i in range(school["num_of_LanguagesTaught"]):
         LanguageName = input("Please enter the name of the language: ")
         languages.append(addLanguage(LanguageName))
    school["languages"] = languages
    return school
    
def mostPopularLanguage(schools):
    for school in schools:
        students = 0
        languageName = None
        for language in school["languages"]:
              if language["entire_num_of_students"] > students:
                  students = language["entire_num_of_students"]
                  languageName = language["language_name"]
        if students > 0:
              print("The most popular language at ", school["SchoolName"], " is ", languageName, " with ", students, " students")

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
        insert_mode = input("Do you want to add language schools? Please answer yes or no: ")
        if(insert_mode == "no"):
            mostPopularLanguage(schools)
            print("Goodbye")
            break
        else:
            SchoolName = input("Enter school name: ")
            school = check_for_school(SchoolName, schools)
            if (school == None):
                school = addSchool(SchoolName)
                schools.append(school)
            else:
                print("School already exists (update unavailable)")

    print("Saving to the file")
    saveToTheFile(schools)
    displayAllSchools(schools)

main()
