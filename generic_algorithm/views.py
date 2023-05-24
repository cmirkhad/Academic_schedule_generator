from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import datetime
from utils.print_helpers import convert_schedule_to_required_format, receive_data
from .scheduler import GeneticAlgorithmScheduler
import json

@csrf_exempt
def generate_schedule(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))  # Decode the request body

        classrooms, groups, teachers, subjects = receive_data(data)
        semester = data.get('semester')

        ga = GeneticAlgorithmScheduler(groups=groups, teachers=teachers, classrooms=classrooms, subjects=subjects)
        best_individual = ga.run()

        converted_schedule = convert_schedule_to_required_format(best_individual)
        url = 'https://schedule-back.herokuapp.com/api/schedule'
        session = requests.Session()
        sh_name = data.get('name')

        data = {
            'year': datetime.datetime.today().isoformat(),
            'name': sh_name,
            'semester': semester,
            'days': converted_schedule
        }
        response = session.post(url, json=data)


        return JsonResponse(response.json(), status=response.status_code)

    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)
