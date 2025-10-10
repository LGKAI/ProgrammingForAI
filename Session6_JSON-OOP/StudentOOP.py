class Student:
    def __init__(self, id, name, score):
        self.student_id = id
        self.name = name
        self.grades = score
    
    def print(self):
        print(self.student_id, "-", self.name, "-", self.grades)

    def get_avg(self):
        return sum(self.grades) / len(self.grades)


if __name__ == "__main__":
    a = Student("23127000", "Nguyen Tran Duy Minh", [1, 2, 3])
    b = Student("23127050", "Duy Minh", [90, 100, 90])
    a.print()
    score_a = a.get_avg()
    print(score_a)

