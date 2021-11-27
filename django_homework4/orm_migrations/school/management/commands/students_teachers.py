from school.models import Teacher, Student

for teacher in Teacher.objects.all():
    for student in Student.objects.all():
        student.teachers.add(teacher)