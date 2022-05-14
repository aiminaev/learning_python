class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        """
        Ставит оценку лектору, в случае если курс закреплен за преподавателем и студент изучает курс
        :param lecturer: Lecturer
        :param course: @str
        :param grade: int
        """
        try:
            if not (isinstance(lecturer, Lecturer)):
                raise TypeError('Этот объект не принадлежит классу Лектор')
            if not (course in self.courses_in_progress):
                raise Exception('Такой курс студент не изучает')
            if not (course in lecturer.courses_attached):
                raise Exception('Лектор такой курс не преподает')
            if not (0 < grade <= 10):
                raise Exception('Введите оценку от 1 до 10')

            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        except (TypeError, Exception) as err:
            print(err)

    def calc_average_grade_hw(self, course=None):
        """подсчет средней оценки за лекции"""
        try:
            if course:
                if course in self.grades:
                    sum_marks = sum(self.grades[course])
                    return round(sum_marks / len(self.grades[course]), 1)
                else:
                    raise Exception('У студента отсутствует данный курс')
            else:
                all_marks_list = sum(self.grades.values(), [])
                return round(sum(all_marks_list) / len(all_marks_list), 1)

        except Exception as e:
            print(e)

    def __gt__(self, other):
        '''To get called on comparison using > operator.'''
        return self.calc_average_grade_hw() > other.calc_average_grade_hw()

    def __lt__(self, other):
        '''To get called on comparison using < operator.'''
        return self.calc_average_grade_hw() < other.calc_average_grade_hw()

    def __le__(self, other):
        '''To get called on comparison using <= operator.'''
        return self.calc_average_grade_hw() <= other.calc_average_grade_hw()

    def __eq__(self, other):
        '''To get called on comparison using == operator.'''
        return self.calc_average_grade_hw() == other.calc_average_grade_hw()

    def __ne__(self, other):
        '''To get called on comparison using != operator.'''
        return self.calc_average_grade_hw() != other.calc_average_grade_hw()

    def __ge__(self, other):
        '''To get called on comparison using >= operator.'''
        return self.calc_average_grade_hw() >= other.calc_average_grade_hw()

    def __str__(self):
        return f"""\nИмя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.calc_average_grade_hw()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}"""


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calc_average_grade_lec(self, course_attached=None):
        """подсчет средней оценки за лекции"""
        try:
            if course_attached:
                if course_attached in self.grades:
                    sum_marks = sum(self.grades[course_attached])
                    return round(sum_marks / len(self.grades[course_attached]), 1)
                else:
                    raise Exception('У лектора отсутствует данный курс')
            else:
                all_marks_list = sum(self.grades.values(), [])
                return round(sum(all_marks_list) / len(all_marks_list), 1)

        except Exception as e:
            print(e)

    def __gt__(self, other):
        """To get called on comparison using > operator."""
        return self.calc_average_grade_lec() > other.calc_average_grade_lec()

    def __lt__(self, other):
        """To get called on comparison using < operator."""
        return self.calc_average_grade_lec() < other.calc_average_grade_lec()

    def __le__(self, other):
        """To get called on comparison using <= operator."""
        return self.calc_average_grade_lec() <= other.calc_average_grade_lec()

    def __eq__(self, other):
        """To get called on comparison using == operator."""
        return self.calc_average_grade_lec() == other.calc_average_grade_lec()

    def __ne__(self, other):
        """To get called on comparison using != operator."""
        return self.calc_average_grade_lec() != other.calc_average_grade_lec()

    def __ge__(self, other):
        """To get called on comparison using >= operator."""
        return self.calc_average_grade_lec() >= other.calc_average_grade_lec()

    def __str__(self):
        return f"""\nИмя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.calc_average_grade_lec()}"""


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """
        Ставит оценку за предмет, в случае если курс закреплен за преподавателем и студент изучает курс
        :param student:
        :param course:
        :param grade:
        :return:
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"""\nИмя: {self.name}
Фамилия: {self.surname}"""


def calc_average_mark_students_by_course(course, *students):
    sum_mark_by_course = 0
    for student in students:
        sum_mark_by_course += student.calc_average_grade_hw(course)

    return round(sum_mark_by_course / len(students), 1)


def calc_average_mark_lecturer_by_course(course, *lecturers):
    sum_grades_by_cource = 0
    for lec in lecturers:
        sum_grades_by_cource += lec.calc_average_grade_lec(course)

    return round(sum_grades_by_cource / len(lecturers), 1)


# ============== Тесты ===============

# Создаем экземпляры наших базовых классов
some_reviewer = Reviewer('Вася', 'Пупкин')
other_reviewer = Reviewer('Никита', 'Джигурда')
some_lecturer = Lecturer('Бенедикт', 'Камбербетчович')
other_lecturer = Lecturer('Иван', 'Иванов')
some_student = Student('Михаил', 'Терентьев', 'man')
other_student = Student('Михаил', 'Зубенко', 'man')

# Наполним наши экземпляры данными
some_reviewer.courses_attached = ['Git', 'Python']
some_lecturer.courses_attached = ['Git', 'Python']
other_lecturer.courses_attached = ['Git', 'Python']
some_student.courses_in_progress = ['Git', 'Python']
other_student.courses_in_progress = ['Git', 'Python']
some_student.finished_courses = ['HTML', 'CSS']

# Проставим оценки
# ------- Студентам
some_reviewer.rate_hw(some_student, 'Git', 8)
some_reviewer.rate_hw(some_student, 'Git', 9)
some_reviewer.rate_hw(some_student, 'Python', 7)
some_reviewer.rate_hw(other_student, 'Git', 8)
some_reviewer.rate_hw(other_student, 'Python', 9)
some_reviewer.rate_hw(other_student, 'Python', 7)

# ------- Преподавателю
some_student.rate_lecturer(some_lecturer, 'Git', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 8)
other_student.rate_lecturer(other_lecturer, 'Git', 9)
other_student.rate_lecturer(other_lecturer, 'Python', 4)

print(calc_average_mark_students_by_course('Python', some_student, other_student))
print(calc_average_mark_lecturer_by_course('Git', some_lecturer, other_lecturer))
print(some_student)
print(some_lecturer)
print(some_reviewer)

print(some_student == other_student)
print(some_lecturer == other_lecturer)
