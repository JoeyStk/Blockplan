from django.shortcuts import render
from django.http import HttpResponse
from .models import Week, Class, Plan


# Views für die Homepage
def home(request):
    plans = Plan.objects.all()
    weeks_dict = {}
    for plan in plans:
        week = plan.weeks.values()
        weeks_dict = week
    print(weeks_dict)

    all_weeks = Week.objects.all().order_by('start_date')
    courses = {}
    for week in all_weeks:
        course = week.reference.values()
        # courses[course[0]['name']] = course[0]
    
    context = {
        'plans': plans,
        'plans_courses' : courses,
        'weeks' : all_weeks,
        'classes': Class.objects.all()
    }
    # übergibt das Context dict an Views
    return render(request, 'plans/home.html', context)