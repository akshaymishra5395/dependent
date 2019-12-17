from django.shortcuts import render
from .models import Building
from django.http import JsonResponse
# Create your views here.
def base_view(request):
    return render(request,'takelogiii/index.html')

def getfloors(request):
    buil_id = request.GET.get('id_building','')
    floor = 0
    try:
        floor = Building.objects.filter(pk=buil_id).first().floors
    except:
        print('error')
    
    if floor:
        data=[(str(x),str(x))for x in range(1, floor + 1)] 
        # data=[role_name for role_name in Building.objects.filter(pk=mapi).first()]
        return JsonResponse(data, safe=False)