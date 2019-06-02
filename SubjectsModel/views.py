from django.shortcuts import render
from SubjectsModel.models import Exam

from django.http import HttpResponse

# Create your views here.
def choose_exam(request):
    exam_list = list(Exam.objects.all().order_by('name'))
    return render(request, 'choose_exam.html', {'exam_list': exam_list})

def make_exam(request):
    if request.method == 'POST':
        exam_paper = request.POST.get("ExamPapers")
        exam_obj = Exam.objects.get(name=exam_paper)
        subjects = list(exam_obj.subjects_set.all())
        context = {'exam_name': exam_paper, 'subjects' : subjects}
        return render(request, 'make_exam.html', context)
    else:
        return HttpResponse("make_exam!")

def mark_exam(request):
    if request.method == 'POST':
        return HttpResponse("Correct exam!")
    else:
        return HttpResponse("Correct exam!")