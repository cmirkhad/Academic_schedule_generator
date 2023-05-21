from tabulate import tabulate
from django.http import JsonResponse
import json
from models.group import Group
from models.subject import Subject
from models.classroom import Classroom
from models.teacher import Teacher

def print_schedule(schedule):
    headers = ['Group', 'Subject', 'Teacher', 'Classroom', 'Day', 'Slot']

    rows = [entry for entry in schedule]
    print(tabulate(rows, headers=headers))
    print(schedule.__sizeof__())


def convert_schedule_to_required_format(best_individual):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    schedule = [
        {
            'day': day,
            'courses': [
                {
                    'course': course,
                    'subjects': [None] * 11
                } for course in range(1, 5)
            ]
        } for day in days
    ]

    for group, subject, teacher, classroom, day, slot in best_individual:
        course_index = int(group.course) - 1
        schedule[day]['courses'][course_index]['subjects'][slot] = {
            'title' : subject.subj_name,
            'teachers': teacher.name + ' '  + teacher.surname,
            'code': subject.code,
            'numberOfHours': 1,
            'classroom': classroom.name
        }

    return schedule








def receive_data(data):

        groups = []
        groups.append(Group(id = '1', group_name='COM22', number_of_students=80, course=1))
        groups.append(Group(id = '2', group_name='COM21', number_of_students=80, course=2))
        groups.append(Group(id = '3', group_name='COM20', number_of_students=80, course=3))
        groups.append(Group(id = '4', group_name='COM19', number_of_students=80, course=4))


        # Extracting classrooms data
        classrooms_data = data['classrooms']
        classrooms = []
        for classroom in classrooms_data:
            classrooms.append(Classroom(
                id=classroom.get('_id'),
                name=classroom.get('title'),
                capacity=classroom.get('capacity'),
                room_type=classroom.get('type'),
            ))

        # Extracting subjects data
        subjects_data = data['subjects']
        subjects = []
        teachers = []
        for subject in subjects_data:
            teachers_data = subject.get('teachers')

            if teachers_data:
                for teacher in teachers_data:
                    if teacher in teachers:
                        continue
                    teachers.append(Teacher(
                        id=teacher.get('_id'),
                        name=teacher.get('firstName'),
                        surname=teacher.get('lastName'),
                        working_days=teacher.get('workingDays'),
                        working_graphic=teacher.get('workingGraphic'),
                    ))
            subjects.append(Subject(
                id=subject.get('_id'),
                subj_name=subject.get('name'),
                code=subject.get('code'),
                teachers=teachers,
                credits=subject.get('credits'),
                semester=subject.get('semester'),
                course=subject.get('courses')[0] if subject.get('courses') else None,
                number_of_hours=subject.get('numberOfHours'),
            ))

        # Call your schedule generation function here
        # generate_schedule(classrooms, subjects)

        return classrooms, groups, teachers, subjects