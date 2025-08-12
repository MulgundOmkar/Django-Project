from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('team-updates/', views.team_updates, name='team_updates'),
    path('employee-handbook/', views.employee_handbook, name='employee_handbook'),
    path('project-reports/', views.project_reports, name='project_reports'),
    path('hiring/', views.hiring, name='hiring'),
    path('annual/', views.annual_report, name='annual'),
    path('new-services/', views.new_services, name='new_services'),
    path('learn-python/', views.learn_python, name='learn_python'),
    path('learn/', views.learn_python, name='learn_python'),
    path('python-basics/', views.python_basics, name='python_basics'),
    path('flask-framework/', views.flask_framework, name='flask_framework'),
    path('django-framework/', views.django_framework, name='django_framework'),
    path('restful-apis/', views.restful_apis, name='restful_apis'),
    path('full-stack-dev/', views.full_stack_dev, name='full_stack_dev'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    
]
