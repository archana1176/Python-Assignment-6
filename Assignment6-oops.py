class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def __str__(self):
        return f"{self.course_code}: {self.course_name} ({self.credit_hours} credit hours)"

class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def __str__(self):
        status = "Required" if self.required_for_major else "Optional"
        return f"{super().__str__()} - {status} for major"

class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def __str__(self):
        return f"{super().__str__()} - Elective Type: {self.elective_type}"



core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
elective_course = ElectiveCourse("ECE100", "Basics of Electronics", 2, "Technical")

# Printing course details
print(core_course)
print(elective_course)
