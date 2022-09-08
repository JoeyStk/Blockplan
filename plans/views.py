from .models import Plan, Week, Class
from django.shortcuts import render

def home(request):
    plan_list = []
    for plan in Plan.objects.all():
        if plan.status:
            week_list = []
            for week in plan.weeks.all():
                if week.school:
                    class_list = [
                        int(str(week.week_id)[2:]),
                        week.start_date,
                        week.end_date,
                        week.amound_of_days,
                    ]
                    for year in range(10, 14):
                        if week.reference.filter(profession='elektro', year=year):
                            class_list.append(str(week.amound_of_days))
                        else:
                            class_list.append('')

                    class_list.append(week.commentary)

                    for year in range(10, 13):        
                        for group in ['a', 'b', 'c']:
                            if week.reference.filter(profession='it', year=year, group=group):
                                class_list.append(str(week.amound_of_days))
                            else:
                                class_list.append('')
                                
                    week_list.append(class_list)
                else:
                    class_list = [
                        int(str(week.week_id)[2:]),
                        week.start_date,
                        week.end_date,
                        '',
                        '',
                        '',
                        '',
                        '',
                        week.commentary,
                        '',
                        '',
                        '',
                        '',
                        '',
                        '',
                        '',
                        '',
                        '',
                    ]
                    week_list.append(class_list)    
            plan_list.append(week_list)
    context = {
        'plan_list': plan_list,
        'classes' : Class.objects.all
    }
    return render(request, 'plans/home.html', context)

