from django.shortcuts import render
from SubjectsModel.models import Exam, Subject

from django.http import HttpResponse

ans_idx_map_en = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
ans_idx_map_math = ['', '1', '2', '3', '4', '5', '6', '7', '8']

ans_idx_map = ans_idx_map_en

class form_subject:
    def __init__(self, data):
        self.modeldata = data
        self.user_ans = 0
        self.correct_ans = ans_idx_map[0]
        self.is_correct = 0

# Create your views here.
def choose_exam(request):
    exam_list = list(Exam.objects.all().order_by('name'))
    return render(request, 'choose_exam.html', {'exam_list': exam_list})

def make_exam(request):
    if request.method == 'POST':
        exam_paper = request.POST.get("ExamPapers")
        exam_obj = Exam.objects.get(name=exam_paper)
        subjects = list(exam_obj.subjects_set.all())
        context = {'exam_name': exam_paper, 'subjects' : subjects, 'ans_idx_map' : ans_idx_map}
        return render(request, 'make_exam.html', context)
    else:
        return HttpResponse("make_exam!")

def show_recommend(request):
    if request.method == 'GET':
        sid = request.GET.get('sid', '0')
        sub = Subject.objects.get(id=sid)
        context = {'sid': sid, 's': sub}
        return render(request, 'recommend.html', context)
    elif request.method == 'POST':
        sid = request.POST.get("sid", '0')
        sub = Subject.objects.get(id=sid)
        ans = request.POST.get("ans0")
        fs = form_subject(sub)
        fs.user_ans = int(ans)
        if fs.user_ans == sub.answer_idx:
            fs.is_correct = 1
        fs.correct_ans = ans_idx_map[sub.answer_idx]
        context = {'sid': sid, 'fs': fs}
        return render(request, 'recommend.html', context)

def do_recommend(sub):
    # hijack for demo
    if(sub.id == 12):
        return 15
    elif(sub.id == 14):
        return 16
    return sub.id

def mark_exam(request):
    if request.method == 'POST':
        exam_paper = request.POST.get("exam_name")
        exam_obj = Exam.objects.get(name=exam_paper)
        subjects = list(exam_obj.subjects_set.all())
        sub_idx = 0
        form_subject_list = []

        for s in subjects:
            fs = form_subject(s)
            ans_name = "ans" + str(sub_idx)
            ans = request.POST.get(ans_name)
            print("%d) your choise: %d" % (sub_idx, int(ans)))
            print("answer: %d" % (s.answer_idx))
            fs.correct_ans = ans_idx_map[s.answer_idx]
            fs.user_ans = int(ans)

            if fs.user_ans == s.answer_idx:
                fs.is_correct = 1
            else: # Do Recommand
                fs.rec_sid = do_recommend(s)

            form_subject_list.append(fs)
            sub_idx = sub_idx + 1

        context = {'exam_name': exam_paper, 'form_subjects' : form_subject_list, 'ans_idx_map' : ans_idx_map}
        return render(request, 'make_exam.html', context)
    else:
        return HttpResponse("Correct exam!")