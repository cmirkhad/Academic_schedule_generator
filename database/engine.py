import pandas as pd
import sys
sys.path.insert(1,'/')
from sqlalchemy import create_engine
from models.classroom import Classroom
from models.group import Group
from models.teacher import Teacher
from models.subject import Subject

def fetch_data_from_db():
    connection_string = "postgresql://postgres:123456789@localhost:5433/postgres"
    engine = create_engine(connection_string)

    classrooms_df = pd.read_sql("SELECT id, title, capacity, type FROM classrooms", engine)
    classrooms = [Classroom(*row) for _, row in classrooms_df.iterrows()]

    groups_df = pd.read_sql("SELECT g.id, g.name, g.year, g.studentscount FROM groups g", engine)
    groups = [Group(*row) for _, row in groups_df.iterrows()]

    teachers_df = pd.read_sql("SELECT id, firstName, lastName, workingDays, workingGraphic FROM teachers", engine)
    teachers = [Teacher(*row) for _, row in teachers_df.iterrows()]

    subjects_df = pd.read_sql("SELECT id, name, code, teachers, credits, semester, courses,  numberOfHours FROM subjects", engine)
    subjects = [Subject(*row) for _, row in subjects_df.iterrows()]

    engine.dispose()

    return classrooms, groups, teachers, subjects



