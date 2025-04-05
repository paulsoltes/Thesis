from django.urls import path
from . import views  # ✅ Import views correctly

urlpatterns = [
    path('', views.index_view, name='index'),  
    path('dashboard/', views.dashboard_view, name='dashboard'),  
    path('logout/', views.logout_view, name='logout'),  
    
    # ✅ Subject Management
    path("add_subject/", views.add_subject, name="add_subject"),  
    path("delete_subject/", views.delete_subject, name="delete_subject"),  # ✅ Now uses POST request
    
    # ✅ Schedule Management
    path("update_schedule/", views.update_schedule, name="update_schedule"),  
    path("update_subject/", views.update_subject, name="update_subject"),  
    path("add-class/", views.add_class, name="add_class"),  # ✅ Add Class API
    
    # ✅ Data Retrieval Endpoints
    path("get_schedule/", views.get_schedule, name="get_schedule"),  
    path("get_subject/", views.get_subject, name="get_subject"),  
    path("get_timetable/", views.get_timetable, name="get_timetable"),  
    path("get_instructor/", views.get_instructor, name="get_instructor"),  
    path("get_room/", views.get_room, name="get_room"),  
    path("get_course/", views.get_course, name="get_course"),  
    path("get_section/", views.get_section, name="get_section"),  
    path("get_time/", views.get_time, name="get_time"),  
    path("get_day/", views.get_day, name="get_day"),  
    path("get_semester/", views.get_semester, name="get_semester"),  
    path("get_year/", views.get_year, name="get_year"),  
    path("get_department/", views.get_department, name="get_department"),  
    path("get_program/", views.get_program, name="get_program"),  

    # ✅ Subject Details Retrieval
    path("get_subject_code/", views.get_subject_code, name="get_subject_code"),  
    path("get_subject_name/", views.get_subject_name, name="get_subject_name"),  
    path("get_subject_type/", views.get_subject_type, name="get_subject_type"),  
    path("get_subject_credit/", views.get_subject_credit, name="get_subject_credit"),  
    path("get_subject_prerequisite/", views.get_subject_prerequisite, name="get_subject_prerequisite"),  
    path("get_subject_corequisite/", views.get_subject_corequisite, name="get_subject_corequisite"),  
    path("get_subject_description/", views.get_subject_description, name="get_subject_description"),  
    path("get_subject_objectives/", views.get_subject_objectives, name="get_subject_objectives"),  
    path("get_subject_outcomes/", views.get_subject_outcomes, name="get_subject_outcomes"),  
    path("get_subject_resources/", views.get_subject_resources, name="get_subject_resources"),  
]
