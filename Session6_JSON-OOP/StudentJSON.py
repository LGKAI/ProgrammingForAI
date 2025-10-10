import json

def read_students(file_path: str) -> dict:
    with open(file_path, "r") as file:
        students = json.load(file)
    return students

def find_student_max_avg_grade(students: dict) -> str:
    top_student = None
    max_avg = 0
    for student_id, student_info in students.items():
        avg_grade = sum(student_info["grades"]) / len(student_info["grades"])
        if avg_grade > max_avg:
            max_avg = avg_grade
            top_student = student_id
    return top_student

if __name__ == "__main__":
    student_list = read_students("student.json") # dùng path thì code mới chạy
    id = find_student_max_avg_grade(student_list)
    print(student_list[id]["name"])

    student = student_list[id]
    out_file = open("top_student.json", "w")
    json.dump(student, out_file, indent = 4)
    out_file.close()