import sys
from generic_algorithm.scheduler import GeneticAlgorithmScheduler
from database.engine import fetch_data_from_db
from utils.print_helpers import print_schedule
from utils.print_helpers import convert_schedule_to_required_format
from pprint import pprint
import requests
import datetime



def main():
    # Fetch data from database
    classrooms, groups, teachers, subjects = fetch_data_from_db()

    # Initialize the genetic algorithm scheduler
    scheduler = GeneticAlgorithmScheduler(classrooms, groups, teachers, subjects)

    best_individual = scheduler.run()

    # Print the final schedule
    converted_schedule = convert_schedule_to_required_format(best_individual)
    pprint(converted_schedule)


    url = 'https://schedule-back.herokuapp.com/api/schedule'
    session = requests.Session()

    data = {
        'year': datetime.datetime.today().isoformat(),
        'name': 'improved schedule 5',
        'semester': 1,
        'days': converted_schedule
    }
    response = session.post(url, json=data)

    print(response.status_code)
    print(response.json())

if __name__ == "__main__":
    main()
