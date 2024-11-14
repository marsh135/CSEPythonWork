

class csStudents:
    def __init__(self, fName, lName, grade):
        self.fName = fName
        self.lName =  lName
        self.grade =  grade
    def __str__(self):
        return f"{self.grade}  - {self.lName}, {self.fName}"

rb =  csStudents("Richie", "Boice", "sophomore")
rb1 =  csStudents("Riley", "Bice", "sophomore")
ll =  csStudents("Lee", "Lehtomaki", "sophomore")
eh =  csStudents("Ethan", "Holmes", "freshman")
lc =  csStudents("Logan", "Church", "senior")
ta =  csStudents("Thomas", "Ames", "freshman")



print(rb)