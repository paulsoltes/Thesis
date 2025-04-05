from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json

from .models import (
    Subject, Schedule, Instructor, Room, Course, Section, Time, Day,
    Semester, Year, Department, Program
)


# ✅ LOGIN VIEW
def index_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(f"🛠 Attempting login: {username}")  # Debugging

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print("✅ Login successful!")  # Debugging
            login(request, user)
            return redirect("dashboard")
        else:
            print("❌ Login failed!")  # Debugging
            messages.error(request, "Invalid username or password")

    return render(request, "index.html")


# ✅ DASHBOARD VIEW (Protected)
def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect("index")
    return render(request, "dashboard.html")


# ✅ LOGOUT VIEW
def logout_view(request):
    logout(request)
    return redirect("index")


# ✅ ADD SUBJECT
def add_subject(request):
    if request.method == "POST":
        subject_name = request.POST.get("subject_name")
        new_subject = Subject.objects.create(name=subject_name)
        return JsonResponse({"success": True, "subject_id": new_subject.id})
    return JsonResponse({"success": False, "error": "Invalid request method"})


# ✅ DELETE SUBJECT
def delete_subject(request):
    if request.method == "POST":
        subject_id = request.POST.get("subject_id")
        subject = get_object_or_404(Subject, id=subject_id)
        subject.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False, "error": "Invalid request method"})


# ✅ UPDATE SCHEDULE
def update_schedule(request):
    return JsonResponse({"success": True, "message": "Schedule updated!"})


# ✅ ADD CLASS / SCHEDULE
@csrf_exempt
def add_class(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            schedule = Schedule.objects.create(
                instructor=Instructor.objects.get(name=data['instructor']),
                room=Room.objects.get(name=data['room']),
                day=Day.objects.get(name=data['day']),
                start_time=data['start_time'],
                end_time=data['end_time'],
                course=Course.objects.get(name=data['course']),
                subject=Subject.objects.get(name=data['subject']),
                year=Year.objects.get(name=data['year']),
                section=Section.objects.get(name=data['section']),
            )

            class_entry = {
                "instructor": schedule.instructor.name,
                "room": schedule.room.name,
                "day": schedule.day.name,
                "start_time": schedule.start_time,
                "end_time": schedule.end_time,
                "course": schedule.course.name,
                "subject": schedule.subject.name,
                "year": schedule.year.name,
                "section": schedule.section.name,
            }

            return JsonResponse({"success": True, "class_entry": class_entry})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({"success": False, "error": str(e)})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)


# ✅ UPDATE SUBJECT
def update_subject(request):
    return JsonResponse({"success": True, "message": "Subject updated!"})


# ✅ GET ALL DATA HELPERS
def get_model_data(model, fields=None):
    if fields:
        return list(model.objects.values(*fields))
    return list(model.objects.values())


def get_schedule(request):
    return JsonResponse({"schedules": get_model_data(Schedule)})

def get_subject(request):
    return JsonResponse({"subjects": get_model_data(Subject)})

def get_timetable(request):
    return JsonResponse({"timetable": get_model_data(Schedule)})

def get_instructor(request):
    return JsonResponse({"instructors": get_model_data(Instructor)})

def get_room(request):
    return JsonResponse({"rooms": get_model_data(Room)})

def get_course(request):
    return JsonResponse({"courses": get_model_data(Course)})

def get_section(request):
    return JsonResponse({"sections": get_model_data(Section)})

def get_time(request):
    return JsonResponse({"times": get_model_data(Time)})

def get_day(request):
    return JsonResponse({"days": get_model_data(Day)})

def get_semester(request):
    return JsonResponse({"semesters": get_model_data(Semester)})

def get_year(request):
    return JsonResponse({"years": get_model_data(Year)})

def get_department(request):
    return JsonResponse({"departments": get_model_data(Department)})

def get_program(request):
    return JsonResponse({"programs": get_model_data(Program)})


# ✅ GET SUBJECT SPECIFIC DATA
def get_subject_code(request):
    return JsonResponse({"subject_codes": get_model_data(Subject, ['id', 'code'])})

def get_subject_name(request):
    return JsonResponse({"subject_names": get_model_data(Subject, ['id', 'name'])})

def get_subject_type(request):
    return JsonResponse({"subject_types": get_model_data(Subject, ['id', 'type'])})

def get_subject_credit(request):
    return JsonResponse({"subject_credits": get_model_data(Subject, ['id', 'credit'])})

def get_subject_prerequisite(request):
    return JsonResponse({"subject_prerequisites": get_model_data(Subject, ['id', 'prerequisite'])})

def get_subject_corequisite(request):
    return JsonResponse({"subject_corequisites": get_model_data(Subject, ['id', 'corequisite'])})

def get_subject_description(request):
    return JsonResponse({"subject_descriptions": get_model_data(Subject, ['id', 'description'])})

def get_subject_objectives(request):
    return JsonResponse({"subject_objectives": get_model_data(Subject, ['id', 'objectives'])})

def get_subject_outcomes(request):
    return JsonResponse({"subject_outcomes": get_model_data(Subject, ['id', 'outcomes'])})

def get_subject_resources(request):
    return JsonResponse({"subject_resources": get_model_data(Subject, ['id', 'resources'])})
