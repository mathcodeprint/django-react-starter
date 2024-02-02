from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import StateTable, Counties, Towns
from rest_framework import generics
from .models import State, County, Town
from .serializers import StateSerializer, CountySerializer, TownSerializer


def get_state_list(request):
    qset = StateTable.objects.order_by('name').values_list('name', flat=True).distinct()
    context = {'object_list': qset}
    return render(request, 'your_app_name/state_list.html', context)

def get_county_list(request, state_pk):
    state_obj = StateTable.objects.get(id=state_pk)
    qset = Counties.objects.filter(state_table__id=state_pk).order_by('name').values_list('name', flat=True).distinct()
    context = {
        'object_list': qset,
        'state': state_obj,
    }
    return render(request, 'your_app_name/county_list.html', context)

def get_town_list(request, county_pk):
    county_obj = Counties.objects.get(id=county_pk)
    qset = Towns.objects.filter(counties__id=county_pk).order_by('name').values_list('name', flat=True).distinct()
    context = {
        'object_list': qset,
        'county': county_obj,
    }
    return render(request, 'your_app_name/town_list.html', context)

class CombinedView(ListView):
    model = StateTable
    template_name = 'your_app_name/combined.html'

    def get_queryset(self):
        result = []
        queryset = super().get_queryset()
        
        for state in queryset:
            state_qs = Counties.objects.filter(state_table=state).annotate(state_name=F("state_table__name"))
            for county in state_qs:
                county_qs = Towns.objects.filter(counties=county).annotate(county_name=F("counties__name"), state_name=F("counties__state_table__name"))
                
                for town in county_qs:
                    row = {"state": state, "county": county, "town": town}
                    result.append(row)
        return result
    
class StateListCreateView(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class CountyListCreateView(generics.ListCreateAPIView):
    serializer_class = CountySerializer

    def get_queryset(self):
        state_id = self.kwargs['state_id']
        return County.objects.filter(state_id=state_id)

class TownListCreateView(generics.ListCreateAPIView):
    serializer_class = TownSerializer

    def get_queryset(self):
        county_id = self.kwargs['county_id']
        return Town.objects.filter(county_id=county_id)