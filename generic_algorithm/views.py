from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from utils.print_helpers import convert_schedule_to_required_format, receive_data
from .scheduler import GeneticAlgorithmScheduler
import json

@csrf_exempt
def generate_schedule(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        classrooms, groups, teachers, subjects = receive_data(data)

        ga = GeneticAlgorithmScheduler(groups=groups, teachers=teachers, classrooms=classrooms, subjects=subjects)
        best_individual = ga.run()

        converted_schedule = convert_schedule_to_required_format(best_individual)

        return JsonResponse(converted_schedule)

    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=400)
