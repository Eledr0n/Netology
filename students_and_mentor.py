class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if all_grades:
            return sum(all_grades) / len(all_grades)
        return 0

    def __str__(self):
        average = self.average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {average:.1f}\n'
                f'Курсы в процессе изучения: {courses_in_progress}\n'
                f'Завершенные курсы: {finished_courses}')

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grade() <= other.average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.average_grade() != other.average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() > other.average_grade()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.average_grade() >= other.average_grade()
        return NotImplemented


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if all_grades:
            return sum(all_grades) / len(all_grades)
        return 0

    def __str__(self):
        average = self.average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {average:.1f}')

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() <= other.average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() != other.average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() > other.average_grade()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() >= other.average_grade()
        return NotImplemented


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
student1.grades = {'Python': [10, 9, 8], 'Git': [9, 10]}

student2 = Student('John', 'Doe', 'your_gender')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Основы программирования']
student2.grades = {'Python': [7, 8, 9]}

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']
lecturer1.grades = {'Python': [9, 10]}

lecturer2 = Lecturer('Anna', 'Smith')
lecturer2.courses_attached += ['Python']
lecturer2.grades = {'Python': [8, 7, 9]}

reviewer1 = Reviewer('Kate', 'Johnson')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Michael', 'Brown')
reviewer2.courses_attached += ['Python']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 7)

student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer2, 'Python', 8)
student2.rate_lecturer(lecturer1, 'Python', 7)
student2.rate_lecturer(lecturer2, 'Python', 9)


print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)


def average_hw_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    if total_grades:
        return sum(total_grades) / len(total_grades)
    return 0

def average_lecture_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    if total_grades:
        return sum(total_grades) / len(total_grades)
    return 0


print(f'Средняя оценка за домашние задания по курсу Python: {average_hw_grade([student1, student2], "Python"):.1f}')
print(f'Средняя оценка за лекции по курсу Python: {average_lecture_grade([lecturer1, lecturer2], "Python"):.1f}')
