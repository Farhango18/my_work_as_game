class CellType:
    def __init__(self, element='Header', next=None):
        self.element = element
        self.next = next

    def print_cell(self):
        print(self.element, end=",")


class SList:
    def __init__(self):
        self.header = CellType()
        self.size = 0

    def end_list(self):
        h = self.header
        while h.next is not None:
            h = h.next
        return h

    def append(self, element):
        endl = self.end_list()
        cellnode = CellType(element)
        endl.next = cellnode
        self.size += 1

    def __iter__(self):
        current = self.header.next
        while current :
            yield current.element
            current = current.next
    def pop(self, value):
        element = self.header.next
        previous = self.header
        while element :
            if element.element == value:
                previous.next = element.next
                self.size -= 1
                return
            previous = element
            element = element.next

class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def show(self):
        return f"{self.hour:02}  :  {self.minute:02}"


class Lessons:
    def __init__(self, name, location, lesson_id, next_lesson=None, time_lesson=(0, 0)):
        self.name = name
        self.location = location
        self.lesson_id = lesson_id
        self.time_lesson = time_lesson
        self.next_lesson = next_lesson

    def print_lessons(self):
        current = self
        while current :
            hour, minute = current.time_lesson
            print(f"lesson: {current.name} (ID:{current.lesson_id})\tlocation: {current.location}\tTime: {hour:02}:{minute:02}")
            current = current.next_lesson

    def add_lesson(self, name, location, lesson_id):
        new_lesson = Lessons(name, location, lesson_id)
        if not self:
            return new_lesson
        current = self
        while current.next_lesson:
            current = current.next_lesson
        current.next_lesson = new_lesson

    def remove_lesson1(self, lesson_id):
        current = self
        if current.lesson_id == lesson_id:
            return current.next_lesson
        while current.next_lesson :
            if current.next_lesson.lesson_id == lesson_id:
                current.next_lesson = current.next_lesson.next_lesson
                return self
            current = current.next_lesson
        return self


def search_student(lesson_id, student_list):
    print(f"!!!!Searching for students who took lesson with ID {lesson_id}!!!!")

    matched_students = []

    for student in student_list:
        for pointer in student.P_profile.week_lessons:
            lesson = pointer.lesson
            while lesson:
                if lesson.lesson_id == lesson_id:
                    matched_students.append((student, lesson.location))
                    break
                lesson = lesson.next_lesson
            if matched_students and matched_students[-1][0] == student:
                break

    if matched_students:
        for student, location in matched_students:
            print(student.P_profile.cout(), student.show(), f"\tClass Location: {location}")
    else:
        print("No students found for this lesson ID.")


class Pointer:
    def __init__(self, day, lesson=None):
        self.day = day
        self.lesson = lesson

    def print_pointer(self):
        print(f"{self.day}: ")
        if self.lesson:
            self.lesson.print_lessons()
        else:
            print("No lesson")


class Profile:
    def __init__(self, fname, lname, age, week_lessons=None):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.week_lessons = week_lessons if week_lessons else []

    def cout(self):
        return f"Name: {self.fname} {self.lname}, Age: {self.age}"

    def show_week_lessons(self):
        print(f"Weekly lessons for {self.fname} {self.lname}:")
        for pointer in self.week_lessons:
            pointer.print_pointer()

    def add_lesson2(self, day, lesson):
        for pointer in self.week_lessons:
            current = pointer.lesson
            while current :
                if current.name== lesson.name:
                    print(f"Error: {self.fname} already has the class '{lesson.name}' on another day.")
                    return
                current = current.next_lesson

        for pointer in self.week_lessons:
            if pointer.day == day:
                current = pointer.lesson
                while current:
                    if current.time_lesson == lesson.time_lesson:
                        print(f"Error: {self.fname} already has a class at this time on {day}.")
                        return
                    elif current.lesson_id == lesson.lesson_id:
                        print(f"Error: {self.fname} already has this class.")
                        return
                    current = current.next_lesson

                if pointer.lesson is None:
                    pointer.lesson = lesson
                else:
                    current = pointer.lesson
                    while current.next_lesson:
                        current = current.next_lesson
                    current.next_lesson = lesson

                print(f"Lesson '{lesson.name}' added on {day} at {lesson.time_lesson}.")
                return
        print(f"Error: {day} is not in {self.fname}'s weekly schedule.")

    def remove_lesson2(self, day, lesson_id):
        day_pointer = next((p for p in self.week_lessons if p.day == day), None)
        if not day_pointer or not day_pointer.lesson:
            print("Lesson not found or day has no lessons.")
            return

        current = day_pointer.lesson
        previous = None

        while current:
            if current.lesson_id == lesson_id:
                if previous is None:
                    day_pointer.lesson = current.next_lesson
                else:
                    previous.next_lesson = current.next_lesson
                print(f"Lesson '{current.name}' removed successfully.")
                return
            previous = current
            current = current.next_lesson

        print("Lesson ID not found.")


class Student:
    def __init__(self, student_id, next_s=None, p_profile=None):
        self.ID = student_id
        self.next_s = next_s
        self.P_profile = p_profile

    def show(self):
        return f"Student ID: {self.ID}"


l1 = Lessons("Math", 1205, "MATH_SATURDAY",None,(13,0))
l2 = Lessons("Physic", 1314, "PHYSIC_SATURDAY",l1,(15,40))
l3 = Lessons("English", 1134, "ENGLISH_SUNDAY",None,(9,30))
l4 = Lessons("Data Structure", 1502, "DATA STRUCTURE_SUNDAY",l3,(13,0))
l5 = Lessons("Algorithm", 1414, "ALGORITHM_MONDAY",None,(9,45))
l6 = Lessons("Programming", 1512, "PROGRAMMING_MONDAY",l5,(12,30))
l7 = Lessons("Culture Of Iran", 2212, "CULTURE OF IRAN_TUESDAY",None,(7,15))
l8 = Lessons("Islamic History", 1115, "ISLAMIC HISTORY_TUESDAY",l7,(9,0))
l9 = Lessons("Logic System", 1513, "LOGIC SYSTEM_WEDNESDAY",None,(7,30))
l10 = Lessons("Electric System", 1234, "ELECTRIC SYSTEM_WEDNESDAY",l9,(10,15))
l11 = Lessons("Web Design", 1234, "WEB DESIGN_THURSDAY",None,(16,30))

m = [
    Pointer("Saturday", l2),
    Pointer("Sunday", l4),
    Pointer("Monday", l6),
    Pointer("Tuesday", l8),
    Pointer("Wednesday", l10),
    Pointer("Thursday", l11),
    Pointer("Friday")
]
n = [
    Pointer("Saturday"),
    Pointer("Sunday"),
    Pointer("Monday"),
    Pointer("Tuesday"),
    Pointer("Wednesday"),
    Pointer("Thursday"),
    Pointer("Friday")
]
P1 = Profile("Farhan", "Golestani", 20, m)
S1 = Student("1643490", None, P1)
P2 = Profile("Amirali", "Sadeghi", 22,n)
S2 = Student("1658438", S1, P2)
Student_List = [S1, S2]
a = SList()
a.append(S1)
a.append(S2)


# new_lesson = Lessons("math", 1205, "MATCH_SUNDAY", time_lesson=10)
# P1.add_lesson("Sunday", new_lesson)
#
# conflicting_lesson = Lessons("history", 1302, "HISTORY_SATURDAY", time_lesson=10)
# P1.add_lesson("Saturday", conflicting_lesson)
#
# P1.remove_lesson("PHYSIC_SATURDAY")


def f(choice):
    match choice:
        case "1":
            student_id = input("Enter student ID to view schedule: ")
            student = next((s for s in a if s.ID == student_id), None)
            if student:
                student.P_profile.show_week_lessons()
            else:
                print("Student not found.")
            main()
        case "2":
            student_id = input("Enter student ID to add a lesson: ")
            student = next((s for s in a if s.ID == student_id), None)
            if student:
                day = input("Enter day to add the lesson (e.g., 'Monday'): ").capitalize()
                name = input("Enter name of the lesson: ").capitalize()
                location = input("Enter class of lesson: ")
                lesson_id = input("Enter lesson ID: ").upper()
                time_input = input("Enter lesson time (HH:MM format, 24-hour): ")
                try:
                    hour, minute = map(int, time_input.split(":"))
                    new_lesson = Lessons(name, location, lesson_id, time_lesson=(hour, minute))
                    student.P_profile.add_lesson2(day, new_lesson)
                except ValueError:
                    print("Invalid time format. Please enter the time as HH:MM.")

            else:
                print("Student not found.")
            main()
        case "3":
            student_id = input("Enter student ID to remove a lesson: ")
            student = next((s for s in a if s.ID == student_id), None)
            if student:
                day = input("Enter the day of the lesson to remove (e.g., 'Monday'): ").capitalize()
                lesson_id = input("Enter lesson ID to remove: ").upper()
                student.P_profile.remove_lesson2(day, lesson_id)
            else:
                print("Student not found.")
            main()
        case "4":
            lesson = input("Enter name of lesson : ").upper()
            day = input("Enter day of lesson : ").upper()
            result = lesson + "_" + day
            search_student(result, a)
            main()
        case "5":
            l = [
                Pointer("Saturday"),
                Pointer("Sunday"),
                Pointer("Monday"),
                Pointer("Tuesday"),
                Pointer("Wednesday"),
                Pointer("Thursday"),
                Pointer("Friday")
                ]
            student_id=input("Enter student's ID : ")
            f_name=input("Enter student's name : ").capitalize()
            l_name = input("Enter student's last name : ").capitalize()
            age = int(input("Enter student's Age : "))
            new_profile = Profile(f_name , l_name, age , l)
            new_student = Student(student_id,None,new_profile)
            a.append(new_student)
            print("Student adding was successful.")
            main()
        case "6" :
            student_id = input("Enter student ID to remove : ")
            student= next((s for s in a if s.ID == student_id), None)
            if student:
                a.pop(student)
                print("Removing student was successfully")
            else:
                print("Student not found.")
            main()
        case "0":
            exit()
        case _:
            print("Invalid Choice! Try Again\n")
            main()


def main():
    print(
        "\n\t--- Main Menu ---\n\n"
        "\t1. View Student Schedule\n"
        "\t2. Add a Lesson\n"
        "\t3. Remove a Lesson\n"
        "\t4. Search a Lesson\n"
        "\t5. Add a student\n"
        "\t6. Remove a student\n"
        "\t0. Exit")
    choice = input("\nEnter your choice : ")
    f(choice)




# for i in a:
#      print(i.P_profile.cout(), i.show())
#      i.P_profile.show_week_lessons()

if __name__ == "__main__":
    main()