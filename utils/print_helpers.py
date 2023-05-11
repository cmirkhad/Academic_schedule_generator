from tabulate import tabulate

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