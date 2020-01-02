class Student(object):
    
    def __init__(self, english , science , maths):
        self.english = english
        self.science = science
        self.maths = maths

    def each_sem_marks(self):
        self.sem_marks = (self.english + self.maths + self.science) / 3
        return self.sem_marks
    
    def __lt__(self, other):
        return self.sem_marks < other.sem_marks   

    def __gt__(self, other):
        return self.sem_marks > other.sem_marks

    def __eq__(self, other):
        return self.sem_marks == other.sem_marks

student1 = Student(70,80,80)
student2 = Student(80,60,70)
 
print(student1.each_sem_marks() > student2.each_sem_marks())