import json

def main():
    with open('grades.json') as f:
        grades = json.load(f)

    print("Exam Results for Class 28\n=========================")
    for item in filter(lambda x: x['class_id'] == 28, grades):
        print("Student " + str(item['student_id']) + " scored:\n\t" + str(item['scores'][0]['score']) + " on exam")


if __name__ == "__main__":
    main()
