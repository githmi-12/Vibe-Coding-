def get_valid_name():
    while True:
        name = input("Enter Student name (or 'exit' to stop): ")
        if name.lower() == "exit":
            return "exit"
        if name and len(name) > 2 and name.isalpha():
            return name
        print("The student’s name you entered is invalid. Please re-enter")

def get_valid_mark(subject_num):
    while True:
        try:
            mark_input = input(f"Enter mark for Subject {subject_num:02d}: ")
            if mark_input == "":
                raise ValueError
            mark = int(mark_input)
            if 0 <= mark <= 100:
                return mark
            else:
                raise ValueError
        except ValueError:
            print("The subject mark you entered is invalid. Please re-enter")

def main():
    while True:
        name = get_valid_name()
        if name.lower() == "exit":
            break
            
        marks = []
        for i in range(1, 4):
            marks.append(get_valid_mark(i))
        
        average = sum(marks) / len(marks)
        rounded_average = round(average, 4)
        
        if rounded_average >= 75:
            grade = "A"
        elif rounded_average >= 60:
            grade = "B"
        elif rounded_average > 40:
            grade = "C"
        else:
            grade = "F"
            
        print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
