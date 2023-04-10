from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ),
    path('search',views.search ),
    path('full_info',views.fullInfo),
    path('stud_info/<int:stud_id>',views.stud_info),
    path('update_assignment',views.update_assignment),
]
