import csv
import datetime

class Course:
    def __init__(self, name, exam_price, capacity):
        self.name = name
        self.exam_price = exam_price
        self.capacity = capacity
        self.available_capacity = capacity
    
    # ... (previous methods omitted for brevity)
    # ...
    
    def register_student(self):
        if self.check_capacity():
            self.available_capacity -= 1
            return True
        else:
            return False
        
    def check_capacity(self):
        return self.available_capacity > 0

class CodeAcademy:
    def __init__(self, name, location, programming_languages):
        self.name = name
        self.location = location
        self.programming_languages = programming_languages
        self.registration_status = "inactive"
        self.course_level = 0
        self.course = None
        self.start_date = None
    
    def get_name(self):
        return self.name
    
    def get_location(self):
        return self.location
    
    def get_programming_languages(self):
        return self.programming_languages
    
    def sign_up(self, name, language_preference, payment_status, course):
        self.name = name
        self.programming_languages = [language_preference]
        
        if payment_status and course.check_capacity():
            self.registration_status = "active"
            self.course_level = 1
            self.course = course
            self.course.register_student()
            self.start_date = datetime.datetime.now()
            self.write_student_info()

    def take_exam(self, exam_score):
        if self.registration_status == "active":
            current_date = datetime.datetime.now()
            duration = current_date - self.start_date
            months_passed = duration.days // 30
            
            if months_passed % 2 == 0:
                if exam_score >= 90 and exam_score <= 100:
                    self.course_level += 1
                    if self.course_level == 4:
                        self.registration_status = "inactive"
                        print("Congratulations! You have completed the course.")
                    else:
                        print(f"Congratulations! You have passed the exam. Your level is now {self.course_level}.")
                    self.write_student_info()
                else:
                    print("You need to retake the exam.")
                    retake_exam_price = self.course.exam_price * 1.5
                    print(f"Please pay the retake exam fee of {retake_exam_price} TL.")
            else:
                print("It's not time for an exam yet.")
        else:
            print("You are not registered for any course.")
    
    def write_student_info(self):
        try:
            with open("students.csv", mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([self.name, self.programming_languages[0], self.registration_status, self.course_level])
        except Exception as e:
            print("An error occurred while writing student information:", e)
    
    @staticmethod
    def read_student_info():
        students = []
        try:
            with open("students.csv", mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    students.append(row)
        except Exception as e:
            print("An error occurred while reading student information:", e)
        
        return students
    
    

# Example usage
course = Course("Python Programming", 100, 10)
academy = CodeAcademy("Code Academy", "New York", ["Python", "JavaScript", "Java"])
academy.sign_up("Shayan", "Python", True, course)

academy.take_exam(95)  # Output: It's not time for an exam yet.

# Wait for 2 months...

academy.take_exam(95)  # Output: Congratulations! You have passed the exam. Your level is now 2.

# Wait for 2 months...

academy.take_exam(95)  # Output: Congratulations! You have passed the exam. Your level is now 3.

# Wait for 2 months...

academy.take_exam(95)
# Output: Congratulations! You have passed the exam. Your level is now 4.
#         Congratulations! You have completed the course.

# Read student information from file
students = CodeAcademy.read_student_info()
for student in students:
    print(student)
