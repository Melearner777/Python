# Parent Class
class Staff:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}"

# Child Class
class Teacher(Staff):
    def __init__(self, name, age, position, subject):
        super().__init__(name, age, position)
        self.subject = subject

    def get_details(self):
        
        return f"{self.name},{self.age} Subject: {self.subject}"

# Usage
teacher1 = Teacher("John Doe", 40, "Senior Teacher", "Mathematics")
teacher2 = Teacher("Jane Smith", 35, "Assistant Teacher", "English")

print(teacher1.get_details())  # Output: Name: John Doe, Age: 40, Position: Senior Teacher, Subject: Mathematics
print(teacher2.get_details())  # Output: Name: Jane Smith, Age: 35, Position: Assistant Teacher, Subject: English
