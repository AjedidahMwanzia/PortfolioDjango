from django.urls import path
from . import views

urlpatterns = [
   path('',views.home ,name= 'home'),
      #    path('api/profile/', views.ProfileList.as_view()),
      #    path('api/project/', views.ProjectList.as_view()),


]