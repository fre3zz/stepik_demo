from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render

# Create your views here.

week = 4
course = "Django"
group = "2706"
students = {
    1: "ААА",
    2: "БББ",
    3: "ВВВ",
    4: "ГГГ"
}

def main(request: HttpRequest):
    return render(request, "week1/index.html", context={
        "week": week,
        "course": course,
        "group": group,
    })


def about(request: HttpRequest):
    return render(request, "week1/about.html")

def student(request: HttpRequest, student_id):
    try:
        student = students[student_id]
    except KeyError:
        raise Http404

    return render(request, "week1/student.html", context={
    'student': student
    }
    )
