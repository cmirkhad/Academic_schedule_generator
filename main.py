import sys
from generic_algorithm.scheduler import GeneticAlgorithmScheduler
from database.engine import fetch_data_from_db
from utils.print_helpers import print_schedule
from utils.print_helpers import convert_schedule_to_required_format
from pprint import pprint





def main():
    # Fetch data from database
    classrooms, groups, teachers, subjects = fetch_data_from_db()

    # Initialize the genetic algorithm scheduler
    scheduler = GeneticAlgorithmScheduler(classrooms, groups, teachers, subjects)

    best_individual = scheduler.run()

    # Print the final schedule
    converted_schedule = convert_schedule_to_required_format(best_individual)
    pprint(converted_schedule)

if __name__ == "__main__":
    main()
