from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = 'page1-page'),
    path('YearWise.html/',views.YearWise,name = 'page1-YearWise.html'),
    path('InstituteWise.html/',views.InstituteWise,name = 'page1-InstituteWise.html'),
    path('Roundwise.html/',views.Roundwise,name = 'page1-Roundwise.html'),
    path('Roundwise.html/IIT.html/',views.IIT,name = 'page1-IIT.html'),
    path('IIT.html/',views.IIT,name = 'page1-IIT.html'),
    path('IIT.html/',views.IIT,name = 'page1-IIT.html'),
    path('BestCourses.html',views.BestCourses,name='page1-BestCourses.html'),
    path('get-graph-data-roundwise/', views.get_graph_data_roundwise, name='get_graph_data_roundwise'),
    path('get-graph-data-yearwise/', views.get_graph_data_yearwise, name='get_graph_data_yearwise'),
    path('get-bestcourse/', views.get_bestcourse, name='get_bestcourse'),
    path('Knowiit.html', views.KnowIIT, name='Knowiit'),
    path('preferences.html', views.Preferences, name='preferences'),
    path('get-knowiit/', views.get_knowiit, name='get_knowiit'),
    path('get-yearwise/', views.get_yearwise, name='get_yearwise'),
    path('get-institutewise/', views.get_institutewise, name='get_institutewise'),
    path('get-institutewise-name/', views.get_institutewise_name, name='get_institutewise_name'),
    path('get-institutewise-gender/', views.get_institutewise_gender, name='get_institutewise_gender'),
    path('get-roundwise-institute/', views.get_roundwise_institute, name='get_roundwise_institute'),
    path('get-roundwise-name/', views.get_roundwise_name, name='get_roundwise_name'),
    path('get-roundwise-type/', views.get_roundwise_type, name='get_roundwise_type'),
    path('get-preferences/', views.get_preferences, name='get_preferences'),


]


