

class csStudents:
    def __init__(self, fName, lName, grade):
        self.fName = fName
        self.lName =  lName
        self.grade =  grade
    def __str__(self):
        return f"{self.grade}  - {self.lName}, {self.fName}"

rb =  csStudents("Richie", "B", "sophomore")
rb1 =  csStudents("Riley", "B", "sophomore")
ll =  csStudents("Lee", "L", "sophomore")
eh =  csStudents("E", "H", "freshman")
lc =  csStudents("Logan", "C", "senior")
ta =  csStudents("T", "A", "freshman")



