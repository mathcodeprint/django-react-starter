from django.urls import path
from .views import get_state_list, get_county_list, get_town_list, CombinedView
from .views import StateListCreateView, CountyListCreateView, TownListCreateView


app_name = 'state_selects' # Replace '<your_app_name>' with the correct app name

urlpatterns = [
    path('', get_state_list, name='state_page'),
    path('counties/<int:state_pk>/', get_county_list, name='county_by_state'),
    path('towns/<int:county_pk>/', get_town_list, name='town_by_county'),
    path('all/', CombinedView.as_view(), name='combined'),
    path('states/', StateListCreateView.as_view(), name='state-list'),
    path('states/<int:pk>/counties/', CountyListCreateView.as_view(), name='county-list'),
    path('states/<int:state_id>/counties/<int:county_id>/towns/', TownListCreateView.as_view(), name='town-list')
]

