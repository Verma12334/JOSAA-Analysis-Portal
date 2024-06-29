from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import F
from .models import Extract
from django.views.decorators.http import require_GET


def home(request):
    return render(request,'page1/page.html')

def YearWise(request):
    return render(request,'page1/YearWise.html')

def BranchWise(request):
    return render(request,'page1/BranchWise.html')

def IIT(request):
    return render(request,'page1/IIT.html')

def InstituteWise(request):
    
    return render(request,'page1/InstituteWise.html')

def Roundwise(request):
    return render(request,'page1/Roundwise.html')

def BestCourses(request):
    return render(request,'page1/BestCourses.html')

def KnowIIT(request):
    return render(request,'page1/Knowiit.html')

def Preferences(request):
    return render(request,'page1/preferences.html')


def get_graph_data_roundwise(request):
    
    round_value = request.GET.get('round')
    iit_value = request.GET.get('iit')
    programtype_value = request.GET.get('programtype')
    programname_value = request.GET.get('programname')
    graph_data = Extract.objects.filter(
        Round = round_value,
        Seat_type = "OPEN",
        Institute = iit_value,
        Gender = "Gender-Neutral",
        Program_type = programtype_value,
        Program_name = programname_value
    ).values()

    graph_data = list(graph_data)

    return JsonResponse(graph_data, safe=False)


def get_graph_data_yearwise(request):
    
    gen_value = request.GET.get('gender')
    year_value = request.GET.get('year')
    iit_value = request.GET.get('iit')
    programtype_value = request.GET.get('programtype')
    programname_value = request.GET.get('programname')
    graph_data = Extract.objects.filter(
        
        Seat_type = "OPEN",
        Gender=gen_value,
        Institute = iit_value,
        Program_type = programtype_value,
        Program_name = programname_value
    ).values()

    
    graph_data = list(graph_data)

    return JsonResponse(graph_data, safe=False)


def get_bestcourse(request):
    
    year_val = request.GET.get('year')
    programname_value = request.GET.get('programname')
    data = Extract.objects.filter(
    Year=year_val,
    Program_name=programname_value,
    Seat_type="OPEN",
    Gender="Gender-Neutral",
    Round=3
    ).order_by('Closing_rank')[:5].values()

    
    data = list(data)
    
    return JsonResponse(data, safe=False)
    


def get_knowiit(request):
    
    rank_val = request.GET.get('rank')
    programname_value = request.GET.get('programname')
    data = Extract.objects.filter(
        Year = 2023,
        Program_name = programname_value,
        Seat_type = "OPEN",
        Gender = "Gender-Neutral",
        Round = 3,
        Program_duration = 4,
        Closing_rank__gte=rank_val
    ).order_by('Opening_rank').values()
    
    data = list(data)
    
    return JsonResponse(data, safe=False)


def get_yearwise(request):
    year = request.GET.get('year')

    data = Extract.objects.filter(
            Year = year
        ).values('Program_name').distinct()
    
    data = list(data)
    return JsonResponse(data, safe=False)


def get_institutewise(request):
    inst = request.GET.get('inst')

    data = Extract.objects.filter(
            Institute = inst
        ).values('Program_type').distinct()
    
    data = list(data)
    
    return JsonResponse(data, safe=False)

def get_institutewise_name(request):
    types = request.GET.get('type')
    iit = request.GET.get('iit')
    data = Extract.objects.filter(
            Institute = iit,
            Program_type = types
        ).values('Program_name').distinct()
    
    data = list(data)
    return JsonResponse(data, safe=False)

def get_institutewise_gender(request):
    name = request.GET.get('name')

    data = Extract.objects.filter(
            Program_name = name
        ).values('Gender').distinct()
    
    data = list(data)
    return JsonResponse(data, safe=False)


def get_roundwise_institute(request):
    rounds = request.GET.get('round')

    data = Extract.objects.filter(
            Round = rounds
        ).values('Institute').distinct()
    
    data = list(data)
    return JsonResponse(data, safe=False)


def get_roundwise_name(request):
    rounds = request.GET.get('round')
    iit = request.GET.get('iit')
    
    data = Extract.objects.filter(
            Round = rounds,
            Institute = iit,
            
        ).values('Program_name').distinct()
    
    data = list(data)
    return JsonResponse(data, safe=False)

def get_roundwise_type(request):
    rounds = request.GET.get('round')
    iit = request.GET.get('iit')
    prog = request.GET.get('prog_name')

    data = Extract.objects.filter(
            Round = rounds,
            Institute = iit,
            Program_name = prog
        ).values('Program_type').distinct()
    
    data = list(data)
    return JsonResponse(data, safe=False)


def get_preferences(request):
    
    rank_val = request.GET.get('rank')
    programname_1 = request.GET.get('programname')
    programname_2 = request.GET.get('programname_2')
    programname_3 = request.GET.get('programname_3')
    data = Extract.objects.filter(
        Year = 2023,
        Program_name = programname_1,
        Seat_type = "OPEN",
        Gender = "Gender-Neutral",
        Round = 3,
        Program_duration = 4,
        Closing_rank__gte=rank_val
    ).order_by('Opening_rank').values()
    
    data = list(data)
    
    return JsonResponse(data, safe=False)



