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
        # Formatted average to remove unnecessary trailing zeros if it's a whole number
        display_avg = round(average, 2)
        
        if display_avg >= 75:
            grade = "A"
        elif display_avg >= 60:
            grade = "B"
        elif display_avg > 40:
            grade = "C"
        else:
            grade = "F"
            
        # --- Formatting Logic ---
        line_name = f"Name: {name}"
        line_avg = f"Average: {display_avg}"
        line_grade = f"Grade: {grade}"
        
        # Find the longest string to determine separator length
        max_len = max(len(line_name), len(line_avg), len(line_grade))
        separator = "-" * (max_len + 4) # Added padding for aesthetic
        
        print(separator)
        print(line_name)
        print(line_avg)
        print(line_grade)
        print(separator)

if __name__ == "__main__":
    main()